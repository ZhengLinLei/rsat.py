# Python code for Pollard p-1 
# factorization Method
	

import math
	

def factorizatePm1(n):
	
	a = 2
	i = 2
	
	while(True):
		a = (a**i) % n
		d = math.gcd((a-1), n)
		if (d > 1):
			return d

		i += 1
