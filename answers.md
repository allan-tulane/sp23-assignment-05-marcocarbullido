# CMPS 2200 Assignment 5
## Answers

**Name:**Marco Carbullido


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**
- Algorithm (Greedy)
- 1. Initialize minCoins to 0
- 2. Initialize power to the largest integer k such that 2^k <= N
- 3. While N > 0:
     a. Add N // (2^power) to minCoins
     b. Update N to N % (2^power)
     c. Decrement power by 1
- 4. Return minCoins



- **1b.**
- Because each step decreases n by a power of 2, and there is no parallelization, the work and span are logarithmic and we get O(log(n)), 



- **2a.**
- In Fortuito, suppose the available denominations are {1, 4, 6} and you want to make change for N = 8 dollars. The greedy algorithm would choose 6, then 1, and then 1, using 3 coins. However, the optimal solution is to use two 4-dollar coins, totaling only 2 coins.
- This occurs because of our greedy criteria, which neglect thorough exploration of the solution space for optimal solution.




- *2b.**
- Let `min_coins(N, denominations, memo)` be a function which computes the min number of coins needed for `N` dollars given a set of denominations named `denominations` and a memoization dictionary named `memo`.
- If `N` is in memo, return the value.
- If `N < 0`, return infinity (no change for negative values).
- If `N = 0`, return 0 (no coins needed).
- For each denomination `d` in `denominations`, recursively call `min_coins(N - d, denominations, memo)`, and store the minimum of these results in the memo.
- Eventually, return the minimum number of coins found.

- The Work is O(N * k). This is because in the worst case we have to try all k combinations for each amount from 1 to N for each denomination in the set.
- The Span is O(N) because the maximum depth of recursion corresponds to the longest chain of recursive calls when subtracting the smallest denomination from the number N, resulting in N recursive calls.

