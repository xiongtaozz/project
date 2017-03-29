#coding:utf-8
# 有桔子不吃苹果 2015/11/24 11:09:25
for x in range(10000):
    if x % 5 == 1:
        for i in range(5):
            x = x*0.8 - 1
            if x % 5 != 1:
                break
            elif i == 4:
                print(x)

# for x in range(10000):
#     if x%5 ==1:
#         for i in range(5):
#             x = x * 0.8 - 1
#             if x % 5 !=1:
#                 break
#             else:
#                 print x