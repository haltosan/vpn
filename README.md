# VPN
This (as the name suggests) is a janky vpn. The project was built for my junior project (glorified science fair, but way harder). It has a 
server side application and a client side application. The client side is the master branch, while the server side is the 'server' branch.

## Getting Started

### Prerequisites
The system this is running on is a kali linux (clien and server). The purpose is because is contained many packet crafting and injecting 
tools (what the system runs on). It can work on any other linux (haven't tried it on anything else than debian) with the proper tools.
Needed tools are:
* ifconfig
* python
* [hexinject](http://hexinject.sourceforge.net/)
* hex2raw (part of hexinject)
* packets.tcl (part of hexinject)
* prettypacket (part of hexinject) - Not used in main system

### Running
The system requires no instilation (past the tools). To use the sysem, the config file has to be properly setup.
* lhost - Local host (client ip)
* lmac - Local mac (client mac address)
* rhost - Remote host (server ip)
* rmac - Remote mac (server mac address)
* int - Interface (ex: eth0)

The server has to be setup as well. The only difference is 'int' is the listening interface, while 'curlInt' is the internet interface. It 
is important to note they have to be different to work. The 'int' doesn't nessesarily have to be connected to the internet for it to work.
