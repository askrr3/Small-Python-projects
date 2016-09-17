# class Human(object):
#     def __init__(self):
#       print "New Human!!!"     #when we create a new human, we'll get this as an output
#     def taunt(self):
#       print "You want a piece of me?"


class bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayinfo(self):
		print self.price, self.max_speed, self.miles
		return self

	def ride(self):
		print
		self.miles += 10
		return self

	def reverse(self):
		print 
		self.miles -= 5
		return self


bike1 = bike(200,'25mph', 0)
bike1.ride().ride().ride().reverse().displayinfo()


# .ride().ride().reverse().displayinfo()



bike2 = bike(200,'25mph',0)
bike2.ride().ride().ride().reverse().displayinfo()

# .ride().reverse().displayinfo()


bike3 = bike(200,'25mph',15)
bike3.reverse().reverse().reverse().displayinfo()








