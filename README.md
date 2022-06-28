# EECE_5360_Project

EECE 5360 Combinatorial Optimization Project\
Summer 1, 2022\
Stav Rones | Bryan Keller

## NP-Complete Problem: Subset Sum (SS)

**Optimal Solver**: Given a set $S$ of integers of length $n$ and a target integer $T$, decide if there exists a subset of $S$ whose sum is exactly $T$

### Benchmark ###

1 - 30: Instances of size n = 0, 1, 2, ... 29 where no solution exists. Achieved by array of all 1s with target = 0.

31 - 50: Instances of size n = 20 where 1 solution exists whose size is inscreasing from 1 to 20 and whose positions are random.

51 - 65: Instances of size n = 15, 17, ... 29 with random elements in range [0,10e3] and a target of n * 1000 / 4

66 - 80: Instances of size n = 15, 17, ... 29 with random elements and target using the middle square method

81 - 90: Instances of size n = 20, 21, ... 29 with random elements and target using xor shift method

91 - 100: Instances of size n = 20, 21, ... 29 with random elements and target using the linear congruential generator method


TODO: 
    - Include negative numbers and targets
    - Include non-integer numbers



### Exhaustive Solution:** 

1. Inclusion-exclusion: $O(n*2^n)$ time $O(n)$ memory, 
    - Uses a binary tree where each level corresponds to a list element. The left child of every node is 0, and the right child of every node is the next value in the list.
    - Works for +, -, and 0 targets and list elements
    - Returns True as soon as set is found, False if there does not exist a set

### Greedy Solution:** 

### ILP Solution:** 

ILP formulation of SS:

    Given a set of integers X = {x_1, x_2, ... x_n}, binary variables Y = {y_1, y_1, ... y_n}, and a target T,
    
    Maximize: 

        (x_1)(y_1) + (x_2)(y_2) + ... + (x_n)(y_n)

    Constraints:

        (x_1)(y_1) + (x_2)(y_2) + ... + (x_n)(y_n) <= T
        y_i = binary

[] What is a bound for the LP formulation?
[] Convert instances to ILP formulation
[] Solve all ILP with time limits

ILP -> LP Relaxation -> Lower Bound 

**AMPL / CPLEX**
- 