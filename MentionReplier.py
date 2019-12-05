import tweepy
import globals as gls
import time
from random import randint


# to reply to everyone that mentions me

def save_last_seen_id(my_id, my_file):
    f_write = open(my_file, 'w')
    f_write.write(str(my_id))
    f_write.close()
    return


def get_last_seen_id(my_file):
    f_read = open(my_file, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


class MentionReplier:
    def __init__(self, value_holder_file):
        self.value_holder_file = value_holder_file
        # VALUE_HOLDER_FILE = 'last_seen_id.txt'

    def mention_replier(self):
        print("replying to custom mentions...")
        last_seen_id = get_last_seen_id(self.value_holder_file)

        mentions = gls.api.mentions_timeline(last_seen_id, tweet_mode='extended')

        # print(mentions[0].__dict__.keys())  # converts list into dict and extracts all the keys
        #
        # print(mentions[0].text)
        # 1163451084704079873 for testing
        for single_mention in reversed(mentions):
            print(f"{single_mention.id} - {single_mention.full_text}")
            last_seen_id = single_mention.id
            save_last_seen_id(last_seen_id, self.value_holder_file)

            gls.api.update_status("good day to you , @" + single_mention.user.screen_name + " #DogsMostWanted",
                                  single_mention.id)
            time.sleep(randint(5, 55))

        print("end of reply cycle")


def let_the_games_begin(self):
    while True:
        self.mention_replier()
        time.sleep(randint(6, 44))
