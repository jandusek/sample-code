from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "[AuthToken]"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+441632960675",
    messaging_service_sid="MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    body="Phantom Menace was clearly the best of the prequel trilogy.",
)
