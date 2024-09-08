import string
import re
orig_string= input("Please enter string of letters and numbers at least 16 characters long  ")
alpha_list = [char for char in orig_string if char.isalpha()]
nmbr_list = [char for char in orig_string if char.isdigit()]

alpha = ','.join(alpha_list)
nmbr = ','.join(nmbr_list)

print ("When seperated, alphabets and numerlas are:  ")
print(alpha)
print (nmbr)

ascii_num = []

for number in nmbr.split(','):
    if int(number) % 2 == 0 and int(number) > 0:
        ascii_num += (number)

ascii_alpha = list(filter(lambda char: char.isupper(), ''.join(alpha)))
 

print ("Even numbers before and after ASCII conversion are:  \"{}\"".format(ascii_num))

ascii_num_list = [ord(x) for x in ascii_num]

print (ascii_num_list)

print ("Capital Letters before and after ASCII conversion are:  \"{}\"".format(ascii_alpha))
ascii_alpha_list = [ord(x) for x in ascii_alpha]
print (ascii_alpha_list)
