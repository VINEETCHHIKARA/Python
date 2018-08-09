class Addition:
	count=0
	def __init__(self,num1,num2):
		self.num1=num1
		self.num2=num2
		Addition.count=Addition.count+1;

	def sum(self):
		return self.num1+self.num2
		

	
	def __del__(self):
		self.num1=0
		self.num2=0




class Multiply(Addition):
	def __init__(self,num1, num2):
		self.num1=num1
		self.num2=num2
		self.num3=num1
		self.num4=num2


	def multy(self):
		return self.num3 * self.num4

	def sum(self):
		return self.num3+9




mul = Multiply(3,5)
print ("The multiply of two number is ",mul.multy())
print ("The multiply of two number is ",mul.sum())

