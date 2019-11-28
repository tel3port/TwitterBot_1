import tweepy
import globals as gls
import csv
import time
from random import randint

# this is to reply to all the tweets from a given hashtag from csv of downloaded tweets

screen_name_list = []
tweet_id_list = []
firstLine = True

with open("hashtag_tweets.csv", "r") as rdr:
    reader = csv.reader(rdr, delimiter=",")
    for single_row in reader:
        if firstLine:  # this skips th first line
            firstLine = False
            continue  # used this way, the rest of the code from here is skipped in this loop
        screen_name_list.append(single_row[0])
        tweet_id_list.append(single_row[2])


for i in range(len(screen_name_list)):
    print("uncommenting the following line replies to everyone in the csv")
    #gls.api.update_status(f"@{screen_name_list[i]}  this is custom tweet" ,in_reply_to_status_id=tweet_id_list[i][:-1])
    time.sleep(randint(5, 60))

# todo add functionality to send out  related images and gifs