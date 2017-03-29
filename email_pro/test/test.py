s = '218916754'
t = ''
while True:
    t += s[0]
    if len(s)>2:
        s += s[2:] +s[1]
    else:
        break

print t
