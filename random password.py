# PRE-REQUISITE
# !pip install random2
# !pip install Arrays

import random 
import array 
  
# maximum length of password needed 
# this can be changed to suit your password length 
MAX_LEN = 12
  
# declare arrays of the character that we need in out password 
# Represented as chars to enable easy string concatenation 
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z'] 
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<&# 039;'] 
  

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

comb_string = ''.join(COMBINED_LIST)
#print(comb_string)

max_len = 9

p = "".join(random.sample(comb_string,9))
#print password of len 9
print(p)

# getting random lists of digits, characters, symbols
rand_digit = random.choice(DIGITS) 
rand_upper = random.choice(UPCASE_CHARACTERS) 
rand_lower = random.choice(LOCASE_CHARACTERS) 
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

# initializing an empty string to generate a password
password = "" 
for x in temp_pass: 
        password = password + x 
          
# print out password 
print(password) 
