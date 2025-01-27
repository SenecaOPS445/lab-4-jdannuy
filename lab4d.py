#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

# Function to return the first five characters of a string
def first_five(s):
    return s[:5]

# Function to return the last seven characters of a string
def last_seven(s):
    return s[-7:]

# Function to return the middle two digits of a number
def middle_number(n):
    str_n = str(n)
    # Find the middle two characters
    if len(str_n) > 1:
        return str_n[1:3]
    return str_n  # In case the number has less than 2 digits

# Function to combine the first three characters of one string with the last three characters of another string
def first_three_last_three(s1, s2):
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))               # 'Hello'
    print(first_five(str2))               # 'Senec'
    print(last_seven(str1))               # 'World!!'
    print(last_seven(str2))               # 'College'
    print(middle_number(num1))            # '50'
    print(middle_number(num2))            # '.5'
    print(first_three_last_three(str1, str2))  # 'Helege'
    print(first_three_last_three(str2, str1))  # 'Send!!'
