import tweepy
import csv
import globals as gls
from random import randint
import time


class TweetDownloader:
    def __init__(self):
        global csv_writer

    def csv_opener(self, hashtag_tweets_list, action):
        tweets_csv = open("hashtag_tweets.csv", 'a')
        csv_writer = csv.writer(tweets_csv)

    def tweet_list_downloader(self, hash_tag, count_num, language, from_date):
        for single_tweet in tweepy.Cursor(gls.api.search, q="#DogsMostWanted", count=1500, lang="en",
                                          since="2019-07-29").items():
            print(single_tweet.id_str)
            single_tweet.favorite()
            single_tweet.retweet()  # retweets and favs then waits for a few seconds before going on with iteration
            time.sleep(randint(5, 55))
            print(single_tweet.author, single_tweet.created_at, single_tweet.text)
            csv_writer.writerow(
                [single_tweet.author.screen_name, single_tweet.created_at, str(single_tweet.id_str) + "x",
                 single_tweet.text.encode('utf-8')])

        print("end of tweet download")
