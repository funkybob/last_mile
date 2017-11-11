from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8c09caad3b4b2a5aec323c4c04dfb4ff"
# Your Auth Token from twilio.com/console
auth_token  = "c5c86372de625580a8c3202465701b84"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+61421179133", 
    from_="+61418720218",
    body="Hello from Python!")

print message.sid
