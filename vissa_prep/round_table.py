def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
def number_of_ways(x):
    result = fact(x)
    return result
x=int(input())
print(number_of_ways(x))
