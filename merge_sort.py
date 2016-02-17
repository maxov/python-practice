import random

def merge_sort(coll):
    if len(coll) <= 1:
        return coll
    else:
        midpoint = int(len(coll) / 2)
        sorted_1 = merge_sort(coll[:midpoint])
        sorted_2 = merge_sort(coll[midpoint:])
        i = 0
        j = 0
        len_s1 = len(sorted_1)
        len_s2 = len(sorted_2)
        coll_final = []
        while i < len_s1 and j < len_s2:
            if sorted_1[i] < sorted_2[j]:
                coll_final.append(sorted_1[i])
                i += 1
            else:
                coll_final.append(sorted_2[j])
                j += 1
        return coll_final

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