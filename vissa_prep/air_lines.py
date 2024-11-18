import math
x,n=map(int, input().split())
def minimum_planes(x,n):
    cur_cap=x*100
    rem_pass=max(0,n-cur_cap)
    add_planes=math.ceil(rem_pass/100)
    return add_planes
print(minimum_planes(x,n))
