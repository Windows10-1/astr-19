class Penguin:

	def __init__(self):
		self.arms = 38
		self.eyes = 2
		self.tail = True
		self.hair = False

	def __str__(self):
		return f"This penguin has an arm length of {self.arms}cm and {self.eyes} eyes.\nDoes it have a tail?: {self.tail}\nDoes it have fur: {self.hair}"


def main():
	p1 = Penguin()
	print(p1)

if __name__=="__main__":
	main()

