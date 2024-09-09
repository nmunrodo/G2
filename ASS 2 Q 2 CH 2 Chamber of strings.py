import string
import re
while (True):
    orig_string = input("""Please enter string of letters and numbers at least 16 characters long 
Special characters will be removed """)
    bad_char = [':', ';',',','.','/','?','!','@','#', '$', '%', '^', '&', '*', '(', ')', ]
    orig_string = ''.join(i for i in orig_string if not i in bad_char)
    if len(orig_string) < 16:
        print("Your string needs to be at least 16 characters long!")
    else:
        break;
 
alpha_list = [char for char in orig_string if char.isalpha()]
nmbr_list = [char for char in orig_string if char.isdigit()]

alpha = ','.join(alpha_list)
nmbr = ','.join(nmbr_list)

print()
print ("When seperated, and any special characters removed, alphabets and numerlas are:  ")
print()
print(alpha)
print("&")
print (nmbr)

ascii_num = []

for number in nmbr.split(','):
    if int(number) % 2 == 0 and int(number) > 0:
        ascii_num += (number)

ascii_alpha = list(filter(lambda char: char.isupper(), ''.join(alpha)))
 
print()
print ("Even numbers before ASCII conversion are:  ")
print("{}\"".format(ascii_num))
ascii_num_list = [ord(x) for x in ascii_num]
print()
print("Even numbers after ASCII conversion are:")
print (ascii_num_list)
print()
print ("Capital Letters before and after ASCII conversion are:")
print ("{}\"".format(ascii_alpha))
print()
ascii_alpha_list = [ord(x) for x in ascii_alpha]
print("And capital letters after ASCII conversion are:")
print (ascii_alpha_list)