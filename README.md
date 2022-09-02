# Subset Sum Project
    EECE 5360 - Combinatorial Optimization
    Summer I, 2022
    Bryan Keller & Stav Rones

This project implements and evaluates the performance of different approaches to solving the famous [Subset Sum Problem](https://en.wikipedia.org/wiki/Subset_sum_problem).  The following methods were used to find optimal and [heuristic](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) solutions:

- Exhaustive search
- Greedy algorithm
- Integer Linear Programming (ILP)
- Dynamic Programming (DP)
- Local Search

The results of each algorithm are detailed in the PDF report.

## Subset Sum (SS) Problem

Subset Sum is a nondeterministic polynomial-time complete ([NP-C](https://en.wikipedia.org/wiki/NP-completeness)) [combinatorial optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization) problem, meaning that it is a finite set problem proven to be in the family of problems that are "unsolveable" in polynomial time. The definition is as follows:

> Given a set $S$ of integers of length $n$ and a target integer $T$, decide if there exists a subset of $S$ whose sum is exactly $T$

_NOTE:_ The exhaustive and DP approach only looked for optimal solutions while the greedy, ILP and LS algorithms returned the closest found solution. 

SS is a subproblem of the similarly NP-C [Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem#:~:text=The%20knapsack%20problem%20is%20a,is%20as%20large%20as%20possible.), and the parent problem of the polynomial time solvable problem [3SUM](https://en.wikipedia.org/wiki/3SUM), which asks if there exists a subset of length 3 whose sum is 0. 

## Benchmark

The following constraints were applied to create a testing benchmark of 100 SS instances:
- The largest instances must be at least 20 times larger than the smallest instance
- The structure of the instances themselves should vary
- Some instances should be randomly generated
- These instances should be representative of a large class of possible instances 

Based on these above requirements, the 100 instances were split into six types of instances of varying size and complexity:

1 - 30: Worst Case
> Instances of size n = 0, 1, 2, ... 29 where no solution exists. Achieved by array of all 1s with target = 0.

31 - 50: Average Case.
> Instances of size n = 20 where 1 solution exists whose size is inscreasing from 1 to 20 and whose positions are random.

51 - 65: Random 1
> Instances of size n = 15, 17, ... 29 with random elements in range [0,10e3] and a target of n * 1000 / 4

66 - 80: Random 2
> Instances of size n = 15, 17, ... 29 with random elements and target using the middle square method

81 - 90: Random 3
> Instances of size n = 20, 21, ... 29 with random elements and target using xor shift method

91 - 100: Random 4
> Instances of size n = 20, 21, ... 29 with random elements and target using the linear congruential generator method

# Algorithms

## Exhaustive Solution

The exhaustive algorithm checks all $2^n$ subsets to see if the subset sum equals the target, and returns true if a solution is found. Otherwise, it times out or returns false.

The [Inclusion-exclusion principle](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle) is used to iterate through every subset using a binary tree. This algorithm has time complexity $O(n*2^n)$ and memory complexity $O(n)$. The binary tree has height $n$ where every level represents one element in the set. Every node has a left child of 0 and a right child equal to the next element in the set. Depth First Search is used to traverse the tree where each stop in the traversal represents the sum of a subset.   

![](exhaustive_tree.png)

## Greedy Solution

[Greedy algorithms](https://en.wikipedia.org/wiki/Greedy_algorithm) are a problem solving heurestic that make the optimal choice at each stage. To implement this for SS, the set ordered using timesort and traversed until the sum is $>=$ the target. This has a time complexity of $O(n*log(n))$, and does not always find the optimal solution. 

## ILP Solution

Integer [Linear Programming](https://en.wikipedia.org/wiki/Linear_programming) is a technique used to minimize or maximize a linear function subject to constraints where the solution must be integer. This is achieved by using LP relaxation as a bound for the ILP solution. 

The ILP formulation of SS is as follows:

> $$ Maximize \sum^n_{i=1}w_ix_i \\
Where \sum^n_{i=1}w_ix_i <= T, w_i \in \mathbb{Z}$$

SS.mod contains the AMPL model for the CPLEX solver, which uses LP relaxation as a bound for the ILP solution. 

## Dynamic Programming Solution
[Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming) is an optimization technique that exploits the [optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure) of the SS problem to perform exhaustive search much faster than a naive implementation. This is done by keeping track of subsets that have already been computed using recursive top down [memoization](https://en.wikipedia.org/wiki/Memoization).


## Local Search Solution

[Local search](https://en.wikipedia.org/wiki/Local_search_(optimization)) is a heuristic that modifies an initial non-optimal candidate solution to make it more optimal. 
This local search algorithm uses a [1-Opt](https://en.wikipedia.org/wiki/2-opt) neighborhood - meaning that the local search checks every subset that either includes or excludes 1 element relative to the initial solution. If a more optimal solution is found, it is used as the initial solution for another round of local search, and this process is repeated until no better solution is found.
