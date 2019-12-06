import tweepy
import globals as gls
import time
from random import randint
import csv


class HashtagTweeter:
    # tweeting on a given hashtag
    first_line = True

    def __init__(self, tweet_list_csv, action, tweets_list, hashtag):
        self.tweets_list_csv = tweet_list_csv
        self.action = action
        self.tweets_list = tweets_list
        self.hashtag = hashtag

    def tweet_reader(self):
        with open("tweets_for_today.csv", "r") as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                global first_line
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop
                self.tweets_list.append(single_row[0])

        print(self.tweets_list)

    def tweet_sender(self):
        for single_tweet in self.tweets_list:
            # the following line sends out the tweets from the list
            gls.api.update_status(single_tweet + "#DogsMostWanted")
            time.sleep(randint(5, 60))
