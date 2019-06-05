## Exercise Spellings

# store  the data
words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
canonical_spellings = ['color','amuck','adviser','pepper']

#make dictionary for the correct spelling
mappings = {'colour':'color','amok':'amuck','advisor':'adviser'}

#make an empty list
new_list = []

#loop over words
for word in words:
    # check to see if word is misspelled
    if word in mappings:
        # if word is misspelled don't something
        correct_word = mappings[word]
            # correct  Spelling using mappings dictionary
            # use name of key when checking a dictionary
        new_list.append(correct_word)
            # add to list
    else:
        # if a word is correct we will do something else
        new_list.append(word)
print(new_list)

##  Exercise COLLECTIONS
# step 1: create the collections
#texts = {
#"Jane Eyre":"1847",
#"Antes que anochezca":"1992"
#}

# use the items method for dictionaries to create an order
# need to "name" the key:value pair so title and date (could be any words)
#for title, date in texts.items():
#    print(title + " was published in " + date + ".")


##  METHOD that calls another METHOD
#def method_one():
#    print("look I'm a method")

#def method_two(name):
#    print("about to call our first method for " + name)
#    method_one()
#method_two("Michelle")

#def love():
#    print("I love them!")

#def family(name):
#    print("Let me introduce my family: " + name)
#    love()
#names = ["Mia, my daughter", "Jude, my son","Patrick, my son","Olivia, my daughter","Hugo, my dog","John, my partner"]
#for name in names:
#    family(name)





##  METHODS exercises
#def add(x,y):   #def creates the method; add is the name of the method
#    print(x+y)
#number = 4      #set variable
#add(500, number)

#def hello(name):
#    print("Hi my name is " + name)
#hello("Michelle")
#names = ["Mia", "Jude","Patrick","Olivia","Hugo","Sexy Daddy"]
#for name in names:
#    hello(name)

##  Dictionary exercises

#my_address = {
#"first_name": "Michelle",
#"last_name": "Dalmau",
#"street": "3006 S. Olcott Blvd",
#"city": "Bloomington",
#"state": "Indiana",
#"zip": "47401"
#}

#print(my_address['first_name'] + " " + my_address['last_name'])
#print(my_address['street'])
#print(my_address['city'] + ", " + my_address['state'] + "  " + my_address['zip'])

##    LOOPS exercises

#fruits = ['apple', 'kiwi','orange']
#for fruit in fruits:
#    print(fruit)
#if fruits[0] == "orange":
#        print("Yum!")
#elif fruits[0] == "kiwi" or fruits[0] == "apple":
#    print("Meh")
#else:
#    print("Not bad.")

#age = 1
#if age > 0 and age <=  2:
#    print("baby")
#elif age > 2 and age < 18:
#    print("child")
#else:
#    print("adult")

#counter = 0
#while counter < 5:
#    print(counter)
#    counter += 1
#ctrl + c ends a loop

##           SLICE Exercises
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#print(alphabet[2:7]) #range of characters
#print(alphabet[-2:]) #last two characters in the string



##  COMPREHNSION exercises
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
#numbers = [1,2,3,4,5]
#data = []
#for item in numbers:
#    data.append(item-10)
#print(data)

#data = [item -10 for item in numbers]
#print(data)

#exercise places
# make a list
#vacation = ["Cuba", "Hungary", "Japan", "London"]
# go oever each item in the list
#for place in vacation:
    #print  each place in the list
#    print("I would like to visit " + place  + ".")
