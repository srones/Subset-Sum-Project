# EECE_5360_Project

EECE 5360 Combinatorial Optimization Project\
Summer 1, 2022\
Stav Rones | Bryan Keller

## NP-Complete Problem: Subset Sum (SS)

**Optimal Solver**: Given a set $S$ of integers of length $n$ and a target integer $T$, decide if there exists a subset of $S$ whose sum is exactly $T$

### Solutions

**Exhaustive:** 

1. Inclusion-exclusion: $O(n*2^n)$ time $O(n)$ memory, 
    - s