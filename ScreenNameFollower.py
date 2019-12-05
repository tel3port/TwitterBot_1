import globals as gls
import csv
from random import randint
import time

# for following people based on their @'screen names'


class ScreenNameFollower:
    first_line = True

    def __init__(self, screen_name_list, tweets_list, tweets_list_csv, action):
        self.screen_name_list = screen_name_list
        self.tweets_list = tweets_list
        self.tweets_list_csv = tweets_list_csv
        self.action = action

    def hashtag_tweet_reader(self):
        with open("hashtag_tweets.csv", "r") as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                
                global first_line
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop
                self.screen_name_list.append(single_row[0])

    def twitter_user_follower(self):
        for single_screen_name in self.screen_name_list:
            print("uncommenting the following line follows everyone in the csv")
            gls.api.create_friendship(screen_name=single_screen_name)
            time.sleep(randint(5, 60))
