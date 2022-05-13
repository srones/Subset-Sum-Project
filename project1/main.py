from lib2to3.pytree import Node
import random

class BNode:    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

def createBinTreeRecursive(root, lst):

    if (len(lst) == 0):
        return

    root.left = BNode(0)
    root.right = BNode(lst[0])

    createBinTreeRecursive(root.left, lst[1:len(lst)])
    createBinTreeRecursive(root.right, lst[1:len(lst)])

    return root

def solveInstance(instance):

    n = len(instance)

    if (n == 0):
        return False

    root = createBinTreeRecursive(BNode(instance[0]), instance[1:n])

    
    
    return False

############################################################
########################## Helper ##########################
############################################################

def printTreeByRow(root):

    

    return


############################################################
########################### Main ###########################
############################################################

def main():

    seed = 1234
    random.seed(seed)

    for i in range(1):
        instance = generateInstance(i)

        print(f'instance: {instance}')

        solveInstance(instance)


if __name__ == '__main__':
    main()