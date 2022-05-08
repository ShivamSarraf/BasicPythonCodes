a=float(input("Enter the co-eff of x square: "))
b=float(input("Enter the co-eff of x : "))
c=float(input("Enter the value of constant: "))
d = ((b*b)-(4*a*c))
e=d**0.5
if d>0:
    root1 = ((-b + e)/(2*a))
    root2 = ((-b - e)/(2*a))
    print("The first root is = ",root1,"\nThe second root is = ",root2)
elif d==0:
    root1 = -b/(2*a)
    print("Both the roots are same that is = ",root1)
else:
    print("Roots are imaginary")
