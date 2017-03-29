from django.test import TestCase
import time
# Create your tests here.

# print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


class maopao:
    def __init__(self,number):
        self.a=number

    def bubble_sort(self,number):
        self.number=number
        for j in xrange(len(self.number)-1,-1,-1):
            for i in xrange(j):
                if number[i]> number[i+1]:
                    number[i],number[i+1]=number[i+1],number[i]
                    print number
def main():
    pass

if __name__ =='__main__':
    main()
    number=[23,12,9,15,6]
    a=maopao(number)
    a.bubble_sort(number)