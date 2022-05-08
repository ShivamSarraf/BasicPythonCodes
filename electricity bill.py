n=int(input("Enter the units consumed: "))
price = 0.0
if(n<=50):
    price = n*3.0
elif(n>50 & n<=200):
    price = 150 + (n-50)*4.8
elif(n>200 & n<=400):
    price = 150 + 720 + (n-200)*5.8
else:
    price = 150 + 720 + 1160 + (n-400)*6.2
print(price)
