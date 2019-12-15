import time
from random import randint
import TestClass as tc
import globals as gls
import logging
import csv
import tweepy

print("this  module is for testing out scripts and methods and stuff")

def batch_delete(api):
    print(
        "You are about to Delete all tweets from the account @%s." % api.verify_credentials().screen_name)

    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print("Deleted:", status.id)
        except:
            print("Failed to delete:", status.id)


#batch_delete(api)

custom_hashtag_list = []

with open("/home/m/tweet.txt","r") as f:
    index = 0
    for single_line in f:
        print(single_line)
        index += 1
        if index % 2 != 0:
            hashtag = single_line.split("\t")[1]
            custom_hashtag_list.append(hashtag)

for ht in custom_hashtag_list:
    print(f'"{ht.rstrip()}",')

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

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

            custom_joke_list.append(col_0)
            custom_thnx_list.append(col_1)
            custom_facts_list.append(col_2)
except IOError:
    print("problem reading the csv")
finally:
    print(f'jokes list length: {len(custom_joke_list)}')
    print(f'thanx list length: {len(custom_thnx_list)}')
    print(f'facts list length: {len(custom_facts_list)}')

    for single_joke in custom_joke_list:
        print(single_joke)


print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

age_list = sorted(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"])

obj1 = tc.ThrowAwayClass(age_list=age_list, country_list=None, gender_list=None)

obj1.print_info()


gls.log_file_writer()
try:
    obj1.print_random_num(random_hashtag=gls.random_hashtag())
except Exception as e:
    print("error is ", e)
    logging.error('Error occurred ' + str(e))


t = randint(1, 3)
time.sleep(t)

print(f'sleeping time {t}')
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
obj1.print_info()




test_list = sorted(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"])

while 1:
    try:
        for index in range(len(test_list)):
            print(test_list)
            del (test_list[index])

            if index == 5:
                break

    except Exception as e:
        print("problem messaging follower list ", e)
    finally:
        if len(test_list) == 0:
            break

