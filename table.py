import numpy as np
from astropy.table import Table
import math

def TableMaker():
	x = np.linspace(0,2*math.pi, 1000)
	y = np.copy(x)
	y = np.sin(y)
	func = Table([x,y], names=['x','Sin(x)'])
	return func

def main():
	print(TableMaker())

if __name__=='__main__':
	main()