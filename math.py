
class MathDojo(object):
	def __init__(self, sum=0):
		# self.name = name
		self.sum = sum
	
	def add(self, *args):
		for i in range(0,len(args)):
			self.sum += args[i]
		# print self.sum
		return self
		
	def subtract(self, *args):
		for i in range(0,len(args)):
			self.sum -= args[i]
		print self.sum
		return self

md = MathDojo()
print md.add(2,4,5,6,7).subtract(3,2)

# part 2


# class MathDojo(object):
# 	def __init__(self, sum=0):
# 		self.sum = sum
	
# 	def add(self, *args):
# 		for i in range(0,len(args)):
# 			if type(args[i]) is list or type(args[i]) is tuple:
# 				for x in xrange(0,len(args[i])):
# 					self.sum += args[x]
# 			else:
# 				self.sum += args[i]
# 		return self
		
# 	def subtract(self, *args):
# 		for i in range(0,len(args)):
# 			if type(args[i]) is list or type(args[i]) is tuple:
# 				for x in range(0,len(args[i])):
# 					self.sum -= args[x]
# 			else:
# 				self.sum -= args[i]
# 		print self.sum
# 		return self

# md = MathDojo()
# print md.add(1,[1],1).subtract(1,1)


# # .subtract(1,1)