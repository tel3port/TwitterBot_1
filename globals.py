import tweepy
from random import randint
import time
import logging

hashtag_tweet_csv = "hashtag_tweets.csv"
tweets_for_today = "tweets_for_today.csv"
tweets = "tweets.csv"
value_holder_file = 'last_seen_id.txt'

write = 'r'

CONSUMER_KEY = "dfgdsg"
CONSUMER_SECRET = "dfgdf"
ACCESS_KEY = "dgdfg-xk7V2qkRygrC53122WMwVvGNCxCwLL"
ACCESS_SECRET = "dgdf"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


random_num = randint(1, 5)

# todo load up the hashtag list 50 for NZ


def random_hashtag():
    hashtag_list = ["#mondaymotivation",
                    "#newzealand",
                    "#nz",
                    "#travel",
                    "#ShortlandStreet",
                    "#NZBFC630",
                    "#LISTEN",
                    "#Breaking",
                    "#StandUpWithYourNix",
                    "#nzpol",
                    "#cricketnation",
                    "#superrugby",
                    "#ClimateChange",
                    "#nzqt",
                    "#mafsau",
                    "#LiteraryFiction",
                    "#TheBlockNZ",
                    "#dunedin",
                    "#COYS",
                    "#ClimateAction",
                    "#ISPSHandaPrem",
                    "#Mitre10Cup",
                    "#Brexit",
                    "#edchatnz",
                    "#CreateHistory",
                    "#BlackCaps",
                    "#WATCH",
                    "#bitcoin",
                    "#eNovAaW",
                    "#lfsanzcod",
                    "#Christchurch",
                    "#bksupersmash",
                    "#innovation",
                    "#RWC2019",
                    "#BACKBLACK",
                    "#CWC19",
                    "#wellington",
                    "#DWTSNZ",
                    "#amwriting",
                    "#BACKTHEBLACKCAPS",
                    "#eqnz",
                    "#VASC",
                    "#CWC2019",
                    "#parttimePM",
                    "#ClimateCrisis",
                    "#mentalhealth",
                    "#AllBlacks",
                    "#nationnz",
                    "#TheOrville",
                    "#gamedev",
                    "#FootballFerns",
                    "#trump",
                    "#NZwine",
                    "#STEMeducation",
                    "#Cricket",
                    "#WWESuperCard",
                    "#Unity4J",
                    "#FreeAssange",
                    "#PlunketShield",
                    "#auspol",
                    "#science",
                    "#PokemonGO",
                    "#Auckland",
                    "#ClimateStrike",
                    "#Australia",
                    "#GameOfThrones",
                    "#HudsonValley",
                    "#BB13",
                    "#GOT7",
                    "#NZvENG",
                    "#COYN",
                    "#MeToo",
                    "#ClimateEmergency",
                    "#MAFSNZ",
                    "#Fortnite",
                    "#leadership",
                    "#crypto",
                    "#NZvIND",
                    "#forthefern",
                    "#srilanka",
                    "#joytrain",
                    "#starwars",
                    "#MakeOilHistory",
                    "#Photography",
                    "#SurvivorAU",
                    "#Ashes",
                    "#writingcommunity",
                    "#WeAreWarriors",
                    "#NZvBAN",
                    "#Twitch",
                    "#SecretSantaNZ2019",
                    "#BirdOfTheYear",
                    "#ChathamCup",
                    "#NBAPlayoffs",
                    "#BiggBoss13",
                    "#rugbyworldcup",
                    "#rwc19",
                    "#vaping",
                    "#nzfgc",
                    "#CriticalRole",
                    "#Supernatural",
                    "#LOVETHESTAGS",
                    "#kiwi",
                    "#FreebieFriday",
                    "#MondayMorning",
                    "#interesting"
                    ]

    random_index = randint(0, len(hashtag_list)-1)
    return hashtag_list[random_index]


def random_date():
    date_list = ['2017-12-01',
                 '2017-11-06',
                 '2017-10-03',
                 '2017-07-02',
                 '2017-12-01',
                 '2017-05-06',
                 '2017-09-03',
                 '2017-08-07',
                 '2017-12-01',
                 '2017-11-16',
                 '2017-10-23',
                 '2017-07-12',
                 '2017-12-21',
                 '2017-05-07',
                 '2017-09-23',
                 '2017-08-17'
                 ]

    random_index = randint(0, len(date_list) - 1)

    return date_list[random_index]


def random_default_msg():
    msg_list = ["hi! we a re running a small contest. Can you win? https://win-150-dollars-now.weebly.com/",
                "would you like to participate in a contest to win some money for the holidays? https://win-a-fortune-today.weebly.com/",
                "hi! This is a small contest for our twitter users. Can you win? https://win-150-dollars-now.weebly.com/",
                "We are giving away some cash to our twitter users. Do you want in? https://win-a-fortune-today.weebly.com/",
                "hi! we a re running a small contest. Are you interested? https://win-150-dollars-now.weebly.com/",
                "would you like to participate in a contest to win some money for the holidays? https://win-a-fortune-today.weebly.com/",
                "A this contest our fall prize pool https://win-150-dollars-now.weebly.com/",
                "play this contest our fall prize pool  https://win-a-fortune-today.weebly.com/",
                "Play this game now now. Get 50% off.  https://win-a-fortune-today.weebly.com/",
                "THis is for our best twitter users  https://win-a-fortune-today.weebly.com/",
                "life is short! Act now  https://win-a-fortune-today.weebly.com/",
                "Apply to this contest and Save today  https://win-a-fortune-today.weebly.com/",
                "Hellow? Looking for 123 winners. Yes! I want one.  https://win-a-fortune-today.weebly.com/",
                "Order now  https://win-a-fortune-today.weebly.com/",
                "Repeat your order  https://win-a-fortune-today.weebly.com/",
                "Claim your coupon  https://win-a-fortune-today.weebly.com/",
                "follow and Reveal my mystery coupon  https://win-a-fortune-today.weebly.com/",
                "Start saving today  https://win-150-dollars-now.weebly.com/",
                "Don’t delay. Save now.  https://win-150-dollars-now.weebly.com/",
                "See your hand-selected deals  https://win-150-dollars-now.weebly.com/",
                "Apply and 50% off now  https://win-150-dollars-now.weebly.com/",
                "Play for the clothes you want  https://win-150-dollars-now.weebly.com/",
                "Get the style you want  https://win-150-dollars-now.weebly.com/",
                "Get your winter wardrobe  https://win-150-dollars-now.weebly.com/",
                "Get free shipping  https://win-150-dollars-now.weebly.com/",
                "Free gift with purchase  https://win-150-dollars-now.weebly.com/"]

    random_index = randint(0, len(msg_list) - 1)

    return msg_list[random_index]


def sleep_time():
    t = randint(15, 120)
    print(f"thread sleeping for {t} seconds...")

    time.sleep(t)

    return t


def log_file_writer():
    return logging.basicConfig(filename='twitter_log_error_logs.log',
                               format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                               datefmt='%Y-%m-%d:%H:%M:%S',
                               level=logging.ERROR)
