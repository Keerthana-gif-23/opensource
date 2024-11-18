def calculate_scores(test_cases):
    res=[]
    for x, n in test_cases:
        score=(x//10)*n
        res.append(score)
    return res
T=int(input())
test_cases=[tuple(map(int, input().split())) for _ in range(T)]
scores=calculate_scores(test_cases)
for score in scores:
    print(score)
