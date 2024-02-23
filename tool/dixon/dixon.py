from math import sqrt, gcd
import numpy as np


def factorizateDixon(n):

	base = [2, 3, 5, 7]
	start = int(sqrt(n))

	pairs = []

	for i in range(start, n):
		for j in range(len(base)):
			lhs = i**2 % n
			rhs = base[j]**2 % n
			
			if(lhs == rhs):
				pairs.append([i, base[j]])

	new = []

	for i in range(len(pairs)):
		factor = gcd(pairs[i][0] - pairs[i][1], n)

		if(factor != 1):
			new.append(factor)

	x = np.array(new)

	return(np.unique(x))
