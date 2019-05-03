a = open("payload","r")
red = a.read().replace("\n","")
a.close()
#print(red)
a=open("config","r")
key=a.readline(5).replace("\n","")
key=key.split(" ")[1]
s=""
for i in range(len(red)):
  if(red[i]==" "):
    s=s+" "
    #print(" ",end=" ")
  else:
    s=s+str((int(red[i])+k))
    #print(int(red[i])+k,end=" ")


print(s)
