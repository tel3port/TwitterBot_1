import tweepy

hashtag_tweet_csv = "hashtag_tweets.csv"
tweets_for_today = "tweets_for_today.csv"
tweets = "tweets.csv"
value_holder_file = 'last_seen_id.txt'


CONSUMER_KEY = "vNdmTB5he6nZPMJ52alKPUSXE"
CONSUMER_SECRET = "R5vdHLRj6c6KZYwPZwMFRC0viJCsSXlGDZtmbGC3dMudteq0Wg"
ACCESS_KEY = "1027222327044517888-xk7V2qkRygrC53122WMwVvGNCxCwLL"
ACCESS_SECRET = "X513wVVUW3yyIE3HnEmSEaGdYWsmHIcVBeHUGUdX9TcvI"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


