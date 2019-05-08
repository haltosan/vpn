a=open("payloadI","r")
red=a.read()
a.close()
lst=red.split(" ")
for i in range(len(lst)):
  if(len(lst[i])!=2):
    lst[i]="0"+str(lst[i])
s=""
for i in range(len(lst)):
  if(i!=len(lst)-1):
    s=s+str(lst[i])+" "
  else:
    s=s+str(lst[i])
a=open("payloadI","w")
a.write(s)
a.close()