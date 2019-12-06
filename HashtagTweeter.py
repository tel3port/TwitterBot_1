import tweepy
import globals as gls
import time
from random import randint
import csv


class TwitOnHashTag:
    # tweeting on a given hashtag

    def __init__(self, tweet_list_csv, action, tweets_list, hashtag):
        self.tweets_list_csv = tweet_list_csv
        self.action = action
        self.tweets_list = tweets_list
        self.hashtag = hashtag

    def tweet_reader(self):
        first_line = True
        try:
            with open(self.tweets_list_csv, self.action) as rdr:
                reader = csv.reader(rdr, delimiter=",")
                for single_row in reader:
                    if first_line:  # this skips th first line
                        first_line = False
                        continue  # used this way, the rest of the code from here is skipped in this loop
                    self.tweets_list.append(single_row[0])
        except IOError:
            print("problem reading the csv")

        finally:
            pass

        print(self.tweets_list)

    def tweet_sender(self):
        count = 0
        try:
            for single_tweet in self.tweets_list:
                # the following line sends out the tweets from the list
                gls.api.update_status(single_tweet + self.hashtag)
                time.sleep(randint(5, 60))

        except tweepy.TweepError as e:
            print("problem tweeting out ", e.reason)
        finally:
            pass
