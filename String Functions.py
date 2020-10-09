str1="welcome to Python"
Str2='####Welcome  to  Python#####'
print(str1.casefold())      # Converts all letters to lowercase
print(str1.title())         #Converts the letters to Title case
print(str1.center(100,"-")) #Returns a centered string. Length param: mandatory, character param:Optional
print(str1.count("o"))      #Return the count of mentioend character in string.Start and stop parameter are optional
print(str1.find("to"))      #Return the Position of substring Start and stop parameters are optional
print(str1.index("to"))     #Return the Position of substring Start and stop parameters are optional
print(Str2.strip("#"))      #Remove the mentioned character from the start and end of string. Default character is blank space
print(Str2.lstrip("#"))     #Remove the mentioned character from start from string
print(Str2.rstrip("#"))     #Remove the mentioned character from end from string
print(str1.replace("Python","Data Science")) #Replace the specified phrase with new phrase