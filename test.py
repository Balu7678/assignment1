# Python3 program for 
# the above approach

# Function to count triplets
def CountTriplets(a, d):

	cnt = 0

	for i in range(0, d):
		for j in range(i + 1, d):
			for k in range(j + 1, d):

				# If it satisfy the
				# given conditions
				t=a[i]+a[j]+a[k]
				if t
					cnt += 1
				
	# Return the final count
	return cnt


# Driver code
if __name__ == "__main__": 
	a = [3,3,4,7,8]
	d = len(a)
	print (CountTriplets(a, d))

# This code is contributed by Chitranayal

