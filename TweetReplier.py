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

        print("len of (TwitReplier) handle list: ", len(self.screen_name_list))
        print("len of (TwitReplier) twit id list: ", len(self.tweet_id_list))

    def screen_name_follower(self):

        print("the following replies to everyone in the csv")
        try:
            for i in range(len(self.screen_name_list)):
                gls.api.update_status(f"@{self.screen_name_list[i]}  {self.custom_tweet_list[randint(0, len(self.custom_tweet_list) - 1)]}", in_reply_to_status_id=self.tweet_id_list[i][:-1])
                time.sleep(randint(5, 60))

                t = randint(12, 654)
                time.sleep(t)

                print(f"thread just slept for {t} seconds...")
                del (self.screen_name_list[i])
                del (self.custom_tweet_list[i])

                print(f'index - {i} len - {len(self.screen_name_list)}')

                if i == 5 or len(self.screen_name_list) < 5:
                    break

        except tweepy.TweepError as e:
            print("problem sending tweets ", e.reason)

        except Exception as e:
            print("the problem is: ", e)

        finally:
            pass

        print("screen_name_follower() has terminated after 5 iterations and deletions ")
        return len(self.screen_name_list)

