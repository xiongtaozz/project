class Factory:
	def createFruit(self,fruit):
		if fruit=="apple":
			return Apple()
		elif fruit=="banana":
			return Banana()
class Fruit:
	def __str__(self):
		return "fruit"
class  Apple(Fruit):
	def __str__(self):
		return "apple"
class Banana(Fruit):
	def __str__(self):
		return "banana"

if __name__=="__main__":
    factory=Factory()
    print factory.createFruit("apple")
    print factory.createFruit("banana")
