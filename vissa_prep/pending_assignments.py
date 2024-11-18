x,y,z=map(int, input().split())
time_required=x*y
time_available=z*24*60
if time_required<=time_available:
    print("YES")
else:
    print("NO")
