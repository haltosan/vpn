import os
print("starting")

a=open("payload","r")
payload=a.read().replace("\n","")
a.close()

a=open("config","r")

lhost=a.readline().replace("\n","")
lhost=lhost.split(" ")[1]

lmac=a.readline().replace("\n","")
lmac=lmac.split(" ")[1]

rhost=a.readline().replace("\n","")
rhost=rhost.split(" ")[1]

rmac=a.readline().replace("\n","")
rmac=rmac.split(" ")[1]

os.system("packets.tcl 'ethernet(dst='%s',src='%s',type=0x0800)+ip(ihl=5,ver=4,tos=00,totlen=31,id=60976,fragoff=0,mf=0,df=1,rf=0,ttl=64,proto=tcp,cksum=0x40c9,saddr='%s',daddr='%s')+tcp(sport=12345,dport=12345,seq=1804471615,ack=0,ns=0,off=5,flags=s,win=62694,cksum=0xda46,urp=0)' > werk.pcap"%(rmac,lmac,lhost,rhost))

print("done")
