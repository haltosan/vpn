import sys

site = sys.argv[1]
data = sys.argv[2]

def encode(string):
  for i in range(len(string)):
    if(not string[i]=="'" or not string[i]=='"'):
      yield(str(hex(ord(string[i])))).replace("0x","")

e=list(encode(site))
s=""
for i in e:
  s=s+str(i)+" "
ret=s+"ff "

e=list(encode(data))
s=""
for i in e:
  s=s+str(i)+" "
ret=ret+s

print("02 "+ret)
