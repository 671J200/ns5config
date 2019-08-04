import http.client
import json
import ssl


def ns5login(hostname,username,password):
  contx = ssl._create_unverified_context()

  connection = http.client.HTTPSConnection(hostname, context=contx)
  headers = {'Content-type': 'application/json'}

  creds = {
            'username': username,
            'password': password
          }
  json_creds = json.dumps(creds)
  print(json_creds)
  connection.request('POST', '/auth/login', json_creds, headers)

  response = connection.getresponse()
  print(response.read().decode())



