import tweepy
import globals

# this is to reply to all the tweets from a given hashtag

api = tweepy.API(globals.auth)

mentions = api.mentions_timeline()

for single_mention in mentions:
    print(str(single_mention.id) +" - " + single_mention.text)
    if "#MondayMorning".lower() in single_mention.text.lower():
        print("found")


