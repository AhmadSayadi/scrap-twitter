from flask import Flask, jsonify,request
from flask_restful import Api, Resource
from flask_cors import CORS
import snscrape.modules.twitter as twitterScraper
from controllers import Controller



app = Flask(__name__)
api = Api(app)
CORS(app)

def varTwit(self,tweet):
       dataa ={
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
       self.data=dataa
        # return data


class Variable(Resource):
    def get(self, tweet):
        self.data ={
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
                "content": tweet.content,
            }

        return self.data

class getTwit(Resource):
    def get(self):
        self.store_tweets=[]
        query = "Ansor Jatim"
        limit = 5000
        for tweet in twitterScraper.TwitterSearchScraper(query).get_items():
            if len(self.store_tweets) == limit:
                break
            else:
                  self.store_tweets.append(
                    {
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
                        "lang":str(tweet.lang),
                        "source": str(tweet.source),
                        "sourceUrl": str(tweet.sourceUrl),
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
                        "content": tweet.content,
                     })
        return self.store_tweets

class getTwitHastag(Resource):
    def get(self):
        self.store_tweets=[]
        query = "#PawaiKemenanganEmas"
        limit = 5000
        for tweet in twitterScraper.TwitterHashtagScraper(query).get_items():
            if len(self.store_tweets) == limit:
                break
            else:
                self.store_tweets.append(
                    {
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
                        "content": tweet.content,
                     })
                # self.store_tweets.append({"tweet_date":str(tweet.date), "username": tweet.username, "conten":tweet.content,"retweet_count":tweet.retweetCount,"tweet_countlink":tweet.tcooutlinks})
        return self.store_tweets

class getTwitTrend(Resource):
    def get(self):
        self.store_tweets=[]
        query = "'from:ahmadsayadi_ since:2023-05-17'"
        limit = 50
        for tweet in twitterScraper.TwitterSearchScraper(query).get_items():
            if len(self.store_tweets) == limit:
                break
            else:
                self.store_tweets.append({"tweet_date":str(tweet.date), "username": tweet.username, "conten":tweet.content,"retweet_count":tweet.retweetCount,"tweet_countlink":tweet.tcooutlinks})
        return self.store_tweets

class getTwitProfile(Resource):
    def get(self):
        self.store_tweets=[]
        query = "'from:ahmadsayadi_ since:2023-01-17 until:2023-05-18'"
        limit = 50
        for tweet in twitterScraper.TwitterSearchScraper(query).get_items():
            if len(self.store_tweets) == limit:
                break
            else:
                 
                self.store_tweets.append(
                    {
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
                        "content": tweet.content,
                     })
                # tweetvar = Variable(tweet)
                # tweetvar.get(tweet)

                # data1 =varTwit(tweet)
                # self.store_tweets.append(data1)
                
                # self.store_tweets.append(tweetvar)
                result = {
                     "msg":"success",
                    "status_code":200,
                    "data":self.store_tweets,
                   
                }
        return result


api.add_resource(getTwit,"/api/twit", methods=["GET"])

api.add_resource(getTwitHastag,"/api/twit_hashtag", methods=["GET"])

api.add_resource(getTwitTrend,"/api/twit_trend", methods=["GET"])

api.add_resource(getTwitProfile,"/api/twit_profile", methods=["GET"])






@app.route("/api2/twit", methods=['GET'])
def getTwit():
    return Controller.getTwit()



@app.route("/api/twitapp", methods=['GET','POST'])
def twitdata():
    controller = Controller()
    return controller.gettwit()

@app.route("/api/twitsearch", methods=['GET','POST'])
def twetsearch():
    controller = Controller()
    return controller.gettwit3()




if __name__ == "__main__":
    app.run(debug=True, port=5000)