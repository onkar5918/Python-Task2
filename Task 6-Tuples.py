#Add and remove items from tuple using work around
tup1=(1,2,3,4,5,6,7,8,9,10)
print(tup1)
li1=list(tup1)      #convert the tuple into list to add the values
li1.append(11)
print(li1)
tup1=tuple(li1)     #convert the list into tuple after adding the value
print(tup1)
li1=list(tup1)      #Converting to list to remove the value
li1.remove(11)
print(li1)
tup1=tuple(li1)     #Converting to tuple to after removing the value
print(tup1)