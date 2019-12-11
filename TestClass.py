
class ThrowAwayClass:
    def __init__(self, age_list, country_list, gender_list):
        self.age_list, = age_list,
        self.country_list, = country_list,
        self.gender_list, = gender_list,

    def print_random_num(self, random_hashtag):
        print("random hashtag== ",random_hashtag)
        pass

    def print_info(self):

        try:
            for i in range(len(self.age_list)):
                print(self.age_list)
                print(f'loop number {i+1}')
                del(self.age_list[i])

                if i == 3:
                    break

        except Exception as e:
            print("the problem is: ", e)

        finally:
            pass

        print("len of tweet list ", len(self.age_list))
