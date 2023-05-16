import ijson

import simplejson as json

def parse_json(json_filename):
    with open(json_filename, 'rb') as input_file:
        # load json iteratively
        tweet = ijson.items(input_file, "docs.item")
        i = 0
        j = 0
        compiled_tweets = []
        for o in tweet:
            doc = o.get("doc")
            if (not(doc is None)):
                includes = doc.get("includes")
                if (not(includes is None)):
                    if "places" in includes:
                        doc.pop("_rev")
                        compiled_tweets.append(doc)
                        j += 1
            if (j > 50000):
                current_json = {"docs": compiled_tweets} 
                json_string = json.dumps(compiled_tweets)
                outfile = open(f'located-tweets{i}.json', "w")
                jsonStr = json.dump(current_json, outfile)
                outfile.close()
                compiled_tweets = []
                i += 1
                j = 0
            if (i > 0):
                break
        i += 1
        current_json = {"docs": compiled_tweets} 
        json_string = json.dumps(compiled_tweets)
        outfile = open(f'located-tweets{i}.json', "w")
        jsonStr = json.dump(current_json, outfile)
        outfile.close()

if __name__ == '__main__':
    parse_json('./twitterdata/twitter-huge.json')