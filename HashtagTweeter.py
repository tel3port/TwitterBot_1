import tweepy
import globals as gls
import time
from random import randint
import csv

# tweeting on a given hashtag

tweets_list = []
firstLine = True


def tweet_reader(tweet_list_csv):
    with open("tweets_for_today.csv", "r") as rdr:
        reader = csv.reader(rdr, delimiter=",")
        for single_row in reader:
            if firstLine:  # this skips th first line
                firstLine = False
                continue  # used this way, the rest of the code from here is skipped in this loop
            tweets_list.append(single_row[0])

    print(tweets_list)


def tweet_sender(tweet_list, hash_tag):
    for single_tweet in tweets_list:
        print("uncommenting the following line sends out the tweets from the list")
        # gls.api.update_status(single_tweet + "#DogsMostWanted")
        time.sleep(randint(5, 60))
