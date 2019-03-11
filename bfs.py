## AI Homework 3
## Stacey Frasier
## 03.11.19
## Language: Python v3.7.1

## This program generates a trace of a BFS implementation. This implementation uses
## two queues to represent opened and closed nodes, and a dictionary to represent
## the graph.
from collections import deque

def bfs(graph, goal):
    opened, closed = deque(['A']), deque([])
    print("initial opened: ", opened)
    print("initial closed: ", closed)
    while opened:
        x = opened.popleft() # remove leftmost state from opened
        if x == goal: # if x is goal, SUCCESS
        	return True
        else:
        	children = graph[x] # generate children of x
        	closed.appendleft(x) # put x on closed
        	if children: # remove children of x from if already on opened or closed
	        	for child in children:
		        	if child in opened or child in closed:
		        		children.remove(child)
	        opened.extend(children) # put remaining children on right end of open
        print("opened: ", opened)
        print("closed: ", closed)
        print("\n")
    return False
	
def main():
	# graph is taken from slide 22 for completeness.
	graph = {'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'], 'D': ['I', 'J'],
			 'E': ['K', 'L'], 'F': ['L', 'M'], 'G': ['N'], 'H': ['O', 'P'], 'I': ['P', 'Q'],
			 'J': ['R'], 'K': ['S'], 'L': ['T'], 'M': [], 'N': [], 'O': [], 'P': ['U'], 
			 'Q': [], 'R': [], 'S': [], 'T': [], 'U': []}
	print("BFS implementation in Python:")
	goal = input("Enter the node you wish to find from A-J: ")
	goal = goal.upper()
	found = bfs(graph, goal)
	if found:
		print("Result: Success. Node '", goal, "' was found! :D")
	else:
		print("Result: Fail. Node '", goal, "' was not found :(")

	
if __name__ == "__main__":
	main()

