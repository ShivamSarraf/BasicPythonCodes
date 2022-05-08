n=int(input("Enter a no: "))
d=n
i=j=k=0
while d>0:
    d=d//10
    i=i+1
j=n%10;
k=n//(10**(i-1))
print("The sum = ",j+k)
