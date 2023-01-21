#Please save your 5 functions to one .py file demark the question numbers and the question in a comment above it's respective function

#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    user_name = input("Please enter your username")
    print('hello'+user_name+'!')
                
  

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for i in range(100):
        if i%2 != 0:
            print(i, end='')
                
  

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    print(max(a_list))
  

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    def CheckLeap(Year):  
        if((Year % 400 == 0) or  
            (Year % 100 != 0) and  
            (Year % 4 == 0)):   
            print("Given Year is a leap Year");  
        else:  
            print ("Given Year is not a leap Year")              
  

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))