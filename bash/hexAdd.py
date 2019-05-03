PAYLOAD="66 06 46 0f"
KEY = "4"

each = PAYLOAD.split(" ")

out=[]
r=0
for i in each:
  h=hex(int(i,16)+int(KEY))
  out.append(h)
  out[r]=str(out[r]).replace("0x","")
  if(len(out[r])!=2):
     out[r]="0"+out[r]
  r+=1

print(out)
