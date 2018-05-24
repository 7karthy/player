a=int(input("enter range:"))
b=int(input("enter a check:"))
c=[]
for i in range(a):
  d=int(input("enter your number"))
  c.append(d)
e=sum(c)
if e==b:
  print("yes")
else:
  print("no")
