def single_num(n, arr):
    count_map={}
    for num in arr:
        if num in count_map:
            count_map[num]+=1
        else:
            count_map[num]=1
    for num in count_map:
        if count_map[num]==1:
            return num
n=int(input())
arr=list(map(int, input().split()))
print(single_num(n,arr))
