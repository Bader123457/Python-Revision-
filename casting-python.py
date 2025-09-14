# casting is the process of converting one data type to another one, like converting an integer into a string 

# There are two types of type conversion in Python:
#Implicit Conversion - automatic type conversion
#Explicit Conversion - manual type conversion

# here is an example of an implicit conversion :
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
print("Value:",new_number)
print("Data Type:",type(new_number))  


#Note:

#We get TypeError, if we try to add str and int. For example, '12' + 23. Python is not able to use Implicit Conversion in such conditions.
#Python has a solution for these types of situations which is known as Explicit Conversion.

#Explicit Type Conversion:
#In Explicit Type Conversion, users convert the data type of an object to required data type.
#We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.
#This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.
# ex:
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string) # right here 

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum)) 
