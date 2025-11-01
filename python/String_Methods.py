#capitalize() =>	Converts the first character to upper case

name = "aravinth"
department = "MCA"

print(name.capitalize())

#casefold() =>	Converts string into lower case
"""The casefold() method returns a string where all the characters are lower case.
This method is similar to the lower() method, but the casefold() method is stronger,
 more aggressive, meaning that it will convert more characters into lower case, and will
   find more matches when comparing two strings and both are converted using the casefold() method."""
print(department.casefold())


#center() =>	Returns a centered string

"""
string.center(length, character) 

txt = "banana"

x = txt.center(20, "O")

print(x)

OOOOOOObananaOOOOOOO """


#count() =>	Returns the number of times a specified value occurs in a string

txt = "I love apples, apple are my favorite fruit"

y=txt.count("a")

print(y) #4 || string.count(value, start, end)