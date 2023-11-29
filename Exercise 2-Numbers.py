# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:11:09 2023

@author: xahil
"""


# FUNCTIONS and VARIABLEs
def check_int(number):
    if number.isdigit() == True:        
        return True
    else:
        return False
def check_rango(number):
    if int(number) >= 10 and int(number) <= 20:
        return True
    else:
        return False

#   MAIN            
path = './Exercise 2-Numbers.txt'
with open(path,"r") as exercise_order:
    print(exercise_order.read())

checking = False
while checking == False:
    number = input('please, enter a number between 10 and 20: ')
    if check_int(number) == True:
        if check_rango(number) == True:
            checking = True
        else:
            print('the entire number is out of range')
    else:
        print('it is not an entire number')
        print('please enter a valid entire numer')


print(f'Integers between 1 and {number}')
for i in range(int(number)):
    print(i+1)

print(f'Integers between 30 and {number}, in reverse order')
for i in range(30,int(number)-1,-1):
    print(i)



