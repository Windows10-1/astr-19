#adds 2 float numbers. in retrospect, i could do user input. 
def FloatAdd():
	a = 3.721
	b = 5.312
	c = a+b
	print(c)
	print(type(c))

def IntDiff():
	a = 2
	b = 3
	c = b-a
	print(c)
	print(type(c))

def FloatAndInt():
	a = 0.5
	b = 4
	c = b*a
	print(c)
	print(type(c))

def main():
	FloatAdd()
	IntDiff()
	FloatAndInt()

if __name__=="__main__":
	main()