import snscrape.modules.twitter as twitterScraper
from flask import request

class Controller:
    def gettwit(self):
        self.store_tweets=[]
        query = "Ansor Jatim"
        limit = 100
        for tweet in twitterScraper.TwitterSearchScraper(query).get_items():
            if len(self.store_tweets) == limit:
                break
            else:
                result =vartweet(tweet)
                self.store_tweets.append(result)
        return {
            'status_code':00, #Sukses
            'msg':"success",
            'data': self.store_tweets
        }, 200
    def gettwit3(self):
        self.store_tweets=[]
        query = "from:lviikmatin_"
        limit = 100
        request_data = request.get_json()

        query = request_data['query']


        if request.method == 'POST':
            return {
                'status_code':00, #Sukses
                'msg':"success",
                'data':query
                # 'data': //self.store_tweets
            }, 200



        

def vartweet(tweet):
       data ={
            "id": tweet.id,
            "url": str(tweet.url),
            "date": str(tweet.date),
            "raw_content": tweet.rawContent,
            "rendered_content": tweet.renderedContent,
            "user": str(tweet.user),
            "replyCount": tweet.replyCount,
            "retweetCount": tweet.retweetCount,
            "likeCount": tweet.likeCount,
            "quoteCount": tweet.quoteCount,
            "conversationId": tweet.conversationId,
            "lang": tweet.lang,
            "source": tweet.source,
            "sourceUrl": tweet.sourceUrl,
            "sourceLabel": str(tweet.sourceLabel),
            "links": str(tweet.links),
            "media": str(tweet.media),
            "retweetedTweet": str(tweet.retweetedTweet),
            "quotedTweet": str(tweet.quotedTweet),
            "inReplyToTweetId": str(tweet.inReplyToTweetId),
            "inReplyToUser": str(tweet.inReplyToUser),
            "mentionedUsers": str(tweet.mentionedUsers),
            "coordinates": tweet.coordinates,
            "place": tweet.place,
            "hashtags": tweet.hashtags,
            "cashtags": tweet.cashtags,
            "card": str(tweet.card),
            "viewCount": tweet.viewCount,
            "vibe": tweet.vibe,
            "bookmarkCount": tweet.bookmarkCount,
            "username": tweet.username,
            "outlinks": tweet.outlinks,
            "outlinksss": tweet.outlinksss,
            "tcooutlinks": tweet.tcooutlinks,
            "tcooutlinksss": tweet.tcooutlinksss,
            "content": tweet.content
        }
       return data