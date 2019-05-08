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
  html=(dencode(lst[1:]))
  print("html got")
  a=open("mySite.html","w+")
  a.write("<!DOCTYPE html>\n"+html)
  a.close()
  os.system("firefox file:///root/werk/mySite.html")
