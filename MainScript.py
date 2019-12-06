import globals as gls
import TweetDownloader as td
from DMer import *

from MentionReplier import *

# for putting everything together... somehow
# todo use this file to make sure all the methods are working
# todo put everything together in this  file
# todo do error handling where required
# todo finally deploy on two twitter accounts

# download all tweets from given hashtag and and from said data
# twitDl_1 = td.TwitDloader(hash_tag='DogsMostWanted', count_num=1500, language='en', from_date='2019-12-05')
# twitDl_1.tweet_list_downloader()
# print("DONE with tweet extraction")


# send these direct messages to everyone that follows the screen name
custom_msg_list = ["your follow is very much appreciated",
                   "Your support and efforts for our new venture certainly contributed to our success, and I want to thank you for that. Good luck in all of your endeavors. ",
                   "It is our desire to keep you satisfied with our services and products. You are our inspiration in doing our very best. Thank you and remember; we value you!",
                   "Thank you very much for keeping our product the number one brand in town. We cannot achieve this success without you as our customer. Your satisfaction is our number one concern and we promise to stay reliable",
                   "We are truly grateful to you for choosing us as your service provider and giving us the opportunity to grow. None of our achievements would have been possible without you and your unwavering support",
                   "It has been a great pleasure serving you all through these years. We hope to continue this relationship in the forthcoming year with great reverence and respect. Wish you a happy and fulfilling new year",
                   "We would just like to say thank you for being a part of our family. We are very grateful for your continued patronage because we wouldn’t be here without loyal customers like you.",
                   "Our management would like to thank you for patronizing our products and also thank you for the opportunity to serve you. Truly, it is our pleasure. You are a valued customer to us.",
                   "We wish you a very happy and a prosperous new year. May this year bring you luck and laughter.",
                   "As the year comes to a close, we are glad to inform and share with you that it has been an incredible year of profits and profitable relationships. We thank you for your continued patronage, and wish you a very happy new year.",
                   "If we have to think about the resolutions we have to make for the new year, we only resolve to serve you better and with all our love. Thank you for being a part of our journey and for believing in us all through these years",
                   "Our company promises to provide high quality products for you as well as outstanding customer service for every transaction. Thank you and we are always happy to serve you.",
                   "Thank you for trusting us, for showing faith in us, and for letting us know that you will watch our back.",
                   "This year has been a challenge for us, but without you, we could not have turned these challenges into great challenges. Thank you for being with us",
                   "We appreciate your business and look forward to serving any additional needs in the future",
                   "Thank you for being our valued customer. We are grateful for the pleasure of serving you and meeting your printing needs. We wish you a beautiful holiday season and joyous new year",
                   "Thank you for trusting us! Together with our professional team, we promise to do our very best just to cater every little thing you need",
                   "Thank very much for your loyalty. We are very honor to have customer like you. As a matter of fact, we are looking forward to serve you in the following years",
                   "As we usher in the new year with great celebrations and expectations, we take this moment to express our heartfelt gratitude to you."]

# dm_1 = DMSlider(follower_id_list=[], screen_name_list=[], screen_name="GikSoundz", custom_msg_list=custom_msg_list)
#
# dm_1.follower_extractor()
#
# dm_1.follower_looper()


custom_joke_list = ["Today at the bank, an old lady asked me to help check her balance. So I pushed her over",
                    "I bought some shoes from a drug dealer. I dont know what he laced them with, but I've been tripping all day.",
                    "I told my girlfriend she drew her eyebrows too high. She seemed surprised.",
                    "My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.",
                    "I'm so good at sleeping. I can do it with my eyes closed.",
                    "Joke about going home from work",
                    "My boss told me to have a good day.. so I went home.",
                    "Why is Peter Pan always flying? He neverlands.",
                    "A woman walks into a library and asked if they had any books about paranoia. The librarian says 'They're right behind you!",
                    "The other day, my wife asked me to pass her lipstick but I accidentally passed her a glue stick. She still isn't talking to me.",
                    "Why do blind people hate skydiving? It scares the hell out of their dogs.",
                    "When you look really closely, all mirrors look like eyeballs.",
                    "My friend says to me: 'What rhymes with orange' I said: 'No it doesn't",
                    "What do you call a guy with a rubber toe? Roberto.",
                    "What did the pirate say when he turned 80 years old? Aye matey.",
                    "My wife told me I had to stop acting like a flamingo. So I had to put my foot down.",
                    "I couldn't figure out why the baseball kept getting larger. Then it hit me.",
                    "Why did the old man fall in the well? Because he couldn't see that well.",
                    "I ate a clock yesterday, it was very time consuming.",
                    "Whatdya call a frenchman wearing sandals? Phillipe Phillope.",
                    "A blind man walks into a bar. And a table. And a chair.",
                    "I know a lot of jokes about unemployed people but none of them work.",
                    "What's orange and sounds like a parrot? A carrot.",
                    "Did you hear about the italian chef that died? He pasta way.",
                    "Why couldn't the bicycle stand up? Because it was two tired!",
                    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                    "My wife accused me of being immature. I told her to get out of my fort.",
                    "Where do you find a cow with no legs? Right where you left it.",
                    "When a deaf person sees someone yawn do they think it’s a scream?",
                    "As I suspected, someone has been adding soil to my garden. The plot thickens.",
                    "How do crazy people go through the forest? They take the physco path.",
                    "Joke about traffic light changing",
                    "What did the traffic light say to the car? Don’t look! I’m about to change.",
                    "I just wrote a book on reverse psychology. Do *not* read it!",
                    "What did one hat say to the other? You stay here. I’ll go on ahead.",
                    "Why wouldn’t the shrimp share his treasure? Because he was a little shellfish.",

                    ]

# mention_replier_1 = MentionsRepr(value_holder_file='last_seen_id.txt', hash_tag='#FridayMotivation', custom_message_list=custom_joke_list)
#
# mention_replier_1.custom_replier()
#
# mention_replier_1.shoot_them_up()



