def Sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'Only positive integers are accepted'
    if n == 0:
        return 0
    else:
        return int(n % 10) + Sum_of_digits(int(n/10));

print(Sum_of_digits(-1));