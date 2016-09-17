class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = .15
		else:
			self.tax = .12

	def display_all(self):
		print self.price, self.speed, self.fuel, self.mileage, self.tax

car1 = Car(2000, '35mph', 'full', '15mpg')
car1.display_all()

