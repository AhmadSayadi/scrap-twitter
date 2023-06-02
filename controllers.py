import snscrape.modules.twitter as twitterScraper
from flask import request

class Controller:
    def gettwit(self):
        self.store_tweets=[]
        if request.method == 'POST':
            request_data = request.get_json()
            query = request_data['query']
            limit = request_data['limit']
            jenis = request_data['jenis']

            if(jenis=='Hashtag') :
                for tweet in twitterScraper.TwitterHashtagScraper(query).get_items():
                    if len(self.store_tweets) == limit:
                        break
                    else:
                        self.store_tweets.append(tweet)
            if(jenis=='Cari Nama') :
                query = "'from:"+request_data['query']+"'"
                for tweet in twitterScraper.TwitterHashtagScraper(query).get_items():
                    if len(self.store_tweets) == limit:
                        break
                    else:
                        self.store_tweets.append(tweet)
            else :
                for tweet in twitterScraper.TwitterSearchScraper(query).get_items():
                    if len(self.store_tweets) == limit:
                        break
                    else:
                        self.store_tweets.append(tweet)
            return {
                'jenis':jenis,
                'status_code':00, #Sukses
                'msg':"success",
                'data': self.store_tweets
            }, 200
