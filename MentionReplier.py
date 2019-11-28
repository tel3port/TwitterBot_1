import tweepy
import globals as gls

# to reply to everyone that mentions me


VALUE_HOLDER_FILE = 'last_seen_id.txt'


def get_last_seen_id(my_file):
    f_read = open(my_file, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def save_last_seen_id(my_id, my_file):
    f_write = open(my_file, 'w')
    f_write.write(str(my_id))
    f_write.close()
    return


mentions = gls.api.mentions_timeline()

print(mentions[0].__dict__.keys())  # converts list into dict and extracts all the keys

print(mentions[0].text)

for single_mention in mentions:
    print(f"{single_mention.id} - {single_mention.text}")

