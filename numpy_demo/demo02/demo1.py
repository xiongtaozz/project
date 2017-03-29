# coding:utf-8

import numpy as np
import datetime


# i2 = np.eye(2)
# print i2
# np.savetxt('eye.txt',i2)

path = 'C:/Users/wangbiao/Desktop/nump.csv'

c, v, x = np.loadtxt(path, delimiter=',', usecols=(3,4,5), unpack=True)
print c
print v
print x
print 'c median', np.median(c)  # 中位数
sort_close = np.msort(c)
print 'sorted =', sort_close
N = len(c)
# print 'midde =', sorted([(N-1)/2])
# print 'average middle =', (sorted[N / 2] + sorted[(N - 1) / 2]) / 2
print 'variance =', np.var(c)  # 方差
print 'variance from definition =', np.mean((c-c.mean())**2)

def datestrnum(s):
    return datetime.datetime.strptime(s, '%Y/%m/%d').date().weekday()

dates, close = np.loadtxt(path, delimiter=',', usecols=(1, 6), unpack=True, converters={1: datestrnum})
print 'Dates = ', dates

# 股票收益

averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print "Day", i, 'prices', prices, 'average', avg
    averages[i] = avg

# 找出每周1 .在寻找周1的坐标
first_monday = np.ravel(np.where(dates == 0))[0]
print "The first Monday index is", first_monday
# 同理
last_friday = np.ravel(np.where(dates == 4))[-1]
print 'The last Friday index is', last_friday
# 按照每个子数组5个元素,用于存储三天内没一日按的索引
weeks_indices = np.arange(first_monday, last_friday+1)
print 'weeks indices initial', weeks_indices
# 按照每个子数组5个元素,用split函数切片
weeks_indices = np.split(weeks_indices, 5)
print 'weeks indices after split', weeks_indices





