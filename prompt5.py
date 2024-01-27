import numpy as np

from astropy.table import Table


#two functions to create arrays np.linspace and np.arange
# arange is good when you know the increments between the elements while
#the linspace is good for the number of elements


#highlith the all things and then put brackets around it if you forgot to put brackets 
#around it

#command s to save it without having to exit


def main():
	x = np.linspace(0,2*np.pi,1000)
	y = np.sin(x)
	
	data_table = Table()

	data_table["x"] = x
	data_table["y"] = y

	print(data_table)



if __name__=="__main__":
	main()


	
