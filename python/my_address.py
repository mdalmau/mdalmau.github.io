my_address = {
"first_name": "Michelle",
"last_name": "Dalmau",
"street": "3006 S. Olcott Blvd",
"city": "Bloomington",
"state": "Indiana",
"zip": "47401"
}

#print(my_address['first_name'] + " " + my_address['last_name'])
#print(my_address['street'])
#print(my_address['city'] + ", " + my_address['state'] + "  " + my_address['zip'])

#fruits = ['apple', 'kiwi','orange']
#for fruit in fruits:
#    print(fruit)

#results = []
#for item in fruits:
#    results.append(item)

#numbers =[1,2,3,4,5]
#results=[]
#for item in numbers:
#        results.append(item+5)
#  answer = [6, 7, 8, 9, 10]

#results = [item for item in numbers]

#short version of for item in numbers:results.append(item+5)
#results = [item + 5 for item in numbers]

#names = ['Brandon', 'Ethan', 'Tony']
#results = []

#for name in names:
#	results.append('Hi my name is ' + name)

#comprehensive version of the code snippet above
#results = ['Hi my name is ' + name for name in names]

#exercise
numbers = [1,2,3,4,5]
data = []
#for item in numbers:
#    data.append(item-10)
#print(data)

data = [item -10 for item in numbers]
print(data)
