import snscrape.modules.twitter as twitterScraper
from flask import request

class Controller:
    def gettwit(self):
        try:
            self.store_tweets=[]
            if request.method == 'POST':
                request_data = request.get_json()
                query1 = request_data['query']
                limit = request_data['limit']
                jenis = request_data['jenis']
                lokasi=''
                if(request_data['lokasi']):
                    lokasi=' geocode:"{}"'.format(request_data['lokasi'])
                # return print('tes',lokasi)
                query = request_data['query']+lokasi
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
                    'query':query,
                    'total_data':limit,
                    'jenis':jenis,
                    'status_code':1, #Sukses
                    'msg':"success",
                    'data': self.store_tweets
                }, 200
        except:
              return {
                'status_code':0, #error
                'msg':"error",
            }, 400

    def gettwit2(self):
        self.store_tweets=[]
        # -7.256377485031949, 112.75319583099417
        query = "bakso near:'Surabaya'",
        limit = 100
    
        for tweet in twitterScraper.TwitterHashtagScraper(query).get_items():
            if len(self.store_tweets) == limit:
                    break
            else:
                self.store_tweets.append(tweet)
        
        return {
            'status_code':1, #Sukses
            'msg':"success",
            'data': self.store_tweets
        }, 200