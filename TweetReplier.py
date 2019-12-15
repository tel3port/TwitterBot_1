import tweepy
import globals as gls
import csv
from random import randint
import logging


class TwitReplier:

    # this is to reply to all the tweets from a given hashtag from csv of downloaded tweets

    def __init__(self, screen_name_list, tweet_id_list, custom_tweet_list, hashtag_tweet_csv, action):
        self.screen_name_list = screen_name_list
        self.tweet_id_list = tweet_id_list
        self.custom_tweet_list = custom_tweet_list
        self.hashtag_tweet_csv = hashtag_tweet_csv
        self. action = action

    def tweet_reader(self):
        gls.log_file_writer()

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

        except IOError as e:
            logging.error('Error occurred ' + str(e))

        finally:
            pass

        print("len of (TwitReplier) handle list: ", len(self.screen_name_list))
        print("len of (TwitReplier) twit id list: ", len(self.tweet_id_list))

    def single_tweet_replier(self):
        print("starting screen_name_follower()")

        gls.log_file_writer()

        try:
            for i in range(len(self.screen_name_list)):
                gls.api.update_status(status=f"@{self.screen_name_list[i]}  {self.custom_tweet_list[randint(0, len(self.custom_tweet_list) - 1)]}", in_reply_to_status_id=self.tweet_id_list[i][:-1])
                time_slept = gls.sleep_time()
                #
                # del (self.screen_name_list[i])
                # del (self.custom_tweet_list[i])
                #
                # print(f'index - {i} len - {len(self.screen_name_list)}')
                #
                # if i == gls.random_num or len(self.screen_name_list) < gls.random_num:
                #     break

        except tweepy.TweepError as e:
            logging.error('Error occurred ' + str(e))

        except Exception as e:
            logging.error('Error occurred ' + str(e))

        finally:
            pass

        print("screen_name_follower() has terminated after 5 iterations and deletions ")
        return len(self.screen_name_list)
