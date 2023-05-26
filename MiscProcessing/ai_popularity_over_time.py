import ijson
import simplejson as json

def parse_json(json_filename):
    with open(json_filename, 'rb') as input_file:
        # load json iteratively
        tweet = ijson.items(input_file, "docs.item")
        i = 0
        j = 0
        counter = {}
        for o in tweet:
            data = o.get("data")
            if (not(data is None)):
                date = data.get("created_at")[0:10]                
                if date not in counter:
                    counter[date] = 0
                else:
                    counter[date] += 1
        current_json = {"date_count": counter} 
        outfile = open(f'tweet_frequencies_ai.json', "w")
        json.dump(current_json, outfile)
        outfile.close()

if __name__ == '__main__':
    # Use result of pre-processing
    parse_json('./ai_keyword_tweets.json')