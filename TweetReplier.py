import tweepy
import globals as gls
import csv
import time
from random import randint


class TweetReplier:
    first_line = True
    # this is to reply to all the tweets from a given hashtag from csv of downloaded tweets

    def __init__(self, my_tweet_list_csv, screen_name_list, tweet_id_list, custom_tweet_list):
        self.screen_name_list = screen_name_list
        self.tweet_id_list = tweet_id_list
        self.my_tweet_list_csv = my_tweet_list_csv
        self.custom_tweet_list = custom_tweet_list

    def tweet_reader(self):
        with open("hashtag_tweets.csv", "r") as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                global first_line
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop
                self.screen_name_list.append(single_row[0])
                self.tweet_id_list.append(single_row[2])

    def screen_name_follower(self, ):
        for i in range(len(self.screen_name_list)):
            print("uncommenting the following line replies to everyone in the csv")
            gls.api.update_status(f"@{self.screen_name_list[i]}  this is custom tweet", in_reply_to_status_id=self.tweet_id_list[i][:-1])
            time.sleep(randint(5, 60))
