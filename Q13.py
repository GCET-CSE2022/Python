#h,b,p = map(int,input("Enter a,b and c separate by a space please :\t").split())
#test 5,3,4
h= int(input("Enter Hypithenuse\t"))
p= int(input("Enter Perpendicular\t"))
b= int(input("Enter Base\t"))

if h**2==(pow(b,2)+pow(p,2)):
  print("The Triangle is right angled")
else:
  print("Not right angled")
