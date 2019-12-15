import globals as gls
import csv
import tweepy
import logging

# for following people based on their @'screen names'


class HandleFollower:

    def __init__(self, screen_name_list, tweets_list_csv, action):
        self.screen_name_list = screen_name_list
        self.tweets_list_csv = tweets_list_csv
        self.action = action

        screen_name_list_copy = self.screen_name_list

    def hashtag_tweet_reader(self):
        gls.log_file_writer()

        first_line = True

        try:
            with open(self.tweets_list_csv, self.action) as rdr:
                reader = csv.reader(rdr, delimiter=",")
                for single_row in reader:

                    if first_line:  # this skips th first line
                        first_line = False
                        continue  # used this way, the rest of the code from here is skipped in this loop
                    self.screen_name_list.append(single_row[0])

        except IOError as e:
            logging.error('Error occurred ' + str(e))

        finally:
            pass

        print("len of handle list: ", len(self.screen_name_list))

    def twitter_user_follower(self):
        print("starting twitter_user_follower()")

        gls.log_file_writer()
        try:
            for index in range(len(self.screen_name_list)-1):
                print(f"creating friendship with: {self.screen_name_list[index]}")

                gls.api.create_friendship(screen_name=self.screen_name_list[index])

                time_slept = gls.sleep_time()
                #
                # del (self.screen_name_list[index])
                #
                # print(f'index - {index} len - {len(self.screen_name_list)}')
                #
                # if index == gls.random_num or len(self.screen_name_list) < gls.random_num:
                #     break

        except tweepy.TweepError as e:
            logging.error('Error occurred ' + str(e))

        except Exception as e:
            logging.error('Error occurred ' + str(e))

        finally:
            pass

        print("twitter_user_follower() has terminated after 5 iterations and deletions ")
        return len(self.screen_name_list)