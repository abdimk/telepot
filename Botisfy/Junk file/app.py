import http.client

conn = http.client.HTTPSConnection("api.msg91.com")

payload = {
    "sender": "PUMA",
    "route": "4",
    "country": "251",
    "sms": [
        {
            "message": "Hello, you have won 1 birr.",
            "to": [
                "0939167494"
            ]
        }
    ]
}

headers = {
    'authkey': "9185AQqBttvZTu5fef4eb9P123",
    'content-type': "application/json"
    }

conn.request("POST", "/api/v5/flow/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))






#/api/v5/sendsms?campaign=&response=afterminutes=&schtime=&unicode=&flash=&message=&encrypt=&authkey=&mobiles=&routes=&sender=&country=91"