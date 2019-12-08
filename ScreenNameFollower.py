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

        print("len of handle list: ", len(self.screen_name_list))

    def twitter_user_follower(self):
        print("uncommenting the following line follows everyone in the csv")

        try:
            for index in range(len(self.screen_name_list)):
                print(f"creating friendship with: {self.screen_name_list[index]}")

                gls.api.create_friendship(screen_name=self.screen_name_list[index])

                t = randint(15, 600)
                time.sleep(t)

                print(f"thread just slept for {t} seconds...")
                del (self.screen_name_list[index])

                print(f'index - {index} len - {len(self.screen_name_list)}')

                if index == 5 or len(self.screen_name_list) < 5:
                    break

        except tweepy.TweepError as e:
            print("problem messaging follower list ", e.reason)

        except Exception as e:
            print("the problem is: ", e)

        finally:
            pass

        print("twitter_user_follower() has terminated after 5 iterations and deletions ")
        return len(self.screen_name_list)
