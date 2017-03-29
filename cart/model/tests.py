from django.test import TestCase

# Create your tests here.

data = [3,6,4,9,2,1]

class BetModel(object):

    def __init__(self,model,bet=12,signal_list=[]):
        self.model = model
        self.bet = bet
        self.signal_list=signal_list
    def transformModel(self):
        for i in data:
            if i in self.model:
                self.signal_list.append(1)
            else:
                self.signal_list.append(-1)

a1 = BetModel( )
b1 = BetModel( )
a1.model = [1,2,3,4]
b1.model = [4,5,6,7]
a1.transformModel( )
b1.transformModel( )
print a1.signal_list,b1.signal_list



sum=0
class a :
    global sum
    sum+=1
    print sum




