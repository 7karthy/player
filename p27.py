z=list(input("enter"))
print(z)
for i in range(len(z)):
  if z[i].islower():
    z[i]=z[i].upper()
  else:
    z[i]=z[i].lower()
print(z)
