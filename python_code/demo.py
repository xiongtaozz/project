# coding:utf-8
import code_15118.demo01


def perfectNumber(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
    if num == sum:
            print(num)

while True:
    try:
        num = int(input("enter input number:"))
        break
    except ValueError:
        print(u"输入错误，请重新输入。。。。")

perfectNumber(num)
print("Done")