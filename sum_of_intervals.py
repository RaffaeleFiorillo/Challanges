def is_overlapping(inter1, inter2):
    if inter1[-1] >= inter2[0]:
        return True


def sum_of_intervals(intervals):
    intervals = sorted(list(set(intervals)))
    index_0 = 0
    index_1 = 1
    while index_1 < len(intervals):
        if is_overlapping(intervals[index_0], intervals[index_1]):
            if intervals[index_0][-1] <= intervals[index_1][-1]:
                intervals = intervals[:index_0]+[(intervals[index_0][0], intervals[index_1][-1])] + intervals[index_1+1:]
            else:
                intervals = intervals[:index_0]+[(intervals[index_0][0], intervals[index_0][-1])] + intervals[index_1 + 1:]
        else:
            index_1 += 1
            index_0 += 1
        print(len(intervals))
        print(intervals)
    return sum([i[1]-i[0] if i[1]-i[0] > 0 else (i[1]-i[0])*(-1) for i in intervals])
