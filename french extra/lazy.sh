#!/bin/bash

echo "starting"
echo "what payload to use?"
echo "> "
read payload
ifconfig
echo "what is your ip?"
echo ">"
read lhost
echo "what is your mac?"
echo ">"
read lmac
echo "what ip is the server at?"
echo "> "
read rhost
ping -c 4 $rhost
arp -D $rhost
echo "enter the server mac address"
echo ">"
read rmac
packets.tcl 'ethernet(dst='$rmac',src='$lmac',type=0x0800)+ip(ihl=5,ver=4,tos=00,totlen=31,id=60976,fragoff=0,mf=0,df=1,rf=0,ttl=64,proto=tcp,cksum=0x40c9,saddr='$lhost',daddr='$rhost')+tcp(sport=12345,dport=12345,seq=1804471615,ack=0,ns=0,off=5,flags=s,win=62694,cksum=0xda46,urp=0)' > werk.pcap
echo $payload | hex2raw >> werk.pcap
echo "made pcap"
timeout .3s bash transfer.sh
echo "end"
nano translated
