# import str_utils as su
# user=input('Entere a name: ')
# print(su.vowels_count(user))


# import str_utils
# user=input('Entere a name: ')
# print(str_utils.vowels_count(user))

# from str_utils import *
# user=input('Enter a word? :')
# print(vowels_count(user))

from  error_handling  import *
score=input('Enter your score?: ')
divisor=input('What number do you wnat to divide with: ')
# try:
#     score=int(score)
#     divisor=int(divisor)
#     print(division(score,divisor))
# except ZeroDivisionError:
#     print('Use a number ')
# except ValueError:
#     print('Use a  number instead of a string')

# try:
#     score=int(score)
#     divisor=int(divisor)
#     print(division(score,divisor))
# except ZeroDivisionError:
#     print('Use a number ')
# except ValueError:
#     print('Use a  number instead of a string')
    
    
list = []

count = 0
while count < 5:
    number=input('Enter a value (number)')
    list.append(number)
    count+=1

for i in list:
    try:
        #type conversion
        converted_val=int(list[i])
        if converted_val < 0:
            print('negative value')
    except ValueError:
        print('Entered  a  string !!! expecting a number')
