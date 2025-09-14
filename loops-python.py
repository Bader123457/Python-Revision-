# IMPORTANT NOTE: DON'T FORGET TO READ THE ARTICLES INSIDE ROADMAP.SH BECUASE THEY ARE VERY INFORMATIVE 


# what are the two types of loops in python?
# while and for 
# a while loop is used to execute a piece of code while a condition remains true 
# a for loop is used to iterate a given number of times, you can iterate over a range,string,array and more.  

# here is how to use while loops 
name_1 = input("enter name")
if name_1 == " ":
    print("enter your name again")
else :
    print(f"hi {name_1}")

# in this example the user will be told to enter a name once if they didn't enter a name , but what if they don't continously enter a name and we need to keep checking, here we use a while loop 
# with while loop 
name = input("please enter a name")
while name == "": # if the user doesn't enter a name 
    print("you didn't enter a name") 
    name = input("please enter a name") # both the lines under the while loop will keep outputing until he enters his name 
print(f"Hello {name}") # since this line is not intended in the loop it's not a part of it, instead it's the line that's executed when the while loop is broken 

# so to visulaise it 
# while condition is true :
    #execute the code 
# code that occurs when condition is broken 
 
# while loop example 2 
age = int(input("please enter age"))
while age < 0:
    print("this is not possible")
    age = int(input("please enter age"))

print(f"you are {age} years old")


# while loop example 3, with logical operators 
food = input("enter your favorite food")
while not food == "q": # while the user doesn't press q we remain inside the loop
    print("you like the food" + food)
    food = input("enter your favorite food")

print("you pressed q so you quitted")

#now moving onto for loops 
for x in range(1,11):
    print(x) # you already know how to use this and what it does 

# now let's count from 10 to 1 
for i in range(10,0,-1): # we start from 10 and the second paramter is number we want to end at -1 and the third paramter is what we go down by 
    print(i)
# another way to also do that is this:
for y in reversed(range(1,11)): # 1 to 11 for loop same as printing from 1 to 10 however the reversed function will output the numbers backwards which is what we want 
    print(y)

# we can also do this 
for z in range(1,11,2):# this will go from 1 to 2 but only up by 2 so the ouput will be : 1,3,5,7,9
    print(z)


# now this is very important iterating over strings and arrays and e.t.c 
name = 'BadreldinElsayed' 
for letter in name:
    print(letter) # this will print out every letter in name 


# moving on we have the break and continue keywords 
# they are both known as control statements 

# what continue does is that it skips the part of the loop it's ordered to skip and continues with the rest of the iteration, ex:

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# this will skip 3 , so the ouput is: 1,2,4,5

# now the break statement tells python to stop this loop entirely we are done 
# it exits the loop immediatelt and no further loop iterations occur, ex:
for num in range(1, 6):
    if num == 3:
        break
    print(num)
# the ouput here will just be :1,2
# break is triggered when num = 3 and loop is exited immediately 


#Quick Summary
#continue:
#Skips the state of current loop iteration
#Loop goes on
#break:
#Exits loop immediately
#Loop stops completely

# moving on to nested loops 
# a nested loop is a loop with an outer loop also known as 2D loops
#   outer loop:
#       inner loop 

# there are 4 possibilites of nested loops : while inside while, for inside for, while inside for, for inside while 
# example 1 : let's print the numbers 1 to 9, 3 times 
for a in range(3):
    for b in range(1,10):
        print(b)
# we do this instead of writing for b in range(1,10) 3 times 
# important rules about nested loops is that the code will execute as a multiplication of the times the outer and inner loop are executed 
# so in this example it executed 3 multiplied by 9 times which is 27 



# question chatgpt made me on nested loops, needed to try it 
matrix = [[1,2,3] ,
          [4,5,6] ]
sum = 0 
pointer = 0 
for arr in matrix:
    for element in arr:
        while pointer < len(matrix):
            sum = sum + element 
            pointer = pointer + 1 
print(sum) 



# this was added later on 
# a great analogy to understand how nested loops work:
names = ["b","i","a","o","m"] 
for i in range(len(names)):
    for j in range(i+1,len(names)):
        pass 
# let's say badr want to shake hands with the rest of his friends he will be index i, i remains at badr while j full runs through ishtiaque,abdelbasit,omar,muhammed
# then it see if badr shook hands with them 
# then it moves to ishtiaque and checks if he shook hands with abdelbasit,omar,muhammed
# so the outer loop starts first and lets the nested loop fully run then the outer loop moves once and then the nested loop fully runs again 

