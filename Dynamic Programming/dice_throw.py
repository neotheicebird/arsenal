"""
Given n dice each with m faces, numbered from 1 to m,
find the number of  ways to get sum X. X is the summation of face values of all the dice when thrown.
"""
import numpy as np

def dice_sum(m, n, X, num_ways=None):
    """

    :param m:   number of faces in each dice
    :param n:   number of dices
    :param X:   sum of face values of the dices thrown
    :param num_ways:    a 2D array to cache results
    :return:    number of ways to get the sum X with n dices each of m faces
    """
    if not num_ways:
        num_ways = dict()
        num_ways[(1, 1)] = 1
    if X <= 0:  # X cant be non-positive, no ways to reach there
        return 0
    if n == 1 and X <= m:   # subproblems that are presolved, trivial cases
        return 1

    # these two conditions add to performance (otherwise not needed)
    if X >= m*n:            # if X is so large that the only solution is (1,1,1,1,.....mtimes) or no solution
        return X == m*n
    if n >= X:              # if n is > X then no solution is possible, otherwise there is one sol. (1,1,1...n times)
        return n == X

    if (n, X) in num_ways:
        return num_ways[(n, X)]
    else:
        num_ways[(n, X)] = sum(dice_sum(m, n-1, X-i, num_ways=num_ways) for i in range(1, m+1))
        return num_ways[(n, X)]


if __name__ == "__main__":
    m = 4       # number of faces of each dice
    n = 3       # number of dices
    X = 5       # sum of face values needed
    print(dice_sum(m, n, X))