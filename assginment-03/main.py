# 1, 2
try:
   a = 1 / 0
except ZeroDivisionError as ex:
   print("You divided by 0", ex.args)

# 3
"""
Is the following code legal?

try :
   x = 1
finally :
   print(“finally”)

Answer: Yes
"""

# 4
"""
What exception types can be caught by the
following handler?

Except:

Answer: All kinds of exceptions
"""

# 5
"""
What is wrong with using the above type of
exception handler?

Answer: 
   It's too generic. 
   most of the times we would like to act base of the error that  we got
"""

# 6
"""
What exceptions can be caught by the
following handlers?

...
except IOError
...
except ZeroDivisionError

Answer:
   IOError
   ZeroDivisionError
"""

# 7, 8, 9
with open("words.txt", "w+") as file:
   file.write("Ben")
   file.seek(0) # From StackOverflow: Important: return to the top of the file before reading, otherwise you'll just read an empty string
   content = file.readline()
   print("File content:", content)

# 10
with open("hebrew-file.txt", "w+") as hebrew_file:
   hebrew_file.write("שלום אחי")
   hebrew_file.seek(0)
   hebrew_content = hebrew_file.read()
   print("Hebrew File content:", hebrew_content)

