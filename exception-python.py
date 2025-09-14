# try and except is a form of error handling in python 
# if there is an error in the try block whatever is in the except block will 
# if the try block has no errors it runs fine 
# example here , there is an error in the try block since x is not defined it's supposed to be printing i, so the except block will be executed and not the try 
try : 
    for i in range(10):
        print(x)
except:
    print("there is an error in your code") 


# there are 2 types of erros in python 
# syntax errors(problem with syntax like forgetting to indent) and logical erros (like dividing by 0)
# ex: FileNotFoundError, IndexError, e.t.c 
try : 
    numerator = int(input("enter your neunmenator"))
    denominator = int(input("enter your denominator")) # here the syntax of this code is absolutely fine, however if denominator = 0 the logic is invalid
    res = numerator/denominator
    print(res) 

except:
    print("you can't divide by 0, please try again")
    # if the donminator = 0 a error will occur so the except block will run istead of the try 
      

# also important to note we can specify the type of error after the except keyword, here is an ex:
#except ZeroDivisionError:
    # this will handle zero division errors only 


# moving onto the last part 
# the finally block, is a block that will always be executed no matter what 
try : 
    print(1/0)
except:
    print("wrong denominator")

finally:
    print("prints no matter what") 
    # whether the try block or the except block were the ones working the finally block will always run no matter what 
    # it will run with either the try block or the except block, and it will certainly run 



