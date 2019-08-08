#!/usr/bin/env python
import lib.ns5request as ns5request
import lib.multipart_encoder as multipart_encoder

HOST="192.168.77.128"
PORT="8443"
USER="admin"
PASS="nexentA01"

NODE= HOST + ":" + PORT


conn = ns5request.Ns5request()
conn.ns5login(NODE, USER, PASS)
print(conn.ns5get("/network/links"))


#headers, body = multipart_encoder.multipart_encoder({"license":""},{"license":"license.txt"})
#print(headers)
