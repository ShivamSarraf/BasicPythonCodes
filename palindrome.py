n=int(input("Enter a no: "))
m=0
i=n
while n>0:
    d=n%10
    n=n//10
    m=m*10+d
if(i==m):
    print("It is a Palindrome ")
else:
    print("It is not a palindrome ")
