import random
import time






def joma(performance):
	count = len(performance)
	bonus = [1] * count
	for i in range(1,count):
		if performance[i-1] < performance[i]:
			bonus[i] = bonus[i - 1] + 1
	
	for i in range(count - 2, -1, -1):
		if performance[i+1] < performance[i]:
			bonus[i] = max(bonus[i], bonus[i + 1] + 1)
	
	return bonus

def test(l):
	return


original = [1,2,3,2,3,5,1]



def repeating(l):
	r = []
	for i in range(len(l)):
		for j in range(len(l)):
			if l[i] == l[j] and i != j and l[i] not in r:
				r.append(l[i])
	return r

t = [2,2,3,3,4,4,5,1]
start_time = time.time()
print(str(repeating(t)))
