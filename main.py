import random
import statistics
import time
import numpy as np
from typing import Generator
import matplotlib.pyplot as plt
from datetime import datetime

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

    # 30 Worst case no solution
    if (num < 30):

        for i in range(num):
            instance.append(1)

        return instance, target

    # ----------------------------------------

    # 20 Average
    if (num >= 30 and num < 50):

        target = num - 29
        indexes = random.sample(range(20), num-29)

        for i in range(20):
            if (i in indexes):
                instance.append(1)
            else:    
                instance.append(0)

        return instance, target

    # ----------------------------------------

    # 15 Rand
    if (num >= 50 and num < 65):
        instance: np.ndarray = np.random.randint(1,10e3, num-35)
        target = (num/4) * 1000

        return instance.tolist(), target

    # ----------------------------------------

    # 15 Rand Middle-Square
    if (num >= 65 and num < 80):

        seed = 43512 #arbritrary number selected (must be even)
        
        for i in range(num-50):
            seed = int(str(seed * seed).zfill(8)[2:6])  # zfill adds padding of zeroes
            instance.append(seed)

        target = int(str(seed * seed).zfill(8)[2:6])

        return instance, target

    # ----------------------------------------
    
    # 10 Rand XOR SHIFT
    if (num >= 80 and num < 90):

        xorshift_seed = 23525 #arbritrary
        instance = []
        
        for i in range(num-60):
            xorshift_seed ^= xorshift_seed << 13
            xorshift_seed ^= xorshift_seed >> 17
            xorshift_seed ^= xorshift_seed << 5
            xorshift_seed %= int("ffffffff", 16) # The modulus limits it to a 32-bit number
            instance.append(xorshift_seed)
        
        xorshift_seed ^= xorshift_seed << 13
        xorshift_seed ^= xorshift_seed >> 17
        xorshift_seed ^= xorshift_seed << 5
        xorshift_seed %= int("ffffffff", 16)
        target = xorshift_seed
        
        return instance, target

    # ----------------------------------------
    
    # 10 rand Linear Congruential Generator

    a = 1664525
    modulus = 2**32
    c = 1013904223
    m = 19332
    if (num >= 90 and num < 100):

        for i in range(num-70):
            m = (a * m + c) % modulus
            instance.append(m)
        target = (a * m + c) % modulus 
        return instance, target

    return instance, target

def readBenchmark(i: int):

    f = open("benchmark.txt", "r")

    instance = []
    target = 0

    readingInstance = False

    for line in f:

        if "i" in line:

            if i == int(line.split()[1]):
                target = int(line.split()[3])
                readingInstance = True
                continue

        if readingInstance:
            for e in line.split(" "):
                if e != "\n":
                    instance.append(int(e))    
            f.close()
            return instance, target

    return instance, target

############################################################
###################### Solve Instance ######################

# Returns T or F
# Works for +, - and 0 values

MAX_TIME = 60

def solveBinTreeRecursive(node: BNode, lst: list, target: int, start):

    if (time.perf_counter() - start >= MAX_TIME):
        print("-- Timeout --")
        return False

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

        if (solveBinTreeRecursive(node.left, lst[1:len(lst)], target - node.val, start)):
            return True
        if (solveBinTreeRecursive(node.right, lst[1:len(lst)], target - node.val, start)):
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
    solution = solveBinTreeRecursive(root, instance, target, start)

    if (not solution):
        print("\tNo solution found")

    end = time.perf_counter()

    print(f'\tFinished in {end-start} seconds')

    print("-------------------------------------------------\n")
    
    return solution, end-start

def greedySolver(instance: list[int], target) -> tuple[int, float]:

    print(f'Greedy Solving for target = {target} with instance (n={len(instance)}) {instance}')

    start = time.perf_counter()

    # sort
    instance.sort(reverse=True)

    sum = 0
    for i in range(len(instance)):

        element = instance[i]

        if sum + element <= target:
            sum += element

    if sum + instance[-1] - target < target - sum:
        sum += instance[-1]

    end = time.perf_counter()

    # print(f'\tGreedy accuracy = {1 - abs(target - sum) / target}')
    print(f'\tFinished in {end-start} seconds')
    print("-------------------------------------------------\n")

    return sum, end-start

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

def printInstance(i, instance, target):
    
    print(f'Target: {target}, n = {len(instance)}\n {instance}')

    if (i in [29, 49, 64, 79, 89]):
        print(f'----------------------')

def plotResults(metrics):

    # print(f'metrics: {metrics}')

    time = [1.34, 2.4742, 4.805, 9.4447, 19.8442, 37.227, 69.9, 152.95, 281.38, 583.3, 1137.85]
    size = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

    # for row in metrics:
    #     size.append(row[1])
    #     time.append(row[2])

    plt.plot(size, time, 'g')

    # x = np.arange(0,len(metrics),1)
    # y = np.power(2, x)

    # plt.plot(x,y, 'r')

    plt.title('Worst Case')
    plt.xlabel('Set size')
    plt.ylabel('Time (sec)')

    plt.show()

    return

def saveResult(filename, i, instance, target, solution, time):

    f = open(filename, "a")
    f.write(f'i: {i}, Target: {target}, n: {len(instance)}, solution: {solution}, time: {time}, instance: \n{instance}\n')
    f.close()

def saveGreedyResult(filename, i, instance: list[int], target, solution, time):

    f = open(filename, "a")

    mean = sum(instance) / len(instance)
    var = np.array(instance).std()

    accuracy = "NaN"
    if not target == 0:
        accuracy = 1 - abs(target - solution) / target

    f.write(f'{i}, {len(instance)}, {target}, {mean}, {var}, {accuracy}, {solution}\n')

    f.close()


############################################################
########################### Main ###########################
############################################################

def mainGreedy():

    seed = 1234
    random.seed(seed)
    print()

    # filename = "greedy_" + datetime.now().strftime("%m.%d.%Y_%H:%M:%S.csv")
    filename = "greedy_sln"
    f = open(filename, "w")
    
    f.write(f'i, n, Target, Mean, Variance, Greedy Accuracy, solution\n')
    f.close()

    for i in range(1, 100):
        
        # instance, target = generateInstance(i)
        instance, target = readBenchmark(i)

        solution, time = greedySolver(instance, target)

        saveGreedyResult(filename, i, instance, target, solution, time)

    return

def main():

    seed = 1234
    random.seed(seed)
    print()

    filename = datetime.now().strftime("%m.%d.%Y_%H:%M:%S.txt")
    f = open(filename, "w")

    for i in range(1, 100):
        
        instance, target = generateInstance(i)
        # printInstance(i, instance, target)

        # solution, time = solveInstance(instance, target)
        print(f'i: {i}')

        solution, time = greedySolver(instance, target)

        # saveResult(filename, i, instance, target, solution, time)

if __name__ == '__main__':
    # main()
    mainGreedy()
