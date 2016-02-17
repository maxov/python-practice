def binary_search(coll, val):
    def recurse(start, end):
        if start == end:
            return start
        else:
            middle = int((start + end) / 2)
            if coll[middle] > val:
                return recurse(start, middle)
            else:
                return recurse(middle, end)
    return recurse(0, len(coll) - 1)

my_coll = [1, 3, 6, 7, 8, 10]

binary_search(my_coll, 6)

# for some reason it goes infinitely, no idea why.