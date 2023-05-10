#!/usr/bin/env python3

from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json
import couchdb

os.environ['MASTODON_ACCESS_TOKEN'] ="psbBwt1Fup13_91jQXtLxrWZ6U57XOwZmX5LK-ZF-sU"

remote_server = couchdb.Server("https://admin:admin@172.17.0.4:5984/")
db = remote_server['twitter']
mango = {"selector": {"user.lang": {"$eq": "ja"}}}

for i in db.find(mango): print(i)

# toot = {
#   "account": {
#     "acct": "alessiopomaro@mastodon.uno",
#     "avatar": "https://files.mastodon.social/cache/accounts/avatars/109/303/607/405/681/942/original/83c3791dc57a5843.png",
#     "avatar_static": "https://files.mastodon.social/cache/accounts/avatars/109/303/607/405/681/942/original/83c3791dc57a5843.png",
#     "bot": false,
#     "created_at": "2022-11-06 00:00:00+00:00",
#     "discoverable": true,
#     "display_name": "Alessio Pomaro",
#     "emojis": [],
#     "fields": [
#       {
#         "name": "web",
#         "value": "<a href=\"https://www.alessiopomaro.it\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"\">alessiopomaro.it</span><span class=\"invisible\"></span></a>",
#         "verified_at": null
#       },
#       {
#         "name": "linkedin",
#         "value": "<a href=\"https://www.linkedin.com/in/alessiopomaro/\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"\">linkedin.com/in/alessiopomaro/</span><span class=\"invisible\"></span></a>",
#         "verified_at": null
#       },
#       {
#         "name": "facebook",
#         "value": "<a href=\"https://www.facebook.com/alessio.pomaro\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"\">facebook.com/alessio.pomaro</span><span class=\"invisible\"></span></a>",
#         "verified_at": null
#       }
#     ],
#     "followers_count": 67,
#     "following_count": 23,
#     "group": false,
#     "header": "https://files.mastodon.social/cache/accounts/headers/109/303/607/405/681/942/original/fdb35f4889e9349f.png",
#     "header_static": "https://files.mastodon.social/cache/accounts/headers/109/303/607/405/681/942/original/fdb35f4889e9349f.png",
#     "id": 109303607405681942,
#     "last_status_at": "2023-05-10 00:00:00",
#     "locked": false,
#     "note": "<p>Head of SEO, Head of Voice Technology, AI Conversation Designer. Autore di Brand Voice (FrancoAngeli Editore) e Voice Technology (Dario Flaccovio Editore).<br>\ud83d\udd17 <a href=\"https://www.alessiopomaro.it\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"\">alessiopomaro.it</span><span class=\"invisible\"></span></a></p>",
#     "statuses_count": 422,
#     "url": "https://mastodon.uno/@alessiopomaro",
#     "username": "alessiopomaro"
#   },
#   "card": null,
#   "content": "<p>\"La nostra ricerca fornisce una risposta fornendo ai modelli linguistici valori espliciti determinati da una costituzione, piuttosto che valori determinati implicitamente tramite feedback umano su larga scala\". </p><p><a href=\"https://mastodon.uno/tags/AI\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>AI</span></a> <a href=\"https://mastodon.uno/tags/IntelligenzaArtificiale\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>IntelligenzaArtificiale</span></a> <a href=\"https://mastodon.uno/tags/LLM\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>LLM</span></a> <a href=\"https://mastodon.uno/tags/OpenAI\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>OpenAI</span></a> <a href=\"https://mastodon.uno/tags/futuro\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>futuro</span></a> <a href=\"https://mastodon.uno/tags/innovazione\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>innovazione</span></a> <a href=\"https://mastodon.uno/tags/anthropic\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>anthropic</span></a> </p><p><a href=\"https://www.linkedin.com/posts/alessiopomaro_claudes-constitution-activity-7061941605452136448-DAWk\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"ellipsis\">linkedin.com/posts/alessiopoma</span><span class=\"invisible\">ro_claudes-constitution-activity-7061941605452136448-DAWk</span></a></p>",
#   "created_at": "2023-05-10 06:03:27+00:00",
#   "edited_at": null,
#   "emojis": [],
#   "favourites_count": 0,
#   "filtered": [],
#   "id": 110342871995671859,
#   "in_reply_to_account_id": null,
#   "in_reply_to_id": null,
#   "language": "it",
#   "media_attachments": [],
#   "mentions": [],
#   "poll": null,
#   "reblog": null,
#   "reblogs_count": 0,
#   "replies_count": 0,
#   "sensitive": false,
#   "spoiler_text": "",
#   "tags": [
#     {
#       "name": "ai",
#       "url": "https://mastodon.social/tags/ai"
#     },
#     {
#       "name": "intelligenzaartificiale",
#       "url": "https://mastodon.social/tags/intelligenzaartificiale"
#     },
#     {
#       "name": "llm",
#       "url": "https://mastodon.social/tags/llm"
#     },
#     {
#       "name": "openai",
#       "url": "https://mastodon.social/tags/openai"
#     },
#     {
#       "name": "futuro",
#       "url": "https://mastodon.social/tags/futuro"
#     },
#     {
#       "name": "innovazione",
#       "url": "https://mastodon.social/tags/innovazione"
#     },
#     {
#       "name": "anthropic",
#       "url": "https://mastodon.social/tags/anthropic"
#     }
#   ],
#   "uri": "https://mastodon.uno/users/alessiopomaro/statuses/110342871944572912",
#   "url": "https://mastodon.uno/@alessiopomaro/110342871944572912",
#   "visibility": "public"
# }
# doc_id, doc_rev =  db.save(toot)

m = Mastodon(
        api_base_url=f'https://mastodon.social',
        access_token=os.environ['MASTODON_ACCESS_TOKEN']
    )

class Listener(StreamListener):

    def on_update(self, status):
        print(json.dumps(status, indent=2, sort_keys=True, default=str))
    
    def handle_heartbeat(self):
        print("Thump")
        return super().handle_heartbeat()

# m.stream_hashtag('ai',Listener(), timeout=120)

# curl -XPOST "http://${user}:${pass}@${masternode}:5984/twitter/_find" \
# --header "Content-Type: application/json" --data '{
#    "fields" : ["account.content"],
#    "selector": {
#       "language": {"$eq": "it"}
#    }
# }'  | jq '.' -M
