import globals as gls

# for following people based on their @'screen names'

import csv
from random import randint
import time


class ScreenNameFollower:
    def __init__(self):
        screen_name_list = []
        first_line = True

    def hashtag_tweet_reader(self, tweets_list, screen_name_list):
        with open("hashtag_tweets.csv", "r") as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop
                screen_name_list.append(single_row[0])

    def twitter_user_follower(self, screen_name_list):
        for single_screen_name in screen_name_list:
            print("uncommenting the following line follows everyone in the csv")
            gls.api.create_friendship(screen_name=single_screen_name)
            time.sleep(randint(5, 60))
