def binary_search(coll, val):
    def recurse(start, end):
        middle = int((start + end) / 2)
        compare = coll[middle]
        if compare > val:
            return recurse(start, middle)
        elif compare < val:
            return recurse(middle, end)
        else:
            return middle
    return recurse(0, len(coll) - 1)

my_coll = [1, 3, 6, 7, 8, 10]

print(binary_search(my_coll, 6))
