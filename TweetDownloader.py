import tweepy
import csv
import globals as gls
from random import randint
import time


def csv_opener():
    tweets_csv = open("hashtag_tweets.csv", 'a')
    csv_writer = csv.writer(tweets_csv)
    return csv_writer


class TweetDownloader:
    def __init__(self, hashtag_tweets_list, action,  hash_tag, count_num, language, from_date):
        self.hashtag_tweets_list = hashtag_tweets_list
        self.action = action
        self. hash_tag = hash_tag
        self.count_num = count_num
        self.language = language
        self.from_date = from_date

    def tweet_list_downloader(self):
        for single_tweet in tweepy.Cursor(gls.api.search, q="#DogsMostWanted", count=1500, lang="en",
                                          since="2019-07-29").items():
            print(single_tweet.id_str)
            single_tweet.favorite()
            single_tweet.retweet()  # retweets and favs then waits for a few seconds before going on with iteration
            time.sleep(randint(5, 55))
            print(single_tweet.author, single_tweet.created_at, single_tweet.text)
            self.hashtag_tweets_list.writerow(
                [single_tweet.author.screen_name, single_tweet.created_at, str(single_tweet.id_str) + "x",
                 single_tweet.text.encode('utf-8')])

        print("end of tweet download")
