from twython import Twython
from Inspirotron_Image_Processing import getFinalImage
from time import sleep

APP_KEY = 'paste here'
APP_SECRET = 'paste here'
OAUTH_TOKEN = 'paste here'
OAUTH_TOKEN_SECRET = 'paste here'

while True:
    twitter = Twython(APP_KEY,APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    text = getFinalImage()

    photo = open('out.jpeg', 'rb')
    response = twitter.upload_media(media=photo)

    twitter.update_status(status=text, media_ids=[response['media_id']])

    sleep(1200)


