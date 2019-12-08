import tweepy
import globals as gls
import csv
import time
from random import randint


class TwitReplier:

    # this is to reply to all the tweets from a given hashtag from csv of downloaded tweets

    def __init__(self, screen_name_list, tweet_id_list, custom_tweet_list, hashtag_tweet_csv, action):
        self.screen_name_list = screen_name_list
        self.tweet_id_list = tweet_id_list
        self.custom_tweet_list = custom_tweet_list
        self.hashtag_tweet_csv = hashtag_tweet_csv
        self. action = action

    def tweet_reader(self):
        first_line = True
        try:
            with open(self.hashtag_tweet_csv, self.action) as rdr:
                reader = csv.reader(rdr, delimiter=",")
                for single_row in reader:
                    if first_line:  # this skips th first line
                        first_line = False
                        continue  # used this way, the rest of the code from here is skipped in this loop
                    self.screen_name_list.append(single_row[0])
                    self.tweet_id_list.append(single_row[2])

        except IOError:
            print("problem reading the file")
        finally:
            pass

        print("len of handle list: ", len(self.screen_name_list))
        print("len of twit id list: ", len(self.tweet_id_list))

    def screen_name_follower(self):

        print("the following replies to everyone in the csv")
        try:
            for i in range(len(self.screen_name_list)):
                gls.api.update_status(f"@{self.screen_name_list[i]}  {self.custom_tweet_list[randint(0, len(self.custom_tweet_list) - 1)]}", in_reply_to_status_id=self.tweet_id_list[i][:-1])
                time.sleep(randint(5, 60))

        except tweepy.TweepError as e:
            print("problem sending tweets ", e.reason)
        finally:
            pass
