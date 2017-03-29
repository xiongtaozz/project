# -*- coding:utf-8 -*-  
lines=[]
names=[]
fullName = []
linesWithoutGetting=[]
paths=[]
filename=[]
fullName=[]


f = open("vsslistfile.txt", "r")  
while True:  
    line = f.readline()  
    if line:  
       lines.append(line)
    else:  
        break  

fullName = []
linesWithoutGetting=[]
paths=[]
file=[]
exportfile=[]



dot = '.'
dallor = '$'
colon =':'


for str in lines:
   linesWithoutGetting.append(str.replace("Getting ", "").replace("Getting", ""))

path = ""
for str in linesWithoutGetting:
      if (str.find(dot))>=0:
       exportfile.append(str)

            

            

for str in exportfile:
    with open("vsslistfile11.txt", 'a') as f:
        f.write(str+"=rw" + "\n")

f.close()
 