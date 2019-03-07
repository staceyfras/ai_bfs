## AI Homework 3 || BFS Implementation
## Stacey Frasier
## 03.11.19

def bfs(graph, start):
	opened = [start]
	closed = []
	while opened:
		closed.append(opened.pop())
		print("success")
	return False

def main():
	print("This program uses the example in L02 slide deck, page 27\n")
	start = input("Enter the node you wish to find from A-J: \n")
	start.upper()
	# if(node < 'A' || node > 'J'):
	# 	print("Fail\n")
	# keys represent nodes/parents, values represent children
	graph = {'A': set(['B', 'C', 'D']),
			 'B': set(['E', 'F']),
			 'C': set(['G', 'H']),
			 'D': set(['I', 'J']),
			 'E': set(),
			 'F': set(),
			 'G': set(),
			 'H': set(),
			 'I': set(),
			 'J': set()}
	bfs(graph, start)

if __name__ == "__main__":
	main()

