def fact(n):
    if n ==  1 or n==0:
        return 1
    else:
        return n * fact(n-1)
def s(n):
    if n ==0:
        return 0
    else:
        return n + s(n-1)
n = int(input("Enter the limit"))
print(fact(n))
print(s(n))
        
