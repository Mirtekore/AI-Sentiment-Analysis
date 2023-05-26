import ijson
import simplejson as json
import re 

def parse_json(json_filename):
    with open(json_filename, 'rb') as input_file:
        # load json iteratively
        tweet = ijson.items(input_file, "docs.item")
        keywords_re = "openai|a\.i\.|artificial intelligence|machine learning|neural network|natural language processing|computer vision|deep learning|unsupervised learning|supervised learning|reinforcement learning|sentiment analysis|gpt3|midjourney|stable diffusion|stablediffusion|starryai|nightcafe|craiyon|jasper art|#promptsharing|prompt engineer|#promptengineering|#aicommunity|google bard|anthropicai|palm-2|bardai|large language model|generativeai|generative ai|chatbot|deepmind|diffusion model|FinOps|virtualassistant|selfdrivingcar|musiclm|deforum|so-vits-svc|notion ai|notionai|newbing|copilot"
        i = 0
        j = 0
        ai_tweets = []
        for o in tweet:
            doc = o.get("doc")
            if (not(doc is None)):
                data = doc.get("data")                
                if (not(data is None)):
                    text = data["text"].lower()
                    keyword_found = re.search(keywords_re, text)
                    if keyword_found:
                        ai_tweets.append(doc)
        current_json = {"docs": ai_tweets } 
        outfile = open(f'ai_keyword_tweets.json', "w")
        json.dump(current_json, outfile)
        outfile.close()

if __name__ == '__main__':
    parse_json('./twitterdata/twitter-huge.json')