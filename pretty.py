import os

print "***VPN controller***"
print ""
priv = input("update priv for .sh files? [y/N]\n> ")
if(priv=="y" or priv=="yes" or priv=="Y"):
  os.system("chmod +x *.sh")
a=open("payloadI","w")
a.write("00 01")
a.close()
os.system("./Send.sh")

while True:
  print "0) configure the application"
  print "1) request a webpage"
  print "2) resend the last packet"
  print "3) post data to a site"
  print "99) exit"
  user = input("> ")
  s="'"

  if(user==0):
    #config change
    os.system("ifconfig")
    lhost=str(input("local ip?\n> "))
    lmac=str(input("local mac?\n> "))
    rhost=str(input("server ip?\n> "))
    yn=str(input("ping/arp server? [y/N]\n> "))
    if(yn=="y" or yn=="yes" or yn=="Y"):
      os.system("ping -c 1 "+rhost)
      os.system("arp -D "+rhost)
    rmac=str(input("server mac?\n> "))
    interface =str(input("interface to use?\n> "))
    a=open("config","w")
    a.write("lhost "+lhost+"\nlmac "+lmac+"\nrhost "+rhost+"\nrmac "+rmac+"\nint "+interface)
    a.close()
    print "config updated"

  elif(user==1):
    os.system("./Site.sh")

  elif(user==2):
    os.system("./Send.sh")
    os.system("./Listen.sh")

  elif(user==3):
    os.system("./Post.sh")
    os.system("./Listen.sh")

  elif(user==99):
    #stop server listen
    a=open("payloadI","w")
    a.write("00 00")
    a.close()
    os.system("./Send.sh")
    print("done")
    break

