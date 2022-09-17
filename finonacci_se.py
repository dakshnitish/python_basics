
n = int(input("enter the number : "))
x = 0
y = 1
print("fibonacci series is : ")
for i in range(n):
    if i<=1:
        sum = i
    else:   
        sum = x+y
        x = y
        y = sum
    print(sum) 