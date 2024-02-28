# Python3 program to implement Eulers
# Factorization algorithm
from math import gcd
	
# Function to return N as the sum of
# two squares in two possible ways
def sumOfSquares(n, vp):

	# Iterate a loop from 1 to Math.sqrt(n)
	for i in range(1, 1 + int(n ** 0.5)):

		# If i*i is square check if there
		# exists another integer such that
		# h is a perfect square and i*i + h = n
		h = n - i * i
		h1 = int(h ** 0.5)
	
		# If h is perfect square
		if (h1 * h1 == h):
				
			# Store in the sorted way
			a = max(h1, i)
			b = min(h1, i);
			
			# If there is already a pair
			# check if pairs are equal or not
			if (len(vp) == 1 and a != vp[0][0]):
				vp.append([a, b]);
	
			# Insert the first pair
			if (len(vp) == 0):
				vp.append([a, b]);
	
			# If two pairs are found
			if (len(vp) == 2):
				return;
	
# Function to find the factors
def findFactors(n):

	# Get pairs where a^2 + b^2 = n
	vp = [];
	sumOfSquares(n, vp);

	# Number cannot be represented
	# as sum of squares in two ways
	if (len(vp) != 2):
		return []


	a = vp[0][0]
	b = vp[0][1];
	
	c = vp[1][0];
	d = vp[1][1];
	
	# Swap if a < c because
	# if a - c < 0,
	# GCD cant be computed.
	if (a < c):

		t = a;
		a = c;
		c = t;
		t = b;
		b = d;
		d = t;
	
	# Compute the values of k, h, l, m
	# using the formula mentioned
	# in the approach
	k = gcd(a - c, d - b);
	h = gcd(a + c, d + b);
	l = (a - c) // k;
	m = (d - b) // k;

	# Print the values of a, b, c, d
	# and k, l, m, h
	print("a = ", a, "	    (A) a - c = ", (a - c), "	    k = gcd[A, C] = ", k, sep = "");
	print("b = ", b, "	    (B) a + c = ", (a + c), "	    h = gcd[B, D] = ", h, sep = "");
	print("c = ", c, "	    (C) d - b = ", (d - b), "	    l = A/k       = ", l, sep = "");
	print("d = ", d, "	    (D) d + b = ", (d + b), "	    m = c/k       = ", m, sep = "");
	
	# Printing the factors
	if (k % 2 == 0 and h % 2 == 0):
		k = k / 2
		h /= 2
		return [((k) * (k) + (h) * (h)), (l * l + m * m)]
	
	else:
	
		l = l / 2;
		m = m / 2;
		return [((l) * (l) + (m) * (m)), (k * k + h * h)]