s = '218916754'
while True:
    if len(s)==0:
        break
    else:
        b = s[1:]
        print s[0]
        c = b[1:] +b[0:1]
        s = c