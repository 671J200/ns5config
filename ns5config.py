#!/usr/bin/env python3
import lib.ns5request as ns5request
import lib.multipart_encoder as multipart_encoder
import json

HOST="10.0.100.91"
PORT="8443"
USER="admin"
PASS="nexentA01"

NODE= HOST + ":" + PORT


conn = ns5request.Ns5request()
conn.ns5login(NODE, USER, PASS)
jsonOutput = conn.ns5get("/inventory/disks?limit=250")
diskInfo = json.loads(jsonOutput)
for disk in diskInfo['data']:
  print(disk['logicalDevice'], "OnlinePhyCount:",  disk['multipath']['onlinePhyCount'])

#headers, body = multipart_encoder.multipart_encoder({"license":""},{"license":"license.txt"})
#print(headers)
