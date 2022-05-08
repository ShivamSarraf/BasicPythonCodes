n=int(input("Enter a no: "))
i=j=0
prod=1
while n>0:
    j=n%10
    n=n//10
    i=i+1
    prod=prod*j
print("The product of digits = ",prod)
