import random

# implementing monte-carlo solver for random walk https://www.youtube.com/watch?v=BfS2H1y6tzQ

def random_walk(n):
	""" 
	Return a tuple of (x,y) co-ordinates after 'n' random steps.

	"""
	x,y=0,0
	for i in range(n):
		dx,dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
		x += dx
		y += dy

	# print("final x,y = (%d,%d) after %d iterations" % (x,y,n))

	return (x,y)
		


# Problem 1
# what is the longest random walk you can take so that on average (> 50%)
# you will end up 4 blocks or fewer from home

def n_blocks_or_fewer(num_blocks = 4,max_walk_length = 31, iterations = 1000, percentage_succeed = 0.5):
	"""
	returns the longest random walk value 'n' that you can take so that on average you will end up
	'num_blocks' or fewer from home. 
	if supplied 'max_walk_length' is the maximum length of each walk taken else 31
	if supplied 'iterations' is the number of iterations on each walk length else 1000
	if supplied 'percentage_succeed' is the minimum required percent of success (e.g. 0.6 of the time, 0.5 of the time or better)
	"""

	walk_length_average_blocks = build_dict_of_walks(num_blocks, max_walk_length,iterations,percentage_succeed)



	# return the largest value percentage_succeed or greater --> reverse iterate the dict

	for i in range(max_walk_length-1,0,-1):
		print( "COMPARING: " +str(i) + " - " + str(walk_length_average_blocks[i]) + " vs " + str(percentage_succeed) )
		if(walk_length_average_blocks[i] >= percentage_succeed):
			print("SOLUTION: "+ str(i))

			return i



# refactor

def build_dict_of_walks(num_blocks = 4,max_walk_length = 31, iterations = 1000, percentage_succeed = 0.5):
	"""
	returns the longest random walk value 'n' that you can take so that on average you will end up
	'num_blocks' or fewer from home. 
	if supplied 'max_walk_length' is the maximum length of each walk taken else 31
	if supplied 'iterations' is the number of iterations on each walk length else 1000
	if supplied 'percentage_succeed' is the minimum required percent of success (e.g. 0.6 of the time, 0.5 of the time or better)
	"""

	walk_length_average_blocks = {}

	# randomly walk up to N steps
	for walk_length in range(max_walk_length):
		num_blocks_or_fewer = 0
		success_percentage = 0.0
		for i in range(iterations):
			final_x, final_y = random_walk(walk_length)
			manhattan_distance = abs(final_x) +abs(final_y)

			if manhattan_distance <= num_blocks:
				num_blocks_or_fewer += 1
		success_percentage = float(num_blocks_or_fewer) / iterations

		walk_length_average_blocks[walk_length] = success_percentage

	return walk_length_average_blocks




def main():
	n_blocks_or_fewer(4,31,1000,0.6)



if __name__ == '__main__':
	main()
