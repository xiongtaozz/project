
list =['16\u65e5 \u5468\u4e94','\u767d\u5929','\u6674']

for x in range(len(list)):
    print list[x].decode('raw_unicode_escape')
