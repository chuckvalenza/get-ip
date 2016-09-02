#!/usr/bin/env python
#
#@author Chuck Valenza
#Resolve IP address from hostname
import time
from socket import gethostbyname, gaierror
hostname = raw_input("Enter hostname: ")
try:
    startTime = time.time()
    addr = gethostbyname(hostname)
    elapsedTime = time.time() - startTime
    print ("Hostname", hostname, "IP address =", addr, "Lookup took", elapsedTime, "seconds")
except gaierror:
    print ("Cannot resolve hostname", hostname)
