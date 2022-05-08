n=int(input("Enter a no: "))
m=0
while n>0:
    d=n%10
    n=n//10
    m=m*10+d
print("The reverse is = ",m)
