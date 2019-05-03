a = open("t","r")
red = a.read().replace("\n","")
#print(red)
k = 3
s=""
for i in range(len(red)):
  if(red[i]==" "):
    s=s+" "
    #print(" ",end=" ")
  else:
    s=s+str((int(red[i])+k))
    #print(int(red[i])+k,end=" ")


print(s)
