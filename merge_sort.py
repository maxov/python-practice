import random

def recursive_combine_sorted(c1, c2):
    if len(c1) == 0:
        return c2
    elif len(c2) == 0:
        return c1
    else:
        if c1[0] < c2[0]:
            return c1[:1] + recursive_combine_sorted(c1[1:], c2)
        else:
            return c2[:1] + recursive_combine_sorted(c1, c2[1:])


def combine_sorted(c1, c2):
    len_c1, len_c2 = len(c1), len(c2)
    combined = []
    i = 0
    j = 0
    while i < len_c1 or j < len_c2:
        if j >= len_c2 or (i < len_c1 and c1[i] < c2[j]):
            combined.append(c1[i])
            i += 1
        else:
            combined.append(c2[j])
            j += 1
    return combined

def merge_sort(coll):
    if len(coll) <= 1:
        return coll
    else:
        midpoint = int(len(coll) / 2)
        sorted_1 = merge_sort(coll[:midpoint])
        sorted_2 = merge_sort(coll[midpoint:])
        return recursive_combine_sorted(sorted_1, sorted_2)

my_coll = list(range(0, 10))
shuffled = my_coll.copy()
random.shuffle(shuffled)

# note: random.shuffle is in-place
# from stackoverflow http://stackoverflow.com/questions/7931309/shuffle-in-python, many ways to copy:
# coll.copy()
# coll[:]
# list(coll)
# also sort: sorted(my_coll, key=lambda x: random.random())

assert merge_sort(shuffled) == my_coll