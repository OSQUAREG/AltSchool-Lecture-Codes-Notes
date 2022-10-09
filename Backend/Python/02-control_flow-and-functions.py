# # # CONTROL FLOW

# There are 3 types of control flow statments:
# Conditional Statements
# Iterative Statements
# Transfer Statments


# # CONDITIONAL STATEMENTS
# - acts depending on the validity of a statmenet, whether a statement is True or False. They can be:
# IF statements
# IF-ELSE statements
# IF-ELIF-ELSE statements
# Nested IF-ELSE statements


# # IF STATEMENTS
# IF Statements Syntax
# if condition:
#     Statement_1
#     Statement_2
#     Statement_3...
# Statement

# # Example 1:
# num = int(input('Enter any number: '))

# if (num%5==0):
#     print(f'Given number {num} is divisible by 5')
#     print('This statement belong to the if statement')
# print('This statement does not belong to if statement')

# # Example 2:
# a = 30
# b = 20

# if b > a:
#     print('b is greater than a')
# print('this is false')


# # IF-ELSE STATEMENT
# IF-ELSE Statements Syntax
# if condition:
#     Statement_1
#     Statement_2
# else:
#     Statement_3
#     Statement_4...

# # Example 1:
# a = 20
# b = 30

# if b > a:
#     print('b is greater than a')
# else:
#     print('this is false')

# # Example 2:
# # Check if a number is Even number or not
# num = int(input('Enter any number: '))

# if num % 2 == 0:
#     print(f'The number {num} is an Even number')
# else:
#     print(f'The number {num} is an Odd number')


# # IF-ELIF-ELSE STATEMENT
# IF-ELIF-ELSE Statements Syntax
# if condition_1:
#     Statement_1
#     Statement_2...
# elif condition_2:
#     Statement_3
#     Statement_4...
# else:
#     Statement_5
#     Statement_6...

# # Example 1:
# a = int(input('Enter any First number: '))
# b = int(input('Enter any Second number: '))

# if b > a:
#     print(f'{b} is greater than {a}')
# elif b < a:
#     print(f'{b} is less than {a}')
# elif b == a:
#     print(f'{b} is equal to {a}')
# else:
#     print('Nothing will happen')


# # NESTED IFS STATEMENT
# NESTED IFS Statements Syntax
# if condition_1:
#     if condition_2:...
#         Statement_1
#         Statement_2...
#     else:
#         Statement_3
#         Statement_4...
# else:
#     if condition_3:
#         Statement_5
#         Statement_6...
#     else:
#         Statement_7
#         Statement_8...
# Statement

# # Example 1:
# x = int(input('Enter any First number: '))
# y = int(input('Enter any Second number: '))
# z = int(input('Enter any Third number: '))

# if y > x:
#     if z > y:
#         print(z, 'is greater')
#     else:
#         print(y, 'is greater')
# else:
#     if z > x:
#         print(z, 'is greater')
#     else:
#         print(x, 'is greater')
# print("Done")

# # ITERATIVE STATEMENTS
# these are statements that allow us to execute a block of code repeatedly given that the condition is True. Also known as LOOP Statments.

# For example, instead of printing the list 'a' elements one after the other like this...

# a = [1,2,3,4,5,10]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# ...one loop statement can print them all at once. IN python, there are 2 types of Loops:
# For Loop
# While Loop


# # FOR LOOPS

# # Example 1: Simple For Loop
# for i in a:
#     print(i)

# # Example 2: Nested For Loop
# a = ['red', 'big', 'small']
# fruits = ['banana','apple','cherry']

# for x in a:
#     for y in fruits:
#         print(x, y)

# # Example 3: For Loop and Range Object
# for i in range(6):
#     print(i)
# else:
#     print("Finally finished")


# # WHILE LOOPS

# # Example 1:
# count = int(input('How many times do you want to say "Hello": '))
# i = 1

# while i <= count:
#     print('Hello')
#     i += 1
# print('Job is Done! Thank You!')


