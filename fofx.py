def f_of_x(x):
	b = (x**3)+8 #take x to the power of 3 and add 8. 
	return b

def main():
	print(f_of_x(9))
	if(f_of_x(9)>27):
		print("YAY!")

if __name__=="__main__":
	main()