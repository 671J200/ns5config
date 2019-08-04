#!/usr/bin/env python
from lib.ns5auth import *
HOST="192.168.77.128"
PORT="8443"
USER="admin"
PASS="nexentA01"



ns5login(HOST + ":" + PORT, USER, PASS)
