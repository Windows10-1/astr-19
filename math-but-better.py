#adds 2 float numbers. in retrospect, i could do user input. (8/3/23)
#this is why i dont make notes sometimes (8/10/23)
def FloatAdd():
	while True: #while loop to keep it running for user input
		try:
			i=float(input('Adding! please enter a float:')) #input1
			b=float(input('Now enter another float:')) #input2
			break 
		except ValueError:
			print("Not a float! Again!") #not a float 
	#math time!
	c = i+b 
	print(c)
	print(type(c))

def IntDiff():
	while True: #copy paste is a magical thing.
		try:
			a=int(input('Int subtraction! Enter an integer: '))
			b=int(input('Now enter another integer: '))
			break 
		except ValueError:
			print("Not an integer, try again.")
	#bug fix; prevents the computer from doing the math wrong if one number is bigger than the other.
	if a>b: 
		c = a-b
	else:
		c = b-a
	print(c)
	print(type(c))

def FloatAndInt():
	while True: #ctrl c, ctrl v to prevent having to write the same while loop 3 times 
		try:
			a=float(input('Oh boy, floats and ints! Enter a float:'))
			b=int(input('Now enter an intger and watch the multiplication! '))
			break 
		except ValueError:
			print("Come on really? Again!")
	#simple multiplication 
	c = b*a
	print(c)
	print(type(c))

def main():
	FloatAdd()
	IntDiff()
	FloatAndInt()

if __name__=="__main__":
	main()