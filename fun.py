def sum( a, b):
    return a + b

def avg( a, b):
    return (a+b)/2

def factorial(n):
    n = input("enter a number")
    copy_n = n
    n = int(n)
    f = 1
    while(n!=1):
        n = int(n)
        f = n * f
        n = n - 1
    print("factorial of", copy_n,"is",f)
    return False

def amstrong(n):
    n = input("enter a number")
    n = int(n)
    s = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        n = n/10
        sum += digit **order
        n = n//10
    if (sum == copy_n):
        print(f"{copy_n} is an amstrong number")
    else:
        print(f"{copy_n} is not an amstrong number")
    return False







