month=int(input())
if month<1 or month>12:
    print("Invalid")
elif 3<=month<=5:
    print("Spring")
elif 6<=month<=8:
    print("Summer")
elif 9<=month<=11:
    print("Autumn")
else:
    print("Winter")
