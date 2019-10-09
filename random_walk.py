import random


def random_walk(n):
	""" 
	Return a tuple of (x,y) co-ordinates after 'n' random steps.

	"""
	x,y=0,0
	for i in range(n):
		dx,dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
		x += dx
		y += dy
		print(str(x))

def main():
	random_walk(2)

if __name__ == '__main__':
	main()
# implementing monte-carlo solver for random walk https://www.youtube.com/watch?v=BfS2H1y6tzQ