sequence = ((1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31),
            (2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31),
            (4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31),
            (8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31),
            (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31))


def Guess_Number(answers):
    summ = 0
    if len(answers) != 5:
        return None
    for i in range(5):
        answ = answers[i]
        if type(answ) is int and 1 >= answ >= 0:
            if answ:
                summ += 2**i
            continue
        return None
    return summ


def Answers_Sequence(n):
    if type(n) is int and (0 < n < 32) and n is not None:
        return [1 if n in tup else 0 for tup in sequence]
    return None


for i in range(-10, 40):
    ans = Answers_Sequence(i)
    if ans is not None:
        numb = Guess_Number(ans)
        print(f"Number: {i}| Sequence: {ans} | Guessed: {numb}")
    else:
        print(f"Number: {i}| Sequence: {ans} | Guessed: None")
print(Answers_Sequence(None))
