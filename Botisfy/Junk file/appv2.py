import http.client

conn = http.client.HTTPSConnection("api.msg91.com")

headers = { 'content-type': "application/json" }

conn.request("GET", "/api/v5/otp?extra_param=%7B%22Param1%22%3A%22Value1%22%2C%20%22Param2%22%3A%22Value2%22%2C%20%22Param3%22%3A%20%22Value3%22%7D&unicode=&authkey=Authentication%20Key&template_id=Template%20ID&mobile=Mobile%20Number%20with%20Country%20Code&invisible=1&otp=OTP%20to%20send%20and%20verify.%20If%20not%20sent%2C%20OTP%20will%20be%20generated.&userip=IPV4%20User%20IP&email=Email%20ID&otp_length=&otp_expiry=", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))