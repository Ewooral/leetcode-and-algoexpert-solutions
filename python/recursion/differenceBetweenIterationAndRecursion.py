# Recursion 
def powerOfTwo(n):
    if n == 0: 
        return 1; 
    else:  
        # print(powerOfTwo(n-1) * 2);
        return powerOfTwo(n-1) * 2;

print(powerOfTwo(4));



 
def factorial(n):
    assert n >= 0 and int(n) == n, 'Only positive integers are accepted';
    if n in [0, 1]:
        return 1;
    else: return n * factorial(n-1);   

print(factorial(4));   
print(factorial(0));
print(factorial(1));
# print(factorial(-10))

def fibonacci(n):
    # n should be greater than or equals to 0 and a positive integer
    assert n >= 0 and int(n) == n, 'Only positive integers are accepted'
    if n in [0, 1]:
        return n;
    else:
        return fibonacci(n-1) + fibonacci(n-2);

print(fibonacci(12));
print(fibonacci(0));
print(fibonacci(1));
