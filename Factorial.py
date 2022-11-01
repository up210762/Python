def factorial(n):
    ft = 1
    for i in range(1, n+1):
        ft = ft*i
    return ft

r = factorial(4)
print(r)