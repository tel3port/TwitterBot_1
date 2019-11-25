import tweepy


CONSUMER_KEY = "sUCgsoEIxYymWQCGUS2lq2AAj"
CONSUMER_SECRET = "qYPqA5YsLtdCTqgaMsMMMUPwQDK3ihq9Nyjvru8wXQb0x05qKS"
ACCESS_KEY = "1027222327044517888-F0gaqTdUT8brF6Fzd0rUNFyjuqrelW"
ACCESS_SECRET = "LVRBz6QUfiVUIHLaBkqtltpcSxKb3nyOdhzWiTQVD7oUR"

print("this is first bot")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for single_mention in mentions:
    print(str(single_mention.id) +" - " + single_mention.text)
    if "#MondayMorning".lower() in single_mention.text.lower():
        print("found")



