class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print self.health, self.name
		return self

animal1 = Animal('animal1')
animal1.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):
	def __init__(self, name):
		self.name = name
		self.health = 150
	def pet(self):
		self.health += 5
		return self

dog1 = Dog('dog1')
dog1.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name) 
		self.health = 170
	def fly(self):
		self.health -=10
		return self
	def displayHealth(self):
		print 'this a dragon'
		super(Dragon, self).displayHealth()

dragon1 = Dragon('dragon1')
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()


