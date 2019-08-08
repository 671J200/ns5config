import http.client
import json
import ssl


class Ns5request:

    def __init__(self):
        self.token = "None"
        self.username = "None"
        self.password = "None"
        self.hostname = "None"
        self.header = "None"
        self.connection = ''

    def get_token(self):
        return self.token,self.header

    def ns5login(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        #  Freshly installed ns5 is a self signed cert for https, we want to enable this

        contx = ssl._create_unverified_context()

        self.connection = http.client.HTTPSConnection(self.hostname, context=contx)
        headers = {'Content-type': 'application/json'}

        creds = { 'username': self.username, 'password': self.password }
        json_creds = json.dumps(creds)
        self.connection.request('POST', '/auth/login', json_creds, headers)

        response = self.connection.getresponse()
        json_response = json.loads(response.read().decode())
        self.token = json_response.get('token')
        self.header = {
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                        "Authorization" : "Bearer " + self.token
                      }

    def ns5get(self, method):
        self.connection.request('GET', method, None, self.header)
        response = self.connection.getresponse()
        return(response.read().decode())


