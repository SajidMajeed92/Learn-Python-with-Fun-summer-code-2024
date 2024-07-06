#  person dictionary
person = {
    'first_name':"Sajid",
    'last_name':"Majeed",
    'age':30,
    'gender':"Male",
    'skills':["python","Java","JS"]
}
print(person)
print(type(person))
print(person.keys())
print(person.values())
print(person['skills'])
# Adding a new key-value pair
person["address"] = "karachi"
print(person)
person['age']=28
print(person)
print(person.update({'age':26}))
print(person)
# Remove an item from dictionary
#print(person.pop('age'))
print(person)
print(person.popitem())
# Delete a dictionary
#del person
print(person)