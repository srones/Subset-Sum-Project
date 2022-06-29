from importlib.resources import read_binary
from xmlrpc.client import Boolean
from project4 import readBenchmark
import numpy as np
import time
import random
from main import greedySolver

#####################################################################
######################## Helper Functions ###########################
#####################################################################

def soln2sum(instance: list[int], solution: list[int]):

    sum = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            sum += instance[i]

    return sum

#####################################################################
######################## Initial Solutions ##########################
#####################################################################

# greedy
def initial_solution1(instance: list[int], target: int):

    solution = [0 for i in range(len(instance))]

    if len(instance) == 0:
        return [], 0

    # sort
    instance.sort(reverse=True)

    sum = 0
    for i in range(len(instance)):

        element = instance[i]

        if sum + element <= target:
            solution[i] = 1
            sum += element

    return solution, sum

# random
def initial_solution2(instance: list[int], target: int):

    solution = [random.randint(0,1) for b in range(len(instance))]

    sum = soln2sum(instance, solution)

    return solution, sum

#####################################################################
######################### Steepest Descent ##########################
#####################################################################

def bestNeighbor_swap(instance: list[int], target: int, init_sln: list[int]):

    bestSolution = init_sln

    bestSolution_value = 0
    for i in range(len(bestSolution)):
        if bestSolution[i] == 1:
            bestSolution_value += instance[i]
    
    # swap
    for i in range(len(init_sln)):
        if init_sln[i] == 1:
            for j in range(len(init_sln)):
                if init_sln[j] == 0:

                    new_solution = init_sln

                    new_solution[i] = 0
                    new_solution[j] = 1

                    newValue = 0
                    for i in range(len(new_solution)):
                        if new_solution[i] == 1:
                            newValue += instance[i]

                    if abs(newValue - target) < abs(bestSolution_value - target):
                        bestSolution = new_solution
                        bestSolution_value = newValue

    return bestSolution, bestSolution_value

def bestNeighbor_1opt(instance: list[int], target: int, init_sln: list[int]):

    bestSolution = init_sln
    bestSum = soln2sum(instance, init_sln)
    
    # add or remove each element
    for i in range(len(init_sln)):

        new_solution = init_sln.copy()

        if new_solution[i] == 1:
            new_solution[i] = 0
        else:
            new_solution[i] = 1

        newSum = soln2sum(instance, new_solution)

        if abs(newSum - target) < abs(bestSum - target):
            bestSolution = new_solution.copy()
            bestSum = newSum                    

    return bestSolution, bestSum

def steepestDescent(instance: list[int], target: int, init_sln: list[int]):

    # get initial sum
    bestSolution = init_sln
    bestSum = soln2sum(instance, init_sln)

    tabu = []
    
    iterations = 0
    while (True):

        newSln, newSum = bestNeighbor_1opt(instance, target, bestSolution)
        iterations += 1

        print(f'{bestSum} {newSum}')
        
        if (newSln in tabu):
            break
            
        if (newSum != bestSum):
            tabu.append(newSln)
            bestSum = newSum
            bestSolution = newSln
        else:
            break
            
    print(f'iterations: {iterations}')
    return bestSolution, bestSum, iterations

#####################################################################
######################## Dynamic Programming ########################
#####################################################################

memo = {}

def dynamic_programming(instance: list[int], target: int):

    global memo

    if target == 0:
        return True

    if len(instance) == 0 or target < 0:
        return False

    key = (len(instance), target)

    if key not in memo:

        include = dynamic_programming(instance[0:-1], target - instance[-1])

        exclude = dynamic_programming(instance[0:-1], target)
 
        memo[key] = include or exclude

    return memo[key]

def mainDP():

    f = open("DP.txt", "w")
    f.write(f'i, s_dp, t_dp\n')

    for i in range(100):

        instance, target = readBenchmark(i)

        global memo 
        memo = {}

        start = time.perf_counter()

        solution = dynamic_programming(instance, target)

        end = time.perf_counter()

        f.write(f'{i}, {solution}, {end-start}\n')

    return

def mainSteepest():

    f = open("LS_greedy_1opt.txt", "w")
    f.write("i, s_local, t_local, iterations\n")

    for i in range(100):

        instance, target = readBenchmark(i)

        # get initial solution
        init_sln, sum = initial_solution1(instance, target)    

        start = time.perf_counter()

        # run steepest descent
    
        solution, value, iterations = steepestDescent(instance, target, init_sln)

        end = time.perf_counter()

        print(f'{i} {target} {end-start}')
        print(f'init_sln_value = {sum}')
        print(f'new_sln_value = {value}\n')

        f.write(f'{i}, {value}, {end-start}, {iterations}\n')

    return

if __name__ == '__main__':
    # mainDP()
    mainSteepest()
