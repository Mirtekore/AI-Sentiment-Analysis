from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import sys, couchdb
from bs4 import BeautifulSoup

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

m.stream_hashtag('ai',Listener(), timeout=120)


################### CouchDB x Mastodon troubleshooting code below ###############################
# remote_server.resource.session.disable_ssl_verification()

# db = remote_server.create('test')

# doc = {'foo': 'bar'}
# print(db.save(doc))

# username = "admin"
# password = "Zi12ZnK2r2n"
# host = "172.26.135.240:5984"

# remote_server = couchdb.Server('http://'+host)
# remote_server.resource.session.disable_ssl_verification()
# remote_server.resource.credentials = (username, password)

# db = remote_server['test']

# doc = {'foo': 'bar'}
# # db.delete(doc)
# remote_server.delete('test')