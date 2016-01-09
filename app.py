#!env/bin/python
import os
import redis
import traceback
from instapaperlib import Instapaper

config = {
    'CHANNEL': 'instapaper',
    'USERNAME': '',
    'PASSWORD': '',
}

print "Launching redis to instapaper component"

# take config items from environment where present
for configitem in config:
    if configitem in os.environ:
        config[configitem] = os.environ[configitem]

i = Instapaper(config['USERNAME'], config['PASSWORD'])

try:
    red = redis.StrictRedis("redis")
    red_pubsub = red.pubsub()
    red_pubsub.subscribe(config['CHANNEL'])
except:
    print "Failed to subscribe to channel"

try:
    while True:
        for item in red_pubsub.listen():
            if str(item['data']).lower().startswith('http'):
                print "Adding item: " , item['data']
                (statuscode, statusmessage) = i.add_item(item['data'])
                print "Instapaper response: ", statuscode, statusmessage
            else:
                print "Bad data: ", item['data']
except Exception as e:
    print traceback.format_exc()

