# codding:utf-8

l = '[1,2,3,4,5,63]'

print [int(x) for x in l[1:-1].split(',')]

l1 = []
for x in l[1:-1].split(','):
    l1.append(int(x))
print l1

# [1,2,3,4,5,63]