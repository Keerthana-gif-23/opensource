bill=int(input())
dis_10_per=bill*0.10
dis_100=100
max_dis=max(dis_10_per,dis_100)
final=bill-max_dis
print(int(final))
