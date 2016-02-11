"""
A thief sets into a house to steal a set of things.
He finds n items i_0, i_1,...,i_n-1, each of weight
w_0, w_1,...,w_n-1 and whose values when he can sell them to be
v_0,v_1,...,v_n-1 respectively.

His only limitation is that he only has one knapsack, and it can hold a max weight of W.
All items are of integer non-zero weights. Values are obviously positive.
"""
import numpy as np

def knapsack_dp(valuables, max_wt):
    """

    :param valuables: dict of type key= weights, val= values in dollars
    :param max_wt: <int> max. wt. the knapsack can take
    :return: max. value he can get from stolen items
    """
    weights = sorted(valuables.keys())
    num_items = len(weights)
    knapsack = np.zeros((num_items + 1, max_wt + 1))
    knapsack[0, :] = 0     # no items in bag, therefore value of sack = 0
    knapsack[:, 0] = 0     # weight of sack is set to 0, therefore value of sack = 0
    for i in range(1, num_items + 1):
        for w in range(1, max_wt + 1):
            if weights[i-1] > w:
                knapsack[i, w] = knapsack[i-1, w]
                # choices[i, w] is zero
            else:
                knapsack[i, w] = max(knapsack[i-1, w],
                                     valuables[weights[i-1]] + knapsack[i-1, w - weights[i-1]])

    return knapsack[num_items, max_wt]




if __name__ == "__main__":
    valuables = {1: 4, 2: 3, 4: 8, 5: 9}
    #valuables = {23: 92, 31: 57, 29: 49, 44: 68, 53: 60, 38: 43, 63: 67, 85: 84, 89: 87, 82: 72}

    print(knapsack_dp(valuables=valuables, max_wt=10))
