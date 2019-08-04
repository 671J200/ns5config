#!/usr/bin/env python
import lib.ns5auth as ns5auth
import lib.ns5request as ns5request


HOST="192.168.77.128"
PORT="8443"
USER="admin"
PASS="nexentA01"

NODE= HOST + ":" + PORT


conn = ns5request.Ns5request()
conn.ns5login(NODE, USER, PASS)

print(conn.get_token())
