ch=str(input('enter a value'))
if((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):
  print("not valid")
else:
  b=float(ch)
  if((0<b)and(b<=100000)):
    print("positive")
  elif(b<0):
    print("negative")
  else:
    print("zero")
