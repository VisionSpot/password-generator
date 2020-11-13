import random

letters = ['a','A', 'b','B', 'c','C', 'd','D', 'e','E', 'f','F',
'g','G', 'h','H', 'i','I', 'j','J', 'k','K', 'l','L', 'm','M',
'n','N', 'o','O', 'p','P', 'q','Q', 'r','R', 's','S', 't','T',
'u','U', 'v', 'V', 'w','W', 'x','X', 'y','Y', 'z','Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

len_pass = input("how long would you like your password to be?(int number) :")

def list_to_string(lt):
    return ''.join([str(i) for i in lt])


if(len_pass.isdigit()):
    try:
        length_pass = int(len_pass) #addade morede ghabool
        if(length_pass <= 20) and (length_pass >= 4):
            count_of_num_in_pass = input("how many number you want?: ")
            count_of_let_in_pass = input("how many letters you want?: ")

            if (int(count_of_let_in_pass) + int(count_of_num_in_pass)) == length_pass:
                pick_rand_num = random.sample(numbers, int(count_of_num_in_pass))
                pick_rand_let = random.sample(letters, int(count_of_let_in_pass))
                
                for i in pick_rand_let:
                    pick_rand_num.append(i)

                final_lt = random.sample(pick_rand_num, len(pick_rand_num))
                print(list_to_string(final_lt))

            else:
                raise Exception("the sum of numbers and letters must be equl to your password length")

        else:
            print("len is wrong")

    except ValueError:
        print("That's not an integer!")

else:
    print("not an integer!")

