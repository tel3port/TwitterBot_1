import globals as gls
import csv
from random import randint
import time
import tweepy

# for following people based on their @'screen names'


class HandleFollower:

    def __init__(self, screen_name_list, tweets_list_csv, action):
        self.screen_name_list = screen_name_list
        self.tweets_list_csv = tweets_list_csv
        self.action = action

    def hashtag_tweet_reader(self):
        first_line = True

        try:
            with open(self.tweets_list_csv, self.action) as rdr:
                reader = csv.reader(rdr, delimiter=",")
                for single_row in reader:

                    if first_line:  # this skips th first line
                        first_line = False
                        continue  # used this way, the rest of the code from here is skipped in this loop
                    self.screen_name_list.append(single_row[0])

        except IOError:
            print("problem opening or reading the csv")

        finally:
            pass

        print(self.screen_name_list)

    def twitter_user_follower(self):

        count = 0
        try:
            for single_screen_name in self.screen_name_list:
                print("uncommenting the following line follows everyone in the csv")
                gls.api.create_friendship(screen_name=single_screen_name)
                time.sleep(randint(5, 60))

        except tweepy.TweepError as e:
            print("problem messaging follower list ", e.reason)
        finally:
            pass
