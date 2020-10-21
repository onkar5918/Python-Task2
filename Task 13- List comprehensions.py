#Disply Duplicates using normal method
my_list = ['a','b','c','d','b','m','n','n']
duplicate = []
for count in my_list:
  if my_list.count(count) >1:
      if count not in duplicate:
           duplicate.append(count)

print(my_list)
print(f"Duplicates values are :{duplicate}")
#Display duplicates using list comprehensions
duplicates = list(set([char for char in my_list if my_list.count(char)>1]))

print(f"Duplicates values are :{duplicates}")