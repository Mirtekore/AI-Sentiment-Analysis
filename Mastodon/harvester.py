from mastodon import Mastodon, StreamListener
import sys, couchdb
from bs4 import BeautifulSoup

# Connect to database based on arguments passed in shell script
remote_server = couchdb.Server(sys.argv[3])
db = remote_server['mastodon']

m = Mastodon(
        api_base_url=sys.argv[2],
        access_token=sys.argv[1]
    )

class Listener(StreamListener):

    def on_update(self, status):
        # Extract the content field from toot, convert html format of toot into string
        toot = BeautifulSoup(status["content"], 'html.parser').get_text()
        json_doc = {'content': toot}
        db.save(json_doc)
    
    def handle_heartbeat(self):
        return super().handle_heartbeat()
    
    # Restart the harvester when error occurs
    def on_abort(self, err):
        m.stream_hashtag('ai',Listener(), timeout=120)
        return super().on_abort(err)

m.stream_hashtag('ai',Listener(), timeout=120)
