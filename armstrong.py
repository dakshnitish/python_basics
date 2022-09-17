
n = input("enter the three digit number to know about that it is amstrong number or not : ")
ord = len(n)
sum = 0
for i in n:
    sum = sum + int(i)**len(n)
if sum == int(n):
    print(f"{n} is amstrong number")
else:
    print("it is not amstrong number") 