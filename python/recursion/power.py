def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 
    'Only positive integers are accepted as exponent';
    if exp == 0:
        return 1
    if exp == 1: 
        return base;
    return base * power(base, exp - 1);

print(power(3.2, 1)); 
print(power(-2, 4)); 

