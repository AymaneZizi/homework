
from twython import TwythonStreamer

APP_KEY = "PBotuM4Wbx4MSk5gm3VOQ"
APP_SECRET = "UuPhfwly4YRQjG3tqaVyxcgknWLxvZtTkk7Cecsv0"
OAUTH_TOKEN = "472096207-kQmVsCNTBSrgd8eTzHgXb2MrNduusw3zHH69YMhy"
OAUTH_TOKEN_SECRET = "HCAF2ea2sck3MzgWyB8EeErMamxEUVMc2qbkS5Fc2DTUY"

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()


stream = MyStreamer(APP_KEY, APP_SECRET,
                            OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='kashmir')
