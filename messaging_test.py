import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

print('hdhd')

def send_to_token():
    # [START send_to_token]
    # This registration token comes from the client FCM SDKs.
    registration_token = 'eVLe-2qO67s:APA91bGzgBANFENHlHFoXjmXudkfK1dZaWaNlZJ9uwhQtHNuVWDsGcKMArxQNOEW2updmXC2ezQKYJgojv13jqIRAhJXkjJ_924WxXxOxh6VLokqJihVWs_rnsJ-HiQMjKOW4eRydXcf'

    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_token]

send_to_token()

