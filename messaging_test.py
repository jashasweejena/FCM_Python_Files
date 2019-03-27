import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

print('hdhd')

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

registration_token = get_file_contents('keys/firebase_registration_token')

cred = credentials.Certificate('keys/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

def send_to_token(message_text):
    # [START send_to_token]
    # This registration token comes from the client FCM SDKs.

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'data': message_text
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_token]

