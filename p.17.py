from fractions import gcd
a=int(input("enter the first value"))
b=int(input("enter the first value"))
c=a*b/gcd(a,b)
print(int(c))
