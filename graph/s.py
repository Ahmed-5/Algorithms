# Python3 implementation of the above approach

# To create tree
tree = {}
path = []
maxHeight, maxHeightNode = -1, -1

# Function to store the path
# from given vertex to the target
# vertex in a vector path
def getDiameterPath(vertex, targetVertex, parent, path):

	# If the target node is found,
	# push it into path vector
	if (vertex == targetVertex):
		path.append(vertex)
		return True

	for i in range(len(tree[vertex])):
		# To prevent visiting a
		# node already visited
		if (tree[vertex][i] == parent):
			continue

		# Recursive call to the neighbours
		# of current node inorder
		# to get the path
		if (getDiameterPath(tree[vertex][i], targetVertex, vertex, path)):
			path.append(vertex)
			return True
	return False

# Function to obtain and return the
# farthest node from a given vertex
def farthestNode(vertex, parent, height):
	global maxHeight, maxHeightNode
	# If the current height is maximum
	# so far, then save the current node
	if (height > maxHeight):
		maxHeight = height
		maxHeightNode = vertex

	# Iterate over all the neighbours
	# of current node
	if (vertex in tree):
		for i in range(len(tree[vertex])):
		
			# This is to prevent visiting
			# a already visited node
			if (tree[vertex][i] == parent):
				continue
				
			# Next call will be at 1 height
			# higher than our current height
			farthestNode(tree[vertex][i], vertex, height + 1)

# Function to add edges
def addedge(a, b):
	if (a not in tree):
		tree[a] = []

	tree[a].append(b)

	if (b not in tree):
		tree[b] = []

	tree[b].append(a)

def FindCenter(n):
	# Now we will find the 1st farthest
	# node from 0(any arbitary node)

	# Perform DFS from 0 and update
	# the maxHeightNode to obtain
	# the farthest node from 0

	# Reset to -1
	maxHeight = -1

	# Reset to -1
	maxHeightNode = -1

	farthestNode(0, -1, 0)

	# Stores one end of the diameter
	leaf1 = maxHeightNode

	# Similarly the other end of
	# the diameter

	# Reset the maxHeight
	maxHeight = -1
	farthestNode(maxHeightNode, -1, 0)

	# Stores the second end
	# of the diameter
	leaf2 = maxHeightNode

	# Store the diameter into
	# the vector path
	path = []

	# Diameter is equal to the
	# path between the two farthest
	# nodes leaf1 and leaf2
	getDiameterPath(leaf1, leaf2, -1, path)

	pathSize = len(path)

	if (pathSize % 2 == 1):
		print(path[int(pathSize / 2)]*-1)
	else:
		print(path[int(pathSize / 2)], ", ", path[int((pathSize - 1) / 2)], sep = "", end = "")

N = 8

tree = {}

addedge(0, 1)
addedge(1, 2)
addedge(2, 3)
addedge(3, 4)
addedge(1, 5)
addedge(2, 6)
addedge(3, 7)

FindCenter(N)

# This code is contributed by suresh07.
