import random

# random in range: random.randrange(n)


def swap(coll, a, b):
    coll[a], coll[b] = coll[b], coll[a]


def quick_sort(coll):
    if len(coll) <= 1:
        return coll
    else:
        pivot_i = random.randrange(len(coll))
        pivot = coll[pivot_i]
        i = 0
        new_coll = coll.copy()
        swap(new_coll, pivot_i, len(new_coll) - 1)
        for j in range(len(new_coll) - 2):
            if new_coll[j] <= pivot:
                swap(new_coll, i, j)
                i += 1
        swap(new_coll, i, len(new_coll) - 1)
        return quick_sort(new_coll[:i - 1]) + [pivot] + quick_sort(new_coll[i + 1:])

my_coll = list(range(0, 10))
shuffled = my_coll.copy()
random.shuffle(shuffled)

print(quick_sort(shuffled))

assert quick_sort(shuffled) == my_coll