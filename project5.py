from xmlrpc.client import Boolean
from project4 import readBenchmark
import numpy as np
import time

#####################################################################
######################## Initial Solutions ##########################
#####################################################################

def initial_solution1(instance: list[int], target: int):

    return

def initial_solution2(instance: list[int], target: int):

    return

#####################################################################
######################### Steepest Descent ##########################
#####################################################################

def steepest_descent(instance: list[int], target: int, init_sln: list[int]):

    return

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

    

    return

if __name__ == '__main__':
    mainDP()
    mainSteepest()
