s = '218916754'
qq = ''
while True:
    qq += s[0]
    if len(s) > 1:
        s = s[2:]+s[1:2]
    else:
        break
print qq

