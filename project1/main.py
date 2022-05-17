import random
import time
import numpy as np
from typing import Generator
a = 1664525
m = 232
c = 1013904223

class BNode:    
    def __init__(self, val: int, parent):
        self.val: int = val
        self.left: BNode = None
        self.right: BNode = None
        self.parent: BNode = parent

############################################################
#################### Generate Instance #####################
############################################################

def generateInstance(num): #send function number to pick instance type
    
    ret = []

    # 1-25 (INSTANCE I: RANDOM NUMBERS USED RAND FUNCTION AKA Mersenne Twister)
    if (num <= 25):        
        ref = np.random.randint(1,10e3,num)

    # 25-50 (INSTANCE II: Linear Congruential Generator)
    if (num > 25 and num <= 50):
        while True:
            m = (a * m + c) % modulus
    
    #50-75 (INSTANCE III: XOR SHIFT)
    if (num > 50 and num <= 75):
    
    
    #75-100 (INSTANCE IV: Middle-Square Method)
    if (num > 75 and num <= 100):
        seed = 675248
        global seed
        s = str(seed ** 2)
        while len(s) != 12:
            s = "0" + s
        seed = int(s[3:9])
        return seed

    return ret

############################################################
###################### Solve Instance ######################
############################################################

# Returns T or F
# Works for +, - and 0 values

def solveBinTreeRecursive(node: BNode, lst: list, target: int):

    # Solution
    if (node.val == target):

        # Edge case (target = 0, root node)
        if (not target == 0 and node.parent):
            printSolution(node)
            return True

    # Base case (leaf node)
    if (len(lst) == 0):
        return False
 
    # Keep checking if not leaf node
    if (len(lst) != 0):
        
        node.left = BNode(0, node)
        node.right = BNode(lst[0], node)

        if (solveBinTreeRecursive(node.left, lst[1:len(lst)], target - node.val)):
            return True
        if (solveBinTreeRecursive(node.right, lst[1:len(lst)], target - node.val)):
            return True

    # Remove node from memory
    if (node.parent):
        if (node.parent.left == node):
            node.parent.left = None
        else:
            node.parent.right = None

    return False

def solveInstance(instance, target):

    print(f'Solving for sum = {target} with instance {instance}')

    start = time.perf_counter()

    # Edge case
    if (len(instance) == 0):
        return False

    root = BNode(0, None)
    solution = solveBinTreeRecursive(root, instance, target)

    if (not solution):
        print("\tNo solution found")

    end = time.perf_counter()

    print(f'\tSolved in {end-start} seconds')

    print("-------------------------------------------------\n")
    
    return False

############################################################
########################## Helper ##########################
############################################################

def printLevelOrder(root):
     
    # Base case
    if root is None:
        return
    # Create an empty queue for level order traversal
    q = []
     
    # Enqueue root and initialize height
    q.append(root)
         
    while q:
     
        # nodeCount (queue size) indicates number
        # of nodes at current level.
        count = len(q)
         
        # Dequeue all nodes of current level and
        # Enqueue all nodes of next level
        while count > 0:
            temp = q.pop(0)
            print(temp.val, end = ' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
 
            count -= 1
        print(' ')

def printSolution(node: BNode):

    str = "\tSolution found: ["

    while (node):
        if (node.val != 0):
            str += f'{node.val}, '
        node = node.parent

    print(str + "]")

    return

############################################################
########################### Main ###########################
############################################################

def main():

    seed = 1234
    random.seed(seed)
    print()

    # for i in range(1):
    #     instance = generateInstance(i)

    #     print(f'instance: {instance}')

    #     solveInstance(instance)

    instance = [4, -1, 3, 2, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    for target in range(-2,16):
        solveInstance(instance, target)



if __name__ == '__main__':
    main()
