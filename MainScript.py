import globals as gls
import TweetDownloader as td
from DMer import *
from MentionReplier import *
from TweetReplier import *
from HashtagTweeter import *
from ScreenNameFollower import *
import time

# for putting everything together... somehow
# todo LOAD UP THE CSVs AND THE hashtag LIST
# todo run the code till it breaks out of the loops
# todo the short circuit
# todo uncomment th code at the end of this page
# todo finally deploy on two twitter accounts

loop_num = 0
while 1:
    custom_joke_list = []
    custom_thnx_list = []
    custom_facts_list = []

    # open csv and populate above lists
    first_line = True
    try:
        with open(gls.tweets, gls.write) as rdr:
            reader = csv.reader(rdr, delimiter=",")
            for single_row in reader:
                if first_line:  # this skips th first line
                    first_line = False
                    continue  # used this way, the rest of the code from here is skipped in this loop

                col_0 = single_row[0]
                col_1 = single_row[1]
                col_2 = single_row[2]

                if "." in single_row[0]:
                    col_0 = single_row[0].split(".")[1]

                if "." in single_row[1]:
                    col_1 = single_row[1].split(".")[1]

                if "." in single_row[2]:
                    col_2 = single_row[2].split(".")[1]

                if len(col_0) < 15:
                    col_0 = "https://freebie-heaven.weebly.com/"

                if len(col_1) < 15:
                    col_1 = "https://freebie-heaven.weebly.com/"

                if len(col_2) < 15:
                    col_2 = "https://freebie-heaven.weebly.com/"

                custom_joke_list.append(single_row[0])
                custom_thnx_list.append(single_row[1])
                custom_facts_list.append(single_row[2])
    except IOError:
        print("problem reading the csv")
    finally:
        pass

    # download all tweets from given hashtag and and from said data
    twitDl_1 = td.TwitDloader(hash_tag=gls.random_hashtag(), count_num=1500, language='en', from_date=gls.random_date(), hashtag_tweet_csv =gls.hashtag_tweet_csv, action="a")
    twitDl_1.tweet_list_downloader()
    print("DONE with tweet extraction")

    # follow everyone with the provided handle
    handle_follower = HandleFollower(screen_name_list=[], tweets_list_csv=gls.hashtag_tweet_csv, action=gls.write)
    handle_follower.hashtag_tweet_reader()

    # replies to everyone in the csv
    twt_replier = TwitReplier(screen_name_list=[], tweet_id_list=[], custom_tweet_list=custom_facts_list, hashtag_tweet_csv=gls.hashtag_tweet_csv, action=gls.write)
    twt_replier.tweet_reader()

    # send these direct messages to everyone that follows the screen name
    dm_1 = DMSlider(follower_id_list=[], screen_name_list=[], screen_name="GikSoundz", custom_msg_list=custom_thnx_list)
    dm_1.follower_extractor()

    # reply to all mentions and adds the given hashtag
    mention_replier_1 = MentionsRepr(value_holder_file=gls.value_holder_file, hash_tag=gls.random_hashtag(), custom_message_list=custom_joke_list)

    # tweet on a given hashtag
    hashtag_twtr = TwitOnHashTag(tweet_list_csv=gls.tweets_for_today, action=gls.write, tweets_list=[], hashtag=gls.random_hashtag())
    hashtag_twtr.tweet_reader()

    while 1:
        current_handle_num = handle_follower.twitter_user_follower()
        current_screen_name_num = twt_replier.screen_name_follower()
        current_follower_num = dm_1.follower_looper()
        mention_replier_1.custom_replier()
        current_tweet_num = hashtag_twtr.tweet_sender()

        if current_handle_num <= 3:
            break

    # clear the lists  and hashtag.csv, wait a while and start the loop again
    # custom_facts_list.clear()
    # custom_joke_list.clear()
    # custom_thnx_list.clear()
    #
    # f = open(gls.hashtag_tweet_csv, "w+")
    # f.truncate()
    # f.close()
    # gls.sleep_time()

    loop_num += 1
    if loop_num == 3:
        break

print("finished. Remove the above statement, uncomment and deploy")

