# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:27:39 2024

@author: gaikw
"""

numerator=50
try:
    denominator=int(input("Enter denominator: "))
    result=numerator/denominator
    print(f"Division is {result}")
except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("Only integers should be entered")

###############################################################################
#Any error in general
numerator=50
try:
    denominator=int(input("Enter denominator: "))
    result=numerator/denominator
    print(f"Division is {result}")
    print("abc"+23)
except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("Only integers should be entered")
except:
    print("some error occured")

###############################################################################

#Exception with try, except and else blocks

numerator=50
try:
    denominator=int(input("Enter denominator: "))
    result=numerator/denominator
    print("Division performed successfully")
except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("Only integers should be entered")
else:
    print(f"Division is {result}")

###############################################################################

#Finally block

numerator=50
try:
    denominator=int(input("Enter denominator: "))
    result=numerator/denominator
    print("Division performed successfully")
except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("Only integers should be entered")
else:
    print(f"Division is {result}")
finally:
    print("OVER AND OUT")