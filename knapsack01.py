# bottom up dynamic programming
# python3


def knapsack01(path_to_data):
	# creates a list of pairs (weight, value) from path_to_data file
	try:
		fh = open(path_to_data, "r")
	except FileNotFoundError:
		print("(-) Error reading data file, aborting!!")
		raise SystemExit
	W_V_DATA = []
	for line in fh.read().splitlines():
		a, b = line.split()
		W_V_DATA.append((int(a), int(b)))
	fh.close()
	N = len(W_V_DATA)

	try:
		W = int(input("write capacity W:   "))
	except ValueError:
		print("(-) Wrong input, aborting!!")
		raise SystemExit
		
	# initializates bottom up table to fill
	k = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
	
	# building table k[][]
	for n in range(N + 1):
		for w in range(W + 1):
			if n == 0 or w == 0:
				k[n][w] = 0
			elif W_V_DATA[n-1][0] <= w:
				k[n][w] = max(W_V_DATA[n-1][1] + k[n-1][w-W_V_DATA[n-1][0]],  k[n-1][w])
			else:
				k[n][w] = k[n-1][w]
	
	# recursion to find ALL optimal subsets
	# works comparing k[N][W] with value
	# up in table saving a list of possible
	# best subsets
	comp_all = [[]]
	comps = []
	a = N
	b_vect = [W]
	while True:
		i = 0		
		for b in b_vect:
			# For debugging purposes
			# print("a=   ", a, "b_vect=   ", b_vect)
			# print("i=  ", i)
			# print("k[a][b] =    ", k[a][b])
			# print("k[a-1][b]=    ", k[a - 1][b])
			# print("comp_all=   ", comp_all)
			# print("------------------")
			if k[a][b] == 0:
				pass
			elif k[a][b] > k[a-1][b]:
				comp_all[i].append(W_V_DATA[a-1][1])
				b_vect[i] -= W_V_DATA[a-1][0]
			else:
				# corresponds to k[a][b] == k[a-1][b]
				if W_V_DATA[a-1][0] <= b:
					candidate = comp_all[i] + [W_V_DATA[a-1][1]]
					comp_all.append(candidate)
					b_new = b - W_V_DATA[a-1][0]
					b_vect.append(b_new)
					break
			i += 1
		a -= 1
		k_ab_vect = [k[a][b] for b in b_vect]
		if sum(k_ab_vect) == 0:
			break
# filtering best compositions			
	for c in comp_all:
		if sum(c) == k[N][W]:
			comps.append(c)
		
	print("\nDP Bottom-Up Table   ")
	for line in k:
		print(line)
	print("DATA   \n", W_V_DATA)
	print("Best Compositions   \n", comps)


if __name__ == "__main__":
	knapsack01("data.txt")


# Time complexity for DP bottom-up O(WN)
# Time complexity for finding all optimal subsets O(2^N) [probably O(N^2)]