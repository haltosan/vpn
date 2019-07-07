# VPN
This (as the name suggests) is a janky vpn. The project was built for my junior project (glorified science fair, but way harder). It has a 
server side application and a client side application. The client side is the master branch, while the server side is the 'server' branch.

## Getting Started

### Prerequisites
The system this is running on is a kali linux (clien and server). The purpose is because is contained many packet crafting and injecting 
tools (what the system runs on). It can work on any other linux (haven't tried it on anything else than debian) with the proper tools.
Needed tools for both client and server are:
* ifconfig
* python
* python3 (both are needed)
* [hexinject](http://hexinject.sourceforge.net/)
* hex2raw (part of hexinject)
* packets.tcl (part of hexinject)
* prettypacket (part of hexinject) - Not used in main system

### Setup
**Client**

The system requires no instilation (past the tools). To use the sysem, the config file has to be properly setup.
* lhost - Local host (client ip)
* lmac - Local mac (client mac address)
* rhost - Remote host (server ip)
* rmac - Remote mac (server mac address)
* int - Interface (ex: eth0)
The key file should also be changed. The key can be any hex value.
This needs to be the same on the server.
**Server**

The server has to be setup as well. The only difference is 'int' is the listening interface, while 'curlInt' is the internet interface. It 
is important to note they have to be different to work. The 'int' doesn't nessesarily have to be connected to the internet for it to work.
Next, the server has to be listening. To do this, run the Listen script:
```
bash Listen.sh
```
## Running
To run the basic system, run the pretty script:
```
python3 pretty.py
```
The prompt to 'update priv' will chmod the bash files. This is needed for the system to work. Next, the client will send the 'keep 
listening' signal to the server, so the server must be listening before running this script. On exit, the client can send the 'stop 
listening' signal to the server. This stops the server and it then has to be manually set to listen again.

**Individual modules**

To post data to a server/api:
```
./Post.sh
```
To get a webpage:
```
./Site.sh
```
To resend the last sent packet/custom made packet:
```
./Send.sh
```
To listen for a server response:
```
./Listen.sh
```
## Strengths
**todo**
## Extra fun/modification
Each request to the server has a unique task id. This task id identifies what sort of packet it is. 
**to be continued**
