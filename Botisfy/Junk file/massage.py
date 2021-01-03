from twilio.rest import Client

account_ssd = "AC9a91106e66d05bae7ffafa9954deeaa7"
auth_token = "5415f62d4bda17f072ad274a4d56e34e"

client = Client(account_ssd,auth_token)
client.messages.create(from_="+12055486702", body='''hello world''', to="+2510939167494")
