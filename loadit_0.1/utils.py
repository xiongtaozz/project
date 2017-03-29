import os, sys
import Tkinter


def config_validate_task(task):
	if task['baseurl'] == 'http://202.118.83.94:85/':
		task['class'] = 'grsloader'
		return 0
	elif task['baseurl'] == None:
		return 1
	else:
		print >> stderr, '[ERROR] %s is NOT supported currently. Pls notice us to put it into the wish list <rchen.cs@gmail.com>'
		return 1

def config_validate_course(course, ddlYear, ddlTerm):
	pass

def config_validate_scorein(file):
	pass

# read configure file
def config(file='loadit.cfg', tasks = []):
	try:
		filein = open(file, 'r')
	except IOError:
		print >> sys.stderr, '[ERROR] open %s!'%file
		return 1
	else:
		for line in filein:
			if line[0]=='#' or line[0]=='\r' or line[0]=='\n': continue
			print '[INFO ]', line
			fields = line.split(' ')
			assert len(fields)==7, '[ERROR] The fields in this line is insufficient!'
			task ={}
			task['baseurl'] = fields[0].strip()
			config_validate_task(task)
			task['course'] = fields[1].strip()
			task['year'] = fields[2].strip()
			task['term'] = fields[3].strip()
			task['scorein'] = fields[4].strip()
			task['examtime'] = fields[5].strip()
			task['scoretype'] = fields[6].strip()
			task['stage'] = 'n/a'
			tasks.append(task)
		filein.close()
		return 0

# read score file
def read_scores(task, scoresin=[]):
	file = task['scorein']
	print '[INFO ] read score file %s'%file
	try:
		filein = open(file, 'r')
	except IOError:
		print >> sys.stderr, '[ERROR] open %s!'%file
		return 1
	else:
		for score in filein:
			if score[0]=='#' or score[0]=='\r' or score[0]=='\n': continue
			s = score.strip(' ')
			if task['scoretype']=='1':
				assert (0<=int(s) and int(s) <= 100), '[ERROR] The score %s in this line is not within [0..100]!'%s
			else:
				assert ('A'<=s and s <= 'E'), '[ERROR] The score %s in this line is not within [A..E]!'%s
			scoresin.append(s)
		filein.close()
		return 0

# if  __name__ == '__main__':
	# tasks = []
	# config(tasks=tasks)
	# print '[INFO ]', tasks
