a=(input('enter'))
a=a.split()
b=[]
for i in a:
  count=a.count(i)
  if count==1:
    print(i)
  else:
      continue
