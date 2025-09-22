# what are regular expression in python?
# a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation.

# regular expression are a module in python known as re 
# to use it:
import re 

pattern = re.compile("^[A-Z]+$") # here we created a pattern to recognize 
# what this means is that 
# ^ means the beginning  
# behind the [] is our wanted pattern 
# A-Z means all capital characters from A to Z 

# now to look for our pattern we do this 

print(pattern.search("Hello World")) 
print(pattern.search("HELLOWORLD"))
