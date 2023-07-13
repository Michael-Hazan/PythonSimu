import random 

def calculatePI(precision):
	innerAmount = 0
	for i in range(precision):
		x = random.uniform(-1, 1)
		y = random.uniform(-1, 1)
		if x**2+y**2 <= 1**2:
			innerAmount += 1
	pi = 4*innerAmount / precision
	return pi

if __name__ == "__main__":
	precision = 0
	ran = 1
	while precision <= 0:
		precision = int(input("Precision of calculation (PI): "))
	print(calculatePI(precision))