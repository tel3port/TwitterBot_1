import tweepy
from random import randint
import time

hashtag_tweet_csv = "hashtag_tweets.csv"
tweets_for_today = "tweets_for_today.csv"
tweets = "tweets.csv"
value_holder_file = 'last_seen_id.txt'

write = 'r'

CONSUMER_KEY = "vNdmTB5he6nZPMJ52alKPUSXE"
CONSUMER_SECRET = "R5vdHLRj6c6KZYwPZwMFRC0viJCsSXlGDZtmbGC3dMudteq0Wg"
ACCESS_KEY = "1027222327044517888-xk7V2qkRygrC53122WMwVvGNCxCwLL"
ACCESS_SECRET = "X513wVVUW3yyIE3HnEmSEaGdYWsmHIcVBeHUGUdX9TcvI"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# todo load up the hashtag list 50 for NZ
def random_hashtag():
    hashtag_list = ["a",
                    "c",
                    "v",
                    "g"]

    random_index = randint(0, len(hashtag_list))
    print(random_index)

    return hashtag_list[random_index-1]


def random_date():
    date_list = ['2019-12-01',
                 '2019-11-06',
                 '2019-10-03',
                 '2019-07-02',
                 '2019-12-01',
                 '2019-05-06',
                 '2019-09-03',
                 '2019-08-07'
                 ]

    random_index = randint(0, len(date_list))
    print(random_index)

    return date_list[random_index-1]


def sleep_time():
    t = randint(23, 769)
    time.sleep(t)
    print(f"thread just slept for {time} seconds...")

    return t

