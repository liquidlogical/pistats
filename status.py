#!/usr/bin/env python
# -*- coding: utf-8
# Based on pcgod's mumble-ping script found at http://0xy.org/mumble-ping.py.
# Hacked by Liquid <Host> <Port>


from struct import *
import socket, sys, time, datetime
from pyglow import PyGlow
from time import sleep
import os
    
pyglow = PyGlow()

pyglow.all (0)

host = sys.argv[1]
port = int(sys.argv[2])


while True:

 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.settimeout(10)

 buf = pack(">iQ", 0, datetime.datetime.now().microsecond)
 s.sendto(buf, (host, port))

 try:
  data, addr = s.recvfrom(1024)
 except socket.timeout:
 #print "%d:NaN:NaN" % (time.time())
  sys.exit()
  
 s.close()
  
 #print "recvd %d bytes" % len(data)
 r = unpack(">bbbbQiii", data)

 # version = r[1:4]
 # r[0,1,2,3] = version
 # r[4] = ts
 # r[5] = users
 # r[6] = max users
 # r[7] = bandwidth

 ping = (datetime.datetime.now().microsecond - r[4]) / 1000.0
 if ping < 0: ping = ping + 1000
 
 if r[5] < 1: pyglow.all (1), sleep (1), pyglow.all (0)
 if r[5] >= 1: pyglow.color ("blue",75),pyglow.color ("white",75)
 if r[5] >= 2: pyglow.color ("blue",75),pyglow.color ("white",75),pyglow.color ("green",75)
 if r[5] >= 3: pyglow.color ("blue",75),pyglow.color ("white",75),pyglow.color ("green",75), pyglow.color ("yellow",75)
 if r[5] >= 4: pyglow.color ("blue",75),pyglow.color ("white",75),pyglow.color ("green",75), pyglow.color ("yellow",75), pyglow.color ("orange",75)
 if r[5] >= 5: pyglow.color ("blue",75),pyglow.color ("white",75),pyglow.color ("green",75), pyglow.color ("yellow",75), pyglow.color ("orange",75), pyglow.color ("red",75)


# print "Version %d.%d.%d, %d/%d Users, %.1fms, %dkbit/s" % (version + (r[5], r[6], ping, r[7]/1000))

 sleep(5)