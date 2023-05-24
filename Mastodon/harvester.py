# INFORMATION ----------------------------------------------------------------------------------------
# 
# Authors: COMP90024 Team 54
# This file was created for Mastodon harvesting for COMP90024 Cloud and Cluster Computing Assignment 2
#
# ----------------------------------------------------------------------------------------------------

from mastodon import Mastodon, StreamListener
import sys, couchdb
from bs4 import BeautifulSoup
from textblob import TextBlob

# Connect to database based on arguments passed in shell script
remote_server = couchdb.Server(sys.argv[3])
db = remote_server['mast']

m = Mastodon(
        api_base_url=sys.argv[2],
        access_token=sys.argv[1]
    )

class Listener(StreamListener):

    def on_update(self, status):
        # Extract the content field from toot, convert html format of toot into string
        toot = BeautifulSoup(status["content"], 'html.parser').get_text()
        toot_sentiment = TextBlob(toot).sentiment.polarity
        json_doc = {'content': toot, 'sentiment': toot_sentiment}
        db.save(json_doc)
    
    def handle_heartbeat(self):
        return super().handle_heartbeat()
    
    # Restart the harvester when error occurs
    def on_abort(self, err):
        m.stream_hashtag('ai',Listener(), timeout=120)
        return super().on_abort(err)

m.stream_hashtag('ai',Listener(), timeout=120)
