import time
from random import randint
print("uncommenting the following line follows everyone in the csv")

t = randint(5, 60)
time.sleep(t)

print(f'sleeping time {t}')

test_list = sorted(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])

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

