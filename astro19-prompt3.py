import numpy as np
import sys


def f(x):
	operation = x**3 + 8
	return operation


x = 9

def main():
	f(x)
	
	print(f(x))
	


if __name__ =="__main__":
	main() 

"""print(main())"""


if f(x) > 27:
	print("YAY!")