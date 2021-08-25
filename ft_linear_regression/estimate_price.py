import sys
import os.path

from numpy import string_

def estimate_price(t0, t1, x):
	return t0 + t1 * x

if __name__ == "__main__":
	if len(sys.argv) == 2:
		x = sys.argv[1]
		t0 = 0
		t1 = 0
		if (x.isdigit()):
			if (os.path.isfile("theta.csv")):
				try:
					f = open("theta.csv","r")
					line = f.readline()
					str = line.split(',')
					t0 = float(str[0])
					t1 = float(str[1])
				except:
					print("Error: theta.csv error!")
					sys.exit()
			result = estimate_price(t0, t1, int(x))
			if (result < 0):
				result = 0
			print("Estimate price: %d" % int(result))
		else:
			print("Error: argv[1] must be a positive integer!")
	else:
		print("usage: python3 estimate_price.py km")