# # # TRANSFER STATEMENTS

# These are ways to alter the execution of the program in a certain way. In python, there are 3 types:

# Break - used inside a loop to exit the loop.
# Continue - used inside a loop to skip the current iteration and move to the next iteration.
# Pass - used to do nothing in a function or in a loop.

# # Example 1: Break and For Loop statements
# fruits = ['banana', 'orange', 'apple', 'cherry', 'mango']
# for x in fruits:
#     if x == 'apple':
#         break
#     print(x)
# print("...above shows result for 'Break and For Loop statements'")

# # Example 2: Continue and For Loop statments
# for x in fruits:
#     if x == 'apple':
#         continue
#     print(x)
# print("...above shows result for 'Continue and For Loop statements'")

# # Example 3: Pass and For Loop statments
# for x in fruits:
#     if x == 'apple':
#         pass
#     print(x)
# print("...above shows result for 'Pass and For Loop statements'")

# # While Loop, If and Transfer statments
i = 1

# Example 1: Print before the If & Break statement
# while i < 6:
#     print(i)
#     if i == 4:
#         break # breaks after printing 4
#     i += 1

# Example 2: Print after the If & Break statement
# while i < 6:
#     if i == 4:
#         break # breaks before printing 4
#     print(i)
#     i += 1


# # # FUNCTIONS

# # Function Syntax
# def name(arg1, arg2,... argN):
#     statements

# # Example 1:
# def my_function():
#     print("Hello From a function")

# my_function() #calling the function

# # Example 2:
# def name(fname):
#     print(f'My name is {fname}')

# name("Caleb") #calling the function

# # Example 3:
# def area_of_circle(PI=3.142, r=float(input("Enter the radius: "))):
#     PI=PI
#     r = r
#     area = round(PI * r**2,2)
#     print("The Area of the Circle is: ", area)

# area_of_circle()

# # Example 4:
# my_list = [1,'cat',0.5]
# print(my_list)

# def add_list(my_list):
#     my_list.append([1,'cat',0.5])
#     print("Value inside the Function: ", my_list)
#     return

# my_list = [10,20,30]
# add_list(my_list) #calling the function
# print("Value Outside the Function: ", my_list)

# def mul_five(x):
#     return 5 * x

# print(mul_five(5))
# print(mul_five(2))
# print(mul_five(4))
# print(mul_five(3))


# def test(k):
#     if (k > 0):
#         result = k + test(k-1)
#         print(result)
#     else:
#         result = 0
#     return result

# test(7)

# def greet(name):
#     print("Hello, "+ name + ". Good morning")

# greet('Caleb')

# def convert(text):
#     x = text.upper()
#     print(x)

# text = input('Enter a string: ')
# convert(text)

# def to_uppercase():
#     text = input('Enter a lowercase string: ')
#     uppercase = text.upper()
#     print(uppercase)

# to_uppercase()

# def count(val):
#     con=0
#     vov=0
#     for i in range(len(val)):
#         if val[i] in ['a','e','i','o','u']:
#             vov = vov+1
#         else:
#             con = con+1

#     print("The Count of Vowel is", vov)
#     print("The Count of Consonant is", con)


# x = input('Enter any word: ')
# count(x)

# # Function to count both vowels, consonants, spaces and symbols.
# def count(val):
#     con=0
#     vov=0
#     sym=0
#     spc=0
#     for i in range(len(val)):
#         if val[i] in ['a','e','i','o','u']:
#             vov = vov+1
#         elif val[i] in [',',"'",':',';','?','/','&','.']:
#             sym += 1
#         elif val[i] in [' ']:
#             spc += 1
#         else:
#             con = con+1

#     print(f"The Word/Sentence is '{val}'")
#     print("The Count of Vowel is", vov)
#     print("The Count of Consonant is", con)
#     print("The Count of Symbols is", sym)
#     print("The Count of Spaces is", spc)

# x = input('Enter any word or sentence: ')
# count(x)
