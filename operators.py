# x=3>2
# print(x)


w=int(input("enter your weight: "))
unit=input("(K)g or(L)bs :")

if unit.lower()=="k":
    print(str(w//0.45))
elif unit.lower()=="l":
    print(str(w*0.45))