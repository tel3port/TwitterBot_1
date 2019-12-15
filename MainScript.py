import globals as gls
import TweetDownloader as td
from DMer import *
from MentionReplier import *
from TweetReplier import *
from HashtagTweeter import *
from ScreenNameFollower import *
import time

# for putting everything together... somehow

loop_num = 1
while 1:
    print("STARTING LOOP NUMBER ", loop_num)
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
                    col_0 = gls.random_default_msg()

                if len(col_1) < 15:
                    col_1 = gls.random_default_msg()

                if len(col_2) < 15:
                    col_2 = gls.random_default_msg()

                custom_joke_list.append(single_row[0])
                custom_thnx_list.append(single_row[1])
                custom_facts_list.append(single_row[2])
    except IOError:
        print("problem reading the csv")
    finally:
        pass

        # download all tweets from given hashtag and and from said data
        twitDl_1 = td.TwitDloader(hash_tag=gls.random_hashtag(), count_num=1500, language='en',from_date=gls.random_date(), hashtag_tweet_csv=gls.hashtag_tweet_csv, action="a")
        twitDl_1.tweet_list_downloader()
        print("DONE with tweet extraction")

        # follow everyone with the provided handle
        handle_follower = HandleFollower(screen_name_list=[], tweets_list_csv=gls.hashtag_tweet_csv, action=gls.write)
        handle_follower.hashtag_tweet_reader()

        # replies to everyone in the csv
        twt_replier = TwitReplier(screen_name_list=[], tweet_id_list=[], custom_tweet_list=custom_facts_list,hashtag_tweet_csv=gls.hashtag_tweet_csv, action=gls.write)
        twt_replier.tweet_reader()

        # send these direct messages to everyone that follows the screen name
        dm_1 = DMSlider(follower_id_list=[], screen_name_list=[], screen_name="GikSoundz",custom_msg_list=custom_thnx_list)
        dm_1.follower_extractor()

        # reply to all mentions and adds the given hashtag
       # mention_replier_1 = MentionsRepr(value_holder_file=gls.value_holder_file, hash_tag=gls.random_hashtag(),custom_message_list=custom_joke_list)

        # tweet on a given hashtag
        hashtag_twtr = TwitOnHashTag(tweet_list_csv=gls.tweets_for_today, action=gls.write, tweets_list=[],hashtag=gls.random_hashtag())
        hashtag_twtr.tweet_reader()

        handle_follower.twitter_user_follower()
        twt_replier.single_tweet_replier()
        dm_1.follower_looper()
        #mention_replier_1.custom_replier()
        hashtag_twtr.tweet_sender()

        # t = randint(10800, 22320)
        #
        # time.sleep(t)  # sleep for 3 - 6.2 hours and start the loop again
