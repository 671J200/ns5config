import http.client
import json
import ssl


class Ns5request:

    def __init__(self):
        self.token = "None"
        self.username = "None"
        self.password = "None"
        self.hostname = "None"

    def get_token(self):
        return self.token

    def ns5login(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        #  Freshly installed ns5 is a self signed cert for https, we want to enable this

        contx = ssl._create_unverified_context()

        connection = http.client.HTTPSConnection(self.hostname, context=contx)
        headers = {'Content-type': 'application/json'}

        creds = { 'username': self.username, 'password': self.password }
        json_creds = json.dumps(creds)
        connection.request('POST', '/auth/login', json_creds, headers)

        response = connection.getresponse()
        json_response = json.loads(response.read().decode())
        self.token = json_response.get('token')


