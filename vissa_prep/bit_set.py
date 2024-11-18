def bit_set(n,k):
    mask=1<<(k-1)
    if n&mask:
        return "true"
    else:
        return "false"
n=int(input())
k=int(input())
print(bit_set(n,k))
