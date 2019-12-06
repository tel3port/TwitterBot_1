import globals as gls
import time
import tweepy
from random import randint


# this is for dm-ing people that follow you

class DMSlider:
    def __init__(self, follower_id_list, screen_name_list, screen_name, custom_msg_list):
        self.follower_id_list = follower_id_list
        self.screen_name_list = screen_name_list
        self.screen_name = screen_name
        self.custom_msg_list = custom_msg_list

    # this loop gets a list of everyone i follow
    def follower_extractor(self):
        try:
            for single_follower in tweepy.Cursor(gls.api.followers, screen_name=self.screen_name).items():
                print(f"{single_follower.id} - {single_follower.screen_name}")
                self.screen_name_list.append(single_follower.screen_name)
                self.follower_id_list.append(single_follower.id)

                time.sleep(randint(1, 65))
        except tweepy.TweepError as e:
            print("problem downloading follower list ", e.reason)
        finally:
            pass

        print(self.follower_id_list)
        print(self.screen_name_list)

    def follower_looper(self):
        try:
            # this loop sends dms to everyone I follow
            for i in range(len(self.follower_id_list)):
                gls.api.send_direct_message(self.follower_id_list[i],
                                            f'{self.custom_msg_list[randint(0, len(self.custom_msg_list) - 1)]} {self.screen_name_list[i]} :)!')
                time.sleep(randint(9, 34))

        except tweepy.TweepError as e:
            print("problem messaging follower list ", e.reason)
        finally:
            pass
