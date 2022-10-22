# # Try & Except Syntax
# try:
#     Your statement
# except Exception1:
#     Your Statement
# except Exception2:
#     Your Statement

# # Example 1 - Using a simple Try & Except block
# try:
#     a = 5
#     b = 'w'
#     print(a/b)
# except:
#     print('Some error Occured.')
# print('Done!')

# # Without the Try & Except block
# a = 5
# b = 'w'
# print(a/b)

# # Example 2 - Using multiple Error type
# try:
#     a = 5
#     b = '0'
#     print(a/b)
# except TypeError:
#     print('Unsupported Operation')
# except ZeroDivisionError:
#     print('Division by Zero not allowed')
# print('Done!')

'''
Exception: Base class for all exceptions

StopIteration: Raised when the next method of an iterator does not point to any object.

SystemExit: Raised by the sys.exit function.

StandardError: Base class for all built-in exceptions except StopIteration and SystemExit.

ArithmeticError: Base class for all errors that occur for numeric calculation.

OverflowError: Raised when a calculation exceeds maximum limit for a numeric type.

FloatingPointError: Raised when a floating point calculation fails.

ZeroDivisonError: Raised when division or module by zero takes place for all numeric types.

AssertionError: Raised in case of failure of the Assert statement.
'''
# # ValueError:
# try:
#     x = int(input('Enter a number up to 100: '))
#     if x > 100:
#         raise ValueError(x)
# except ValueError:
#     print(x, 'is out of allowed range')
# else:
#     print(x, 'is within the allowed range')


# # KeyError: A KeyError is raised when a value is not found as a key of a dictionary
# import sys
# try:
#     s = {'a':5,'b':7}['c']
# except:
#     print(sys.exc_info())


# # NameError: these are raised when your code refers to a name that does not exist in the current scope.
# import sys
# try:
#     def foo():
#         print(magnolia)
#     foo()
# except NameError as e:
#     print(e)
#     print(sys.exc_info())


# # SyntaxError: this occurs any time the parser finds source code it does not understand.
# import sys
# try:
#     print(eval("six times seven")) # eval() only evaluates numbers
# except SyntaxError as err:
#     print(err) # returns where the error is or explain
#     print('Syntax error found')
#     print(sys.exc_info()) # returns the type of error


# # StandardError: (also known as AttributeError)
# import sys
# try:
#     class Foobar:
#         def __init__(self):
#             self.p = 0
#     f = Foobar()
#     print(f.p)
#     print(f.q)
# except Exception as e:
#     print (e)
#     print (sys.exc_info())
#     print ('This is an example of StandardError exception')


# # FloatingPoinPROMPT_DIRTRIM=3tError: raised when the source code returns a float instead of an integer.
# import sys
# try:
#     b = 5
#     a = 3
#     c = a % b
#     print(c)
#     if c != 0:
#         raise FloatingPointError(c)
# except FloatingPointError as err:
#     print (err)
#     print (sys.exc_info())


# # IndentationError: occurs any time the parser finds source code that does not follow indentation rules.
# try:
#     def f():
#         z=['foo','bar']
#         for i in z:
#             if i == 'foo':
# except IndentationError as e:
#     print (e)


# # StopIteration: When an iterator is done, it’s next method raises StopIteration. This exception is not considered an error.
# import sys
# try:
#     z = [5, 9, 7]
#     i = iter(z) #iter() is used to iterate over a lst
#     print (i)
#     print (i.next())
#     print (i.next())
#     print (i.next())
#     print (i.next())
# except Exception as e:
#     print (e)
#     print (sys.exc_info())
