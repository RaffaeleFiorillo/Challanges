from itertools import permutations
import time


def next_bigger(n):
    num = list(str(n))
    index_to_swap = len(num) - 1
    for i in range(len(num) - 2, -1, -1):
        if num[i] < num[index_to_swap]:
            num[index_to_swap], num[i] = num[i], num[index_to_swap]
            return int("".join(num))
        else:
            index_to_swap = i
    else:
        return -1


def next_bigger2(n):
    n2=n
    len_str_n = len(str(n))
    sorted_n = sorted(str(n))
    while len_str_n == len(str(n2)):
        n2 += 1
        if sorted(str(n2)) == sorted_n:
            return n2
    return -1

def next_bigger3(n):
    str_n = str(n)
    len_n = len(str_n)
    for i in range(1, len_n+1):
        new_str = str_n[-i:]
        print("new sub string: ", new_str)
        len_new = len(new_str)
        poss = list((map(''.join, list(permutations(new_str, len_new)))))
        print("new possibilities: ", poss)
        for p in poss:
            val = int(str_n[:-i] + p)
            print("created Value: ", val)
            if val > n:
                return val
    return -1


def next_bigger4(n):
    list_n = [int(i) for i in (str(n))][::-1]
    min = list_n[0]
    max = list_n[0]
    for i in range(len(list_n)):
        if list_n[i] < min:
            list_n[i] = min
            break
    list_n[min], list_n[max]= list_n[max], list_n[min]
    return int("".join(list_n[::-1]))


t0 = time.time()
for i in range(20):
    print(next_bigger4(127898798675866232222222222))
t1 = time.time()
print(t1-t0)
