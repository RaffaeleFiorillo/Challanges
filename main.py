import time


def turn_normal(ones, map):
    new_m, new_map = [], []
    ind, min_ones = 0, min(ones)
    if len(map) == 1 and len(map[0]) > 1:
        return tuple([(1, 1)])
    for m in map:
        for value in m:
            if not value:
                new_m.append(0)
            else:
                for i in range(ones[ind]//min_ones):
                    new_m.append(1)
                break
        ind +=1
        new_map.append(tuple(new_m))
        new_m = []
    new_new_map = [new_map[0]]
    for i in range(1, len(new_map)):
        if new_map[i-1] == new_map[i]:
            continue
        else:
            new_new_map.append(new_map[i])
    new_map = tuple(new_new_map)
    if len(new_map) == 2:  # if a map has only 2 tuples, it means that the order doesn't matter so it is always the same
        new_map = tuple(sorted(new_map))
    return new_map


def map_poly(poly):
    lengths = [max(poly[p])+1 for p in poly]
    max_len = max(lengths)
    values = tuple([tuple([1 if i in poly[p] else 0 for i in range(max_len)]) for p in sorted(poly)])  # create a tuple map
    return values


def normalize(poly: dict):
    map = map_poly(poly)
    code = check_rect(map)
    if code == 1:
        return tuple([(1, 1,), ])
    elif code == 2:
        return tuple([(1,), ])
    ones = [sum([1 if v else 0 for v in value]) for value in map]  # count all the ones in a tuple
    normal = turn_normal(ones, map)
    return normal


def remove_excess(map):
    leasts = []
    index = 0
    for m in map:
        while sum(m[index:]) == sum(m):
            index += 1
        leasts.append(index-1)
        index = 0
    least = min(leasts)
    map = tuple(tuple(m[least:]) for m in map)
    return map


def check_rect(map):
    map = remove_excess(map)
    size_map = len(map)
    sizes = [len(m) for m in map]
    for m in map:
        if 0 in m:
            return 3
    if max(sizes) == min(sizes):  # check if it is rectangle
        for size in sizes:
            if size != size_map:  # check if it is not square
                return 1
        return 2
    return 3


def separated(dic: dict):
    keys = list(dic.keys())
    numbers_k = [x for x in range(keys[0], max(keys)+1)]
    for i, k in zip(numbers_k, keys):
        if k != i:
            return True
    dic_values = sorted([[v for v in value] for value in list(dic.values())])
    values = []
    for value in dic_values:
        for v in value:
            values.append(v)
    values = list(set(values))
    numbers_v = [x for x in range(values[0], values[-1]+1)]
    print(values)
    print(numbers_v)
    for i, v in zip(numbers_v, values):
        if v != i:
            return True
    return False


def symmetry(polyomino):
    if separated(polyomino):
        return "N"
    possibilities = {((1,), (1, 1)): "M",  ((0, 1), (1, 1, 1)): "M", ((0, 1), (1, 1), (0, 1)): "M",
                     ((1,), (1, 1), (1,)): "M", ((0, 1), (1, 1)): "M", ((1,), (1, 1)): "M",
                     ((1,), (1, 1), (0, 1)): "C2", ((0, 0, 1), (1,)): "C2",
                     ((0, 0, 1), (1, 1, 1), (0, 1, 1, 1), (0, 1)): "C4",
                     ((1, 1,), ): "D2", ((0, 1), (1,)): "D2", ((1,),): "D4",
                     ((0, 1), (1, 1, 1), (0, 1)): "D4"
                     }
    normal = remove_excess(normalize(polyomino))
    try:
        type_sym = possibilities[normal]
    except KeyError:
        type_sym = "N"
    return type_sym


t0 = time.time()
for i in range(10000):
    print(symmetry({0: {0, 1, 2}, 1: {1}}))
    print(symmetry({0: {0}, 1: {0, 1}}))
    print(symmetry({0: {0}, 1: {0, 1}, 2: {1},
                    3: {0, 1}, 4: {1}, 5: {0, 1}, 6: {1},
                    7: {0, 1}, 8: {1}, 9: {0, 1}, 10: {1},
                    11: {0, 1}, 12: {1}, 13: {0, 1}, 14: {1},
                    }))
    print(symmetry({0: {0}, 1: {0, 1}, 2: {1},
                    3: {0, 1}, 4: {1}, 5: {0, 1}, 6: {1},
                    7: {0, 1}, 8: {1}, 9: {0, 1}, 10: {1},
                    11: {0, 1}, 12: {1}, 13: {0, 1}, 14: {1},
                    }))
    print(symmetry({0: {0}, 1: {0, 1}, 2: {1},
                    3: {0, 1}, 4: {1}, 5: {0, 1}, 6: {1},
                    7: {0, 1}, 8: {1}, 9: {0, 1}, 10: {1},
                    11: {0, 1}, 12: {1}, 13: {0, 1}, 14: {1},
                    }))
    print(symmetry({0: {0}, 1: {0, 1}, 2: {1},
                    3: {0, 1}, 4: {1}, 5: {0, 1}, 6: {1},
                    7: {0, 1}, 8: {1}, 9: {0, 1}, 10: {1},
                    11: {0, 1}, 12: {1}, 13: {0, 1}, 14: {1},
                    }))
    print(symmetry({0: {0, 1, 2}, 1: {2, 3, 4}}))
    print(symmetry({0: {2}, 1: {0, 1, 2}, 2: {1, 2, 3}, 3: {1}}))
    print(symmetry({0: {0, 1, 2, 3}}))
    print(symmetry({0: {0, 1}, 1: {0, 1, 2}, 2: {1, 2}}))
    print(symmetry({0: {0, 1}, 1: {0, 1}}))
    print(symmetry({0: {1}, 1: {0, 1, 2}, 2: {1}}))
t1 = time.time()
print("\n\ntime of execution: ", t1-t0)
