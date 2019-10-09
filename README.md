# Random Walk Problem Solver Using Monte Carlo


A monte carlo solution of a random walk problem. 

The problem consists of finding the highest number of steps *N* on a random walk that will on average be a manhattan distance of *M* or less from the origin point. 

Extended from <https://youtu.be/BfS2H1y6tzQ>

### functions

##### There are 3 main functions

* The solution: `<n_blocks_or_fewer>`
	* Helper function: `<random_walk>`
	* Helper function: `<build_dict_of_walks>`

The solution is self contained and runs by calling `<n_blocks_or_fewer>` in the `<main()>` function with passed parameters:

* (**5** blocks or less, up to **31** steps, **1000** iterations, **60%** or greater meeting the 5 blocks or less criteria)

```python
def main():
	n_blocks_or_fewer(5,31,1000,0.6)

def n_blocks_or_fewer(num_blocks = 4,max_walk_length = 31, iterations = 1000, percentage_succeed = 0.5):
```

