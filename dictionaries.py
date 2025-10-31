#A collection of key value pairs.
#represented using {}
#key-what are used to access values
#value-actual data being stored -attached to a key
# -accessed using keys.

#    **KEYS**
#-They are used to access values in a dictionary
#-They are immutable.
#-They are unique and cas sensitive
#----'name'&'Name'----->2 different keys
#----no duplicate keys------
#value pairs are comma separated
#'name':'Alice'

#-----**VALUES------
#1.can be accessed using a key
#can be accessed by any data type

#---------DICTIONARY OPERATIONS----------
#1.accessing values in dictionaries
#2.USE BRACKET NOTATION------>


person = {
    "name":"Hillary",
    "age":22,
    "email":'hillarymaina08@gmail.com',
    "married":False,
    "address":"123 Kimathi st",
    "friends":["John","Stephanie"],
    "occupation":"Software Developer"
}
print(person)
print(type(person))
#person=list(person)
print(person["name"])
print(person["age"])
print(person["address"])
print(person["friends"])
print(person["occupation"])

#<------ALTERNATIVE--------->
#USE GET METHOD
print(person.get("address"))
print(person.get("email"))
print(person.get("occupation"))
#DIFFERENCE BETWEEN THE TWO ABOVE
#ADD A NEW KEY VALUE PAIR
person['I.D']=40295617
person['dob']='25/06/2000'
print(person)

#REASIGNING VALUES
person["name"]="John"
print(person)

#UPDATING MULTIPLE KEYS----->.update({})
person.update({"name":"Alice",
               "age":45,
               "email":"alicewaruhio@gmail.com",
               "occupation":"Database Manager"
               })
print(person)
print("------------------")
#REMOVING ITEMS FROM A DICTIONARY
#-pop('key')-pass a key to remove a specific value
#-popitem()-remove the last inserted key
#-
#.keys()-returns all values in a list
#.items()-returns all values in a list
#FOR EXAMPLE
print("------------------")
person.pop('age')
print(person)

print("------------------")
person.popitem()
print(person)

#person.clear()
#print(person)

print(person.keys())
print(person.values())
print(person.items())

#TASK1 SETS AND TUPLES AGAIN IN SLIDE 40.FOLLOW THE TWO LINKS.
#SLIDE 43.
#COPY AND NESTED DICTIONARIES