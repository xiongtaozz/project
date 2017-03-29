from django.test import TestCase

num =0
for i in range(4,10000,4):
        count = 0
        m = i
        for k in range(5):
            j = i / 4 * 5 + 1
            i = j
            if j % 4 == 0:
                count += 1
            else:
                break
        i = m
        num +=count
        if count == 4:
            print count
            break
print '----------------------------'
x=1
while True:
    s = x
    for i in range(5):
        num = (s-1)%5
        if not num:
            s = (s-1)/5
            s = s * 4
        else:
            break
    else:
        print x
        break
    x += 1