import time
from random import randint
import TestClass as tc

print("this  module is for testing out scripts and methods and stuff")

age_list = sorted(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"])

obj1 = tc.ThrowAwayClass(age_list=age_list, country_list=None, gender_list=None)

obj1.print_info()

t = randint(1, 6)
time.sleep(t)

print(f'sleeping time {t}')
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
obj1.print_info()


# test_list = sorted(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"])

# while 1:
#     try:
#         for index in range(len(test_list)):
#             print(test_list)
#             del (test_list[index])
#
#             if index == 5:
#                 break
#
#     except Exception as e:
#         print("problem messaging follower list ", e)
#     finally:
#         if len(test_list) == 0:
#             break

