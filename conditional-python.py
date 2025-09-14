# if and else statements are known as control structures in python 
# they are very important and used for conditional comparsions 
# you know alot about them but analyze this following piece of code 


if 'hehe' in ['foo', 'bar', 'baz']:     # hehe is not found in the following array   
    print('Outer condition is true')   # so this line won't ouput    

    if 10 > 20:                           
        print('Inner condition 1')        
                                    #since the main if statement is not true all the nested if statemnents won't run even if they are true 
    print('Between inner conditions')     

    if 10 < 20:                           
        print('Inner condition 2')        

    print('End of outer condition')       
print('After outer condition')    # this is the only line that will run in this code


#IMPORTANT: 
# new rule I found out about : #since the main if statement is not true all the nested if statemnents won't run even if they are true 
# indentation of code is very important in python it's known as the offside rule 

# moving on 
# as you know in python there is else and if and you already know how to use them ex:
say_hi = True 
if say_hi == True :
    print("hi") # this line is ran 
else:
    print("don't say hi")

# as you know there is elif (else if) used when one else is not enough, example:
name = 'Joe'
if name == 'Fred':
     print('Hello Fred')
elif name == 'Xander':
     print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe') # this line is the one to run since name == 'Joe' 
elif name == 'Arnold':
     print('Hello Arnold')
else:
    print("I don't know who you are!")



# At most, one of the code blocks specified will be executed. If an else clause isn’t included, and all the conditions are false, then none of the blocks will be executed.


var =True 

if 'a' in 'bar':
    print('foo')
elif 'a' in 'ccc':
    print("This won't happen")  
elif var:
    print("This won't either") # even though var is True this line won't run because a is in bar which is the intial if statement


#not neccassrily used but good to know 
# you can write single if statements like this 
a = 2 
if a == 2 : print("a is equal to 2") # it works even though we didn't use identation however they need to be on the same line 

# it's however better to stick to the usual style 
if a == 2:
    print("a is equal to 2")

# python also supports another stlye known as conditional statements where you can write your code like this 
raining = True
print("Let's go to the", 'beach' if not raining else 'library')
# you write the if and else inside the print statement however still better to stick to the original one 

#here is another example of a conditional expression
a = 4 
b = 5 
m = a if a > b else b

# moving on , 
# in python a pass statement is like a skip in the while language 
# it just tells the program to do nothing, ex:
if True:
    pass  # does nothing but important because if it was empty it would give an error 

#another example 
x = 10

if x > 5:
    pass   # We want to do nothing for now, this line runs since 10 > 5
else:
    print("x is 5 or less")

# moving on to switch statements 
# a switch statment is Primarily performs equality checks against literal values (integers, characters, sometimes strings). It's a simple jump table based on direct value comparison.
# switch statemnts don't directly exist in python we instead have match statements, ex:
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday") # since day = 2 this the line that will output 
    case 3:
        print("Wednesday")
    case _: # this is the defualt case 
        print("Other day") # any day other than Mon,Tue,Wed 


#another example 
command = "start"

match command:
    case "start":
        print("Starting engine!")
    case "stop":
        print("Stopping engine!")
    case _:
        print("Unknown command.")






