import random
red_ball=range(1,34)
blue_ball=range(1,17)
n=1
while n<8:
    if n<=6:
        k=random.choice(red_ball)
        print k
        red_ball.remove(k)
        n +=1
    else:
        print random.choice(blue_ball)
        break
        # x =random.chioce(blue_ball)
        # print x
