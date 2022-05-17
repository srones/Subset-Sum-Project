# EECE_5360_Project

EECE 5360 Combinatorial Optimization Project\
Summer 1, 2022\
Stav Rones | Bryan Keller

## NP-Complete Problem: Subset Sum (SS)

**Optimal Solver**: Given a set $S$ of integers of length $n$ and a target integer $T$, decide if there exists a subset of $S$ whose sum is exactly $T$

### Exhaustive Solution:** 

1. Inclusion-exclusion: $O(n*2^n)$ time $O(n)$ memory, 
    - Uses a binary tree where each level corresponds to a list element. The left child of every node is 0, and the right child of every node is the next value in the list.
    - Works for +, -, and 0 targets and list elements
    - Returns True as soon as set is found, False if there does not exist a set

### Benchmark ###

1 - 30: Instances of size n = 0, 1, 2, ... 29 where no solution exists. Achieved by array of all 1s with target = 0.