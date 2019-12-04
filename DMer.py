import globals as gls
import time
import tweepy
from random import randint

# this is for dm-ing people that follow you

# this loop gets a list of everyone i follow
follower_id_list = []
screen_name_list = []


def follower_extractor(screen_name):
    for single_follower in tweepy.Cursor(gls.api.followers, screen_name="GikSoundz").items():

        # print(f"{single_follower.id} - {single_follower.screen_name}")
        screen_name_list.append(single_follower.screen_name)
        follower_id_list.append(single_follower.id)

        time.sleep(randint(1, 65))


def follower_looper(fol_id_list, custom_msg_list):
    # this loop sends dms to everyone I follow
    for i in range(len(follower_id_list)):
        gls.api.send_direct_message(follower_id_list[i], f'Custom message {screen_name_list[i]} Cheers!')
        time.sleep(randint(9, 34))



