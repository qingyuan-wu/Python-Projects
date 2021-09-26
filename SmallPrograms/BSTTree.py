# Binary Search Trees
# Investigating the relationship between number of nodes and tree height

# Lab 6
# We'll define a node of a binary tree and introduce some features of Python
# classes along the way

import random

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''
        node.insert(5) is the same as BST.insert(node, 5)
        We use this when recursively calling, e.g. self.left.insert
        '''
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def __repr__(self):
        '''The string representation of a node.
        Here, we convert the value of the node to a string and make that
        the representation.
        We can now use
        a = Node(4)
        print(a) # prints 4
        '''
        return str(self.value)

a = BST(4)
a.insert(2)
a.insert(5)
a.insert(10)
a.insert(3)
a.insert(15)

b = BST(5)
b.insert(2)
b.insert(10)
b.insert(1)
b.insert(3)
b.insert(7)
b.insert(14)

# Problem 1
# Draw (manually) the binary tree rooted in a.
'''
        4
     /      \
    2        5
      \        \
        3       10
                  \
                   15
'''



# Problem 2
# Write code to find the height of a Binary Search Tree
def find_height(bst):
    cur_height = 0
    max_height = 0
    s = [[bst, 0]]
    explored = []

    cur = bst
    count = 0
    while len(s) > 0 and count < 20:
        
        if cur.left != None and cur.right != None: #and cur not in explored:
            s.append([bst, cur_height])
            cur = cur.left
            cur_height += 1
        elif cur.left != None: #and cur not in explored:
            cur_height += 1
            cur = cur.left
        elif cur.right != None:
            cur_height += 1
            cur = cur.right
        else:
            if cur_height > max_height:
                max_height = cur_height
            temp = (s.pop(-1))
            cur = temp[0]
            cur_height = temp[1]

        explored.append(cur)
        count += 1

    return max_height

def find_height_rec(bst):
    if bst.left == None and bst.right == None:
        return 0
    elif bst.left == None:
        return 1+find_height_rec(bst.right)
    elif bst.right == None:
        return 1+find_height_rec(bst.left)

    return max(1+find_height_rec(bst.left), 1+find_height_rec(bst.right))

print(find_height(a))
print(find_height_rec(a))
print(find_height_rec(b))

# Problem 3

# Write code to print out the nodes of the BST using
# Breadth-First Search. How would you get the Breadth-First Traversal
# from the tree you've drawn?
# (Modify the BFS function from lecture for this problem)

def BFS_tree(node):
    # NOTE: commented out the explored list and checks because not necessary
        # think about why it's not necessary ...
    q = [node]

    count = 0
    cur = node

    while len(q) > 0:
        cur = q.pop(0)
        print(cur)
        if cur.left != None and cur.right != None:
            q.extend([cur.left, cur.right])

        elif cur.left != None:
            q.append(cur.left)
            cur = cur.left

        elif cur.right != None:
            q.append(cur.right)
            cur = cur.right

#don't need explored list
BFS_tree(a)
print("\n")
BFS_tree(b)

# Problem 4

# Empirically investigate the relationship between the number of nodes in the
# tree and the height of the tree when inserting nodes with values generated
# using random.random()

def make_random_tree(n_nodes):
    '''Make a tree with n_nodes nodes by inserting nodes with values
    drawn using random.random()
    '''
    a = BST(random.random())
    for i in range(n_nodes-1):
        a.insert(random.random())
    return a

def height_random_tree(n_nodes):
    '''Generate a random tree with n_nodes nodes, and return its height'''
    a = make_random_tree(n_nodes)
    return find_height_rec(a)

def make_data(max_nodes):
    '''Make two lists representing the empirical relationship between
    the number of nodes in a random tree and the height of the tree.
    Generate N_TREES = 40 trees with each of
    n_nodes = 5, int(1.2*5), int(1.2^2*5), .....

    return n (a list of values of n_nodes) and h (a list of heights)

    '''
    N_TREES = 40
    n_nodes = [5]
    heights = [0]

    while n_nodes[-1]*1.2 <= max_nodes:
        n_nodes.append(int(n_nodes[-1]*1.2))
        heights.append(0)


    for k in range(len(n_nodes)):
        cur_heights = 0
        for i in range(N_TREES):
            cur_heights += height_random_tree(n_nodes[k])

        heights[k] = cur_heights / N_TREES

    return n_nodes, heights


n, h = make_data(100000)
import matplotlib.pyplot as plt
plt.scatter(n, h)
plt.show()
plt.savefig("trees.png")  # save the data