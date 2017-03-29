str ='218916754'
list=[]
li=[]
str1=''
for x in str:
    list.append(x)
def dre():
	global li,list

	for x in range(len(list)):
		if x==0:
			li.append(list[x])
			list.remove(list[x])
		if x==1:
			a=list[x-1]
			list.remove(list[x-1])
			list.append(a)
		if len(list)<2:
			break

for x in range(len(str)):
	dre()


for i in li:
	str1 +=i
print str1