import os
def dencode(lst):
  s=""
  for i in lst:
    s=s+str(chr(int(i,16)))
  return(s)

a=open("dencoded","r")
red = a.read().replace("\n","")
a.close()
lst = red.split(" ")

if(lst[0]=="02"):
  print(dencode(lst[1:]))
