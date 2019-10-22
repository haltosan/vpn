# VPN
This (as the name suggests) is a vpn. The project was built for my junior project. It has a server side application and a client 
side application. The client side is the master branch, while the server side is the 'server' branch.

## Getting Started

### Prerequisites
The system this is running on is a kali linux (client and server). The purpose is because is contained many packet crafting and 
injecting 
tools (what the system runs on). It can work on any other linux (haven't tried it on anything else than debian) with the proper
tools.
Needed tools for both client and server are:
* ifconfig
* python
* python3 (both are needed)
* [hexinject](http://hexinject.sourceforge.net/)
* hex2raw (part of hexinject)
* packets.tcl (part of hexinject)
* prettypacket (part of hexinject) - Optional package I used in development

### Setup
**Client**

The system requires no instillation (past the tools). To use the system, the config file has to be properly setup.
* lhost - Local host (client ip)
* lmac - Local mac (client mac address)
* rhost - Remote host (server ip)
* rmac - Remote mac (server mac address)
* int - Interface (ex: eth0)


The key file should also be changed. The key can be any hex value.
This needs to be the same on the server.

**Server**

The server has to be setup as well. The only difference is 'int' is the listening interface, while 'curlInt' is the internet 
interface. It is important to note they have to be different to work. The 'int' doesn't necessarily have to be connected to the 
internet for it to work. Next, the server has to be listening. To do this, run the Listen script:
```
bash Listen.sh
```
## Running
To run the basic system, run the pretty script:
```
python3 pretty.py
```
The prompt to 'update priv' will chmod the bash files. This is needed for the system to work. Next, the client will send the 
'keep listening' signal to the server, so the server must be listening before running this script. On exit, the client can send 
the 'stop listening' signal to the server. This stops the server and it then has to be manually set to listen again.

**Individual modules**

To post data to a server/api:
```
./Post.sh
```
To get a webpage:
```
./Site.sh
```
To resend the last sent packet/custom-made packet:
```
./Send.sh
```
To listen for a server response:
```
./Listen.sh
```
## Strengths
The system masquerades it's traffic as tcp, but the system actually uses udp. This prevents sessions hijacking. Also, the system 
has similar anonymous capabilities to TOR in that eavesdroppers will identify that the user is on the network, or that some user 
is requesting a service, not both. The encryption can be upgraded by anybody who feels it needs to be done (now using rot-n). 

## Extra fun/modification
**Packets**

Each request to the server has a unique task id. This task id identifies what sort of packet it is. The meaning of these task 
id's can be seen in the *tasks.py* files on server and client. The task id is the first data in the packet (**00** 01 02). For 
example, a packet reading `00 01` has a task id of 00. New task id's can be made, with functionality for the server or client, 
depending on the need. Next is the data. The data can be a hex encoded html file, or a command. For example, the packet `00 01` 
has a task id of 00, data of 01. This task id is the listening signal, 01 meaning 'keep listening' (00 to stop). You have the 
power of python, so anything is possible.

**Encryption**

To modify the encryption, modify the *encode.py* and *dencode.py* files on both sides, along with *key* if needed. The system is 
an n-tier build, so most modifications will not interfere with overall functionality. The plan was to upgrade to AES, but the 
deadline stopped this upgrade.
