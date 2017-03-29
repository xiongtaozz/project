x = 1
while (x <= 9):
    y = 1
    while (y <= x):
        # print (str(y) + "*" + str(x) + "=" + str(y*x)),
        print ("{0}*{1}={2}".format(y,x,y*x)),
        y += 1
    print
    x += 1
