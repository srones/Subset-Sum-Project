import random
import time

class BNode:    
    def __init__(self, val: int, parent):
        self.val: int = val
        self.left: BNode = None
        self.right: BNode = None
        self.parent: BNode = parent

############################################################
#################### Generate Instance #####################
############################################################

def generateInstance(num):
    
    ret = []

    # 5 / 100 
    #################### Hand generated, easy to solve, length 10 #####################
    if (num < 5):        

        if (num == 0):
            ret = [0,0,0,0,0,0,0,0,0,0]

        if (num == 1):
            ret = [1,1,1,1,1,1,1,1,1,1]

        if (num == 2):
            ret = [0,1,2,3,4,5,6,7,8,9,10]

        if (num == 3):
            ret = [0,1,2,3,4,5,6,7,8,9,10]

        if (num == 4):
            ret = [0,1,2,3,4,5,6,7,8,9,10]

        if (num == 5):
            ret = [0,1,2,3,4,5,6,7,8,9,10]

    # 20 / 100
    #################### Random generated, length 100, range [0,1e6] #####################
    if (num >= 5 and num < 20):

        for i in range(100):
            ret.append(random.randint(0,1e6))

    # ? / 100
    ######################################## ??? #########################################

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