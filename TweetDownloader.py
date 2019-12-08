import tweepy
import csv
import globals as gls
from random import randint
import time


class TwitDloader:
    def __init__(self, hash_tag, count_num, language, from_date,hashtag_tweet_csv, action):
        self.hash_tag = hash_tag
        self.count_num = count_num
        self.language = language
        self.from_date = from_date
        self.hashtag_tweet_csv = hashtag_tweet_csv
        self.action = action

    def tweet_list_downloader(self):
        try:
            tweets_csv = open(self.hashtag_tweet_csv, self.action)
            csv_writer = csv.writer(tweets_csv)

            for single_tweet in tweepy.Cursor(gls.api.search, q=self.hash_tag, count=self.count_num, lang=self.language,
                                              since=self.from_date).items():
                print(single_tweet.id_str)
                single_tweet.favorite()
                single_tweet.retweet()  # retweets and favs then waits for a few seconds before going on with iteration
                time.sleep(randint(5, 55))
                print(single_tweet.author, single_tweet.created_at, single_tweet.text)

                csv_writer.writerow(
                    [single_tweet.author.screen_name, single_tweet.created_at, str(single_tweet.id_str) + "x",
                     single_tweet.text.encode('utf-8')])

        except IOError:
            print("problem opening the said csv file")

        except tweepy.TweepError as e:
            print("error downloading the tweets", e.reason)

        except Exception as x:
            print("something or the other went wrong", x.args)

        finally:
            print("end of tweet extraction")
