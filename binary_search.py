def binary_search(coll, val):
    def recurse(start, end):
        if start > end:
            return -1
        middle = int((start + end) / 2)
        compare = coll[middle]
        if compare > val:
            return recurse(start, middle - 1)
        elif compare < val:
            return recurse(middle + 1, end)
        else:
            return middle
    return recurse(0, len(coll) - 1)

my_coll = [1, 3, 6, 7]

assert binary_search(my_coll, 7) == 3
assert binary_search(my_coll, 1) == 0
assert binary_search(my_coll, 3) == 1
assert binary_search(my_coll, 5) == -1