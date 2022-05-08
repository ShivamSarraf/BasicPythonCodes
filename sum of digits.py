n=int(input("Enter a no: "))
i=j=sum=0
while n>0:
    j=n%10
    n=n//10
    i=i+1
    sum=sum+j
print("The sum of digits = ",sum)
