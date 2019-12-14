import tweepy
import globals as gls
import csv
import logging


class TwitOnHashTag:
    # tweeting on a given hashtag

    def __init__(self, tweet_list_csv, action, tweets_list, hashtag):
        self.tweets_list_csv = tweet_list_csv
        self.action = action
        self.tweets_list = tweets_list
        self.hashtag = hashtag

    def tweet_reader(self):
        gls.log_file_writer()

        first_line = True
        try:
            with open(self.tweets_list_csv, self.action) as rdr:
                reader = csv.reader(rdr, delimiter=",")
                for single_row in reader:
                    if first_line:  # this skips th first line
                        first_line = False
                        continue  # used this way, the rest of the code from here is skipped in this loop
                    self.tweets_list.append(single_row[0])
        except IOError as e:
            logging.error('Error occurred ' + str(e))

        finally:
            pass

        print("len of tweet list ", len(self.tweets_list))

    def tweet_sender(self):
        print("starting tweet_sender()")

        gls.log_file_writer()

        try:
            for i in range(len(self.tweets_list)):
                # the following line sends out the tweets from the list
                gls.api.update_status(f'{self.tweets_list[i]} {gls.random_hashtag()}')

                time_slept = gls.sleep_time()

                del (self.tweets_list[i])

                print(f'index - {i} len - {len(self.tweets_list)}')

                if i == gls.random_num or len(self.tweets_list) < gls.random_num:
                    break

        except tweepy.TweepError as e:
            logging.error('Error occurred ' + str(e))

        finally:
            pass

        print("follower_looper() has terminated after 5 iterations and deletions ")
        return len(self.tweets_list)
