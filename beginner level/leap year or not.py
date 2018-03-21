n=int(input("enter the year"))
if(n%4==0 and n%100!=0 or n%400==0):
  print("the year is leap year")
else:
  print("the year is not a leap year")
  
