dict1 = {
   "april_batch":{
      "student":{
         "name":"Mike",
         "marks":{
            "python":80,
            "maths":70
         }
      }
   }
}
# Access "Mike"
print(dict1['april_batch']['student']['name'])

# Access 80
print(dict1['april_batch']['student']['marks']['python'])

# change "Mike" to "Your name"
dict1['april_batch']['student']['name']="Onkar"
print(dict1['april_batch']['student']['name'])
print(dict1)

# add ML = 80 and DL = 80 inside marks
dict1['april_batch']['student']['marks']['ML']=80
dict1['april_batch']['student']['marks']['DL']=80

print(dict1)