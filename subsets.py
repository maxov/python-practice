# arbitrary element out of set: pop()
# or can do i = iter(set); next(i), frozenset(i)

# shorthand, need to use frozenset to be hashable
frz = frozenset


def subsets(s):
    if len(s) == 0:
        return {frz()}
    popped = s.copy()
    elem = popped.pop()
    subsets_rest = subsets(popped)
    # python sets use |, & for union, intersection
    return {subset for subset in subsets_rest} |\
           {subset | {elem} for subset in subsets_rest}

assert(subsets(frz())) == {frz()}
assert(subsets({1, 2})) == {frz(), frz({1, 2}), frz({2}), frz({1})}
assert(len(subsets(set(range(5))))) == 2 ** 5