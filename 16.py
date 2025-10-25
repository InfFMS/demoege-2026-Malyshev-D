n =117
def f(n):
    return 2*(g(n-3)+8)
def g(n):
    if n < 10:
        return 2*n
    else:
        return g(n-2)+1
for i in range(10):
    print(f(i))