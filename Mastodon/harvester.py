from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import sys, couchdb
from bs4 import BeautifulSoup

# m = Mastodon(
#         api_base_url=sys.argv[2],
#         access_token=sys.argv[1]
#     )

# class Listener(StreamListener):

#     def on_update(self, status):
#         # Extract the content field from toot, convert html format of toot into string
#         toot = BeautifulSoup(status["content"], 'html.parser').get_text()
#         json_doc = {'content': toot}
#         # Insert json doc here
    
#     def handle_heartbeat(self):
#         return super().handle_heartbeat()

# m.stream_hashtag('ai',Listener(), timeout=120)


######## Mastodon and couch db code below (only works on vm because of network bridge stuff) ###############

remote_server = couchdb.Server("https://admin:Zi12ZnK2r2n@172.26.135.240:5984/")
db = remote_server.create('Test')
doc = {'foo': 'bar'}
print(db.save(doc))
