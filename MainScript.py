import globals as gls
import TweetDownloader as td
from DMer import *
from MentionReplier import *
from TweetReplier import *
from HashtagTweeter import *
from ScreenNameFollower import *
import time


# for putting everything together... somehow
# todo put everything together in this file
# todo finally deploy on two twitter accounts

while 1:
    custom_joke_list = []
    custom_thnx_list = []
    custom_facts_list = []

    # open csv and populate above lists
    first_line = True
    try:
        with open("tweets.csv", "r") as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop
                custom_joke_list.append(single_row[0])
                custom_thnx_list.append(single_row[1])
                custom_facts_list.append(single_row[2])
    except IOError:
        print("problem reading the csv")
    finally:
        pass

    # download all tweets from given hashtag and and from said data
    twitDl_1 = td.TwitDloader(hash_tag='FridayMotivation', count_num=1500, language='en', from_date='2019-12-05', hashtag_tweet_csv ="hashtag_tweets.csv", action="a")
    twitDl_1.tweet_list_downloader()
    print("DONE with tweet extraction")

    # follow everyone with the provided handle
    handle_follower = HandleFollower(screen_name_list=[], tweets_list_csv="hashtag_tweets.csv", action="r")
    handle_follower.hashtag_tweet_reader()
    handle_follower.twitter_user_follower()

    # replies to everyone in the csv
    twt_replier = TwitReplier(screen_name_list=[], tweet_id_list=[], custom_tweet_list=custom_facts_list, hashtag_tweet_csv="hashtag_tweets.csv", action="r")
    twt_replier.tweet_reader()
    twt_replier.screen_name_follower()

    # send these direct messages to everyone that follows the screen name
    dm_1 = DMSlider(follower_id_list=[], screen_name_list=[], screen_name="GikSoundz", custom_msg_list=custom_thnx_list)
    dm_1.follower_extractor()
    dm_1.follower_looper()

    # reply to all mentions and adds the given hashtag
    mention_replier_1 = MentionsRepr(value_holder_file='last_seen_id.txt', hash_tag='#FridayMotivation', custom_message_list=custom_joke_list)
    mention_replier_1.custom_replier()

    # tweet on a given hashtag
    hashtag_twtr = TwitOnHashTag(tweet_list_csv="tweets_for_today.csv", action="r", tweets_list=[], hashtag="#CashAppChillFriday")
    hashtag_twtr.tweet_reader()
    hashtag_twtr.tweet_sender()

    # clear the lists  and hashtag.csv, wait a while and start the loop again
    custom_facts_list.clear()
    custom_joke_list.clear()
    custom_thnx_list.clear()

    f = open("hashtag_tweets.csv", "w+")
    f.truncate()
    f.close()
    time.sleep(randint(153, 600))
