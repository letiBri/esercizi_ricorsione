def factorial(n):
    if (n<=1):
        return 1
    else:
        counter = n-1
        return n * factorial(counter)


if __name__ == '__main__':
    print(factorial(4))