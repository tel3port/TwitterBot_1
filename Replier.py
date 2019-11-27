import tweepy
import globals as gls

# this is to reply to all the tweets from a given hashtag


mentions = gls.api.mentions_timeline()

for single_mention in mentions:
    print(str(single_mention.id) +" - " + single_mention.text)
    if "#MondayMorning".lower() in single_mention.text.lower():
        print("found")


