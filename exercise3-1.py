fib = [0, 1]
# n = 20
n = int(input("Number of Fibonacci elements: "))
for i in range(2, n):
    fib.append(fib[i-2]+fib[i-1])
print(fib)