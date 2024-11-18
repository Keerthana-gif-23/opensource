def compress_string(s):
    if not s:
        return ""
    res=[]
    cur_char=s[0]
    count=1
    for i in range(1, len(s)):
        if s[i]==cur_char:
            count+=1
        else:
            res.append(f"{cur_char}{count}")
            cur_char=s[i]
            count=1
    res.append(f"{cur_char}{count}")
    return "".join(res)
s=input().strip()
result=compress_string(s)
print(result)
