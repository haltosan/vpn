a = open("payloadI","r")
red = a.read().replace("\n","")
a.close()
a=open("key","r")
k=a.read().replace("\n","")
a.close()
s=""
for i in range(len(red)):
  if(red[i]==" "):
    s=s+" "
  else:
    s=s+str(hex((int(red[i],16)+int(k,16))%16)).replace("0x","")
print(s)
