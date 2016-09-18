def multiply(a,b):
	print(a)
	for x in range(0,len(a)):
		a[x] = a[x] * b
	return a
a = [2,4,10,16]
b = 5
c = multiply(a,b)
print c





# def multiply(a, b):
# 	for x in range(0,len(a)):
# 		(x * b)
# a = [2,4,10,16]
# b = multiply(a, 5)
# print b