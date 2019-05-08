site = str(input(""))
def encode(string):
  for i in range(len(string)):
    yield(str(hex(ord(string[i])))).replace("0x","")

e=list(encode(site))
s=""
for i in e:
  s=s+str(i)+" "
print("01 "+s)

