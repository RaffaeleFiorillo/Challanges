def around_fib(n):
    length = 2
    number = [0, 1]
    while length <= n:
        next_number = number[-2]+number[-1]
        number[0] = number[1]
        number[1] = next_number
        length += 1
    number = str(number[1])
    maxi = 0
    digit_max = 0
    for digit in range(10):
        current_count = number.count(str(digit))
        if current_count>maxi:
            maxi, digit_max = current_count, digit
    len_number = len(number)
    len_rest = len_number%25
    if len_rest:
        last_chunck = number[len_number - len_number % 25:]
    else:
        last_chunck = number[-25:]
    return "Last chunk {}; Max is {} for digit {}".format(last_chunck, maxi, digit_max)

print(around_fib(2509))

