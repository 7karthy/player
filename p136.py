a=int(input("enter"))
b=input("enter the check value")
c=[]
for i in range(a):
  d=input("enter the values")
  c.append(d)
if b in c:
  print("yes",c.count(b))
else:
  print("no")
