import os
def dencode(lst):
  s=""
  for i in lst:
    s=s+str(chr(int(i,16)))
  return(s)

def encode(string):
  def make(string):
    for i in range(len(string)):
      yield(str(hex(ord(string[i])))).replace("0x","")
  e = list(make(string))
  s=""
  for i in e:
    s=s+str(i)+" "
  return("02 "+s)

a=open("dencoded","r")
red=a.read().replace("\n","")
a.close()
a=open("config","r")
l=a.read().split("\n")
rhost=l[2].split(" ")[1]
interface =l[5].split(" ")[1]
a.close()
#print("red: ",red)
params=red.split(" ")[1]
#print("params: ",params)
if(red[:2]=="03"):
  #curl
  os.system("curl --interface "+interface+" "+rhost+":8000/"+params+" > gotFile")
  print("got the file",params)
  print("gotFile")
#sites=["google.com","duckduckgo.com"]
elif(red[:2]=="00"): #toggle loop
#  os.system("curl "+sites[int(params,16)]+" > gotSite")
#  print("gotSite",sites[int(params,16)])
  a=open("loop","w")
  a.write(params)
  a.close()
  if(params=="01"):
    os.system("./Listen.sh")
elif(red[:2]=="01"):
  r=red.split(" ")
  #print(dencode(r[1:]))
  os.system("curl "+dencode(r[1:])+" >gotSite")
  a=open("gotSite","r")
  red1=a.read()
  a.close()
  os.system("echo "+encode(red1)+" >payloadI")
  os.system("python sanitize.py")
  #print("encoded",encode(red1),red1)
  os.system("sleep 1")
  os.system("./Send.sh")

a=open("loop","r")
lState=a.read()
a.close()
if(lState=="01"):
  os.system("./Listen.sh")
