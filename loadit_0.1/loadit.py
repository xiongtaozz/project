import os, sys, argparse
import Tkinter as tk
from utils import *
from loader import GRSLoader, Loader

LOADER_OBJECTS = {'grsloader':GRSLoader,'loader':Loader}

class LoaditApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        toolbar = tk.Frame(self)
        toolbar.pack(side="top", fill="x")
        btnExec = tk.Button(self, text="Execute", command=self.exec_tasks)
        b1 = tk.Button(self, text="print config", command=self.print_config)
        b2 = tk.Button(self, text="print status", command=self.print_status)
        btnExec.pack(in_=toolbar, side="left")
        b1.pack(in_=toolbar, side="left")
        b2.pack(in_=toolbar, side="left")
        self.output = tk.Text(self, wrap="word")
        self.output.pack(side="left", fill="both", expand=True)
        scroll = tk.Scrollbar(self)
        scroll.pack(side="right", fill="y")
        scroll.config(command=self.output.yview)
        self.output.config(yscrollcommand=scroll.set)
        self.output.tag_configure("stderr", foreground="#b22222")

        sys.stdout = TextRedirector(self.output, "stdout")
        sys.stderr = TextRedirector(self.output, "stderr")

        self.loader_objects = LOADER_OBJECTS
        self.tasks = []
        config(tasks=self.tasks)
        self.task=self.tasks[0]

    def create_loader(self, key):
    	return self.loader_objects[key](app=self)

    def exec_tasks(self):
        '''Execute the tasks on request'''
        for t in self.tasks:
        	self.task = t
        	loader = self.create_loader(t['class'])
        	loader.login(url='login.aspx')
        	loader.query_by_form(url='Teacher/ScoreInput.aspx?m=webm_Tea_Maintinfo_scorein', ddlYear=t['year'], ddlTerm=t['term'], debug='debug')
        	loader.load_scores(txtExamTime=t['examtime'], rblTag=t['scoretype'], debug='debug')


    def print_config(self):
        '''Using 'print' writes loadit.cfg to stdout'''
        print '\n=== Task list ==='
        print '#baseurl #course #year #term #scorein #examtime #scoretype'
        for i,t in enumerate(self.tasks):
            print t['baseurl'], t['course'], t['year'], t['term'], t['scorein'], t['examtime'], t['scoretype']
        print '\n'

    def print_status(self):
        '''Write current execution status directly to stderr'''
        print '\n=== Task status ==='
        for i,t in enumerate(self.tasks):
            msg = "T%d. %s %s state: %s"%(i,t['course'], t['year'], t['stage'])
            if t['stage']=='n/a' or t['stage']=='load_scoreloaded':
                print msg
            else:
                sys.stderr.write(msg)
        print >> sys.stderr, '\n'


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")


class Loadit(LoaditApp):
	def __init__(self):
		pass

	def __init__(self, tasks):
		self.loader_objects = LOADER_OBJECTS
		self.tasks = tasks



if  __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Load data from external data files into information management systems on dlmu.edu.cn', prog='loadit')
	parser.add_argument('-t', '--task', nargs='?', metavar='ALL/filename', 
                   help='complete ALL tasks in loadit.cfg, or tasks in the specified file')
	args = parser.parse_args()
	print args
	if args.task != None:
		tasks = []
		if args.task != 'ALL':
			status = config(file=args.task, tasks=tasks)
		else:
			status = config(tasks=tasks)
		if status == 0:
			loadit = Loadit(tasks)
			loadit.exec_tasks()
			
	else:
		app = LoaditApp()
		app.mainloop()