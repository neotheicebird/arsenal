"""
You are given n types of coin denominations of values v(1) < v(2) < ... < v(n) (all integers).
Assume v(1) = 1, so you can always make change for any amount of money C.
Give an algorithm which makes change for an amount of money C with as few coins as possible.
"""
def give_change(denominations, change_required, change_given=None):
    """

    :param denominations:
    :param change_required:
    :param change_given:    Reserved for recursion, dont pass values when you call
    :return:
    """
    if change_given == None:
        if 1 not in denominations:
            raise(ValueError, "Min denomination should be 1")
        change_given = {(c, ()): () for c in range(change_required+1)}

    if len(denominations) == 1:
        change_given[(change_required, denominations)] = (1,)*(change_required)    # assuming denominations[0] == 1

    if len(denominations) == 0:
        change_given[(change_required, ())] = ()

    if change_required == 0:
        change_given[(0, denominations)] = ()

    if (change_required, denominations) in change_given.keys():
        return change_given[(change_required, denominations)]

    for c in range(1, change_required+1):
        for i, v in enumerate(denominations):
            if v > c:
                change_given[(c, denominations[:i+1])] = give_change(denominations[:i], c, change_given)
            else:
                M = (v,)*(c//v)
                change_given[(c, denominations[:i+1])] = M + give_change(denominations[:i], c-sum(M), change_given)

    # find the tuple in last row of the grid that has min number of elements in it. (Best solution = min num elements)
    L = [len(change_given[(change_required, denominations[:i])]) for i in range(1, len(denominations))]
    k = L.index(min(L))

    return change_given[(change_required, denominations[:k+1])]    # return the tuple from last row, that has min len


if __name__ == "__main__":
    V = (1, 3, 5, 10, 12, 15)       # change denominations available
    C = 9                           # change required

    change_given = give_change(V, C)
    print(change_given)