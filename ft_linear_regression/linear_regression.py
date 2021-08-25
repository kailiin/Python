import pandas as pd
import matplotlib.pyplot as plt
import sys

alpha = float(0.1)
init_theta0 = float(0)
init_theta1 = float(0)
iterations = 2000

# show result graphe
def data_graphe(dataX, dataY, result):
	plt.plot(dataX, dataY, 'o')
	plt.plot(dataX, result)
	plt.ylabel("Price")
	plt.xlabel("Km")
	plt.show()

# find theta0 and theta1
# p0 = x + k0 * y
# p1 = x + k1 * y
# => y = (p0 - p1) / (k0 - k1) and x = p0 - k0 * y
def find_save_theta(dataX, dataY):
	y = (dataY[0] - dataY[1]) / (dataX[0] - dataX[1])
	x = dataY[0] - (dataX[0] * y)
	try:
		f = open("theta.csv","w")
		f.write("%f,%f" % (x, y))
	except:
		print("Error: Can't save theta.csv!")
		print("theta0 = %f and theta1 = %f" % (x, y))

# Min-max feature scaling
def normalization(dataX, dataY, dataSize):
	maxX = max(dataX)
	minX = min(dataX)
	maxY = max(dataY)
	minY = min(dataY)
	listX = []
	listY = []
	for i in range(dataSize):
		listX.append((dataX[i] - minX) / (maxX - minX))
		listY.append((dataY[i] - minY) / (maxY - minY))
	return [listX, listY]	

def denormalization(val, minVal, maxVal):
	return val * (maxVal - minVal) + minVal

def estimate_price(t0, t1, x):
	return t0 + t1 * x

def linear_regression(dataX, dataY ,dataSize):
	theta0 = init_theta0
	theta1 = init_theta1
	for i in range(iterations):
		tmp0 = 0.
		tmp1 = 0.
		for i in range(0, dataSize):
			tmp0 += (estimate_price(theta0, theta1, dataX[i]) - dataY[i])
			tmp1 += ((estimate_price(theta0, theta1, dataX[i]) - dataY[i]) * dataX[i])
		theta0 -= (alpha * tmp0 ) / dataSize
		theta1 -= (alpha * tmp1) / dataSize
	return [theta0, theta1]

if __name__ == "__main__":
	# read and get csv data
	try:
		df = pd.read_csv("data.csv")
		dataX =  df.iloc[0:len(df), 0]
		dataY =  df.iloc[0:len(df), 1]
		dataSize = len(dataX)
		if (len(dataX) != len(dataY)) | dataSize < 10:
			raise
		for i in range(dataSize):
			int(dataX[i])
			int(dataY[i])
	except:
		print("Error: scv file error!")
		sys.exit()

	# normalization and regression 
	[norm_dataX, norm_dataY] = normalization(dataX, dataY, dataSize)
	[theta0, theta1] = linear_regression(norm_dataX, norm_dataY, dataSize)

	# estimate price with new theta and denormalization
	resultY = []
	for x in norm_dataX:
		resultY.append(estimate_price(theta0, theta1, x))
	maxDataY = max(dataY)
	minDataY = min(dataY)
	for i in range(dataSize):
		resultY[i] = denormalization(resultY[i], minDataY, maxDataY)

	# show data graphe and save theta
	find_save_theta(dataX, resultY)
	data_graphe(dataX, dataY, resultY)
