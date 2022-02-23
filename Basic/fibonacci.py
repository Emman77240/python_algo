# Function that receives an integer n and calculates fibonacci sequence of n

def fibonacci(n = 10, a = 0, b = 1):
    arr = []
    while n > 0:
        a, b = b, (a + b)
        arr.append(a)
        n -= 1

    print(arr)

fibonacci()