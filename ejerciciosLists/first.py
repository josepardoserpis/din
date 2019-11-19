# Write a function called find_dups that takes a list of integers as its input argument and return
# a set of those integers occurring two or more times in the list


def find_dups(L):
    """
    >>> find_dups([1],[2],[3],[4])
    {1,2}
    >>> find_dups([],[],[],[])
    set()
    """

    elem_set = set()
    dups_set = set()

    for i in L:
        len_initial = len(elem_set)
        elem_set = set.add(i)
        len_end = len(elem_set)
        if len_initial == len_end:
            dups_set.add(i)

    return dups_set