s = '218916754'
sumer=''
while True:
    if len(s)==0:
        break
    else:
        b = s[1:]
        sumer += s[0]
        s = b[1:] +b[0:1]
print sumer