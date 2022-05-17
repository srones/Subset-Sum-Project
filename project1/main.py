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
    
    instance = []
    target = 0

    # 1-25 (INSTANCE I: RANDOM NUMBERS USED RAND FUNCTION AKA Mersenne Twister)
    if (num <= 25):
        instance = np.random.randint(1,10e3,num)
        target = (num/4) * 1000

        return instance, target

    # 25-50 (INSTANCE II: Linear Congruential Generator)
    if (num > 25 and num <= 50):
        while True:
            m = (a * m + c) % modulus #what should i set modulus?
    
    #50-75 (INSTANCE III: XOR SHIFT)
    if (num > 50 and num <= 75):
        return
    
    #75-100 (INSTANCE IV: Middle-Square Method)
    if (num > 75 and num <= 100):
        seed = 675248
        #global seed
        s = str(seed ** 2)
        while len(s) != 12:
            s = "0" + s
        seed = int(s[3:9])
        return seed

    return instance, target

def noSolutionInstance(n):

    target = 0
    instance = []

    for i in range(n):
        instance.append(1)

    return instance, target


############################################################
###################### Solve Instance ######################

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

    print(f'Solving for target = {target} with instance (n={len(instance)}) {instance}')

    start = time.perf_counter()

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

    metrics = []

    for i in range(100):
        instance, target = noSolutionInstance(i)
        time = solveInstance(instance, target)

        metrics.append([i, len(instance), time])


if __name__ == '__main__':
    main()
