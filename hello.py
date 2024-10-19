import sys # system functions and parameters
from datetime import datetime as dt #using an alias



#Importing - Importing is important





# Strings
print("Hello World")
print('Hello, world')
print("""This string runs
multiple lines!""") #triple quote for multi-line
print("This is a "+"string!") # we can concatenate strings
print('\n') # new line
print("Test the new line")


print('\n')

#Math
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 / 6) #division with a remainder
print(50 % 6) #modulo - takes what is left over
print(50 // 6) #no remainder - just integer

print('\n')

# Variables and methods
age = 35 #int
name = "Saga" #string
gpa = 3.3 #float

print(int(age))
print(int(35.1))
print(int(35.9)) 

quote = "All come on"
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

print("My name is " + name+" and I am " + str(age) + " years old.")

age +=1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')
# User input

#x = float(input("Give me a number: "))
#y = float(input("Give me another number: "))
#print(x + y)

#Functions

def who_am_i(name, age):
    print(f"My name is {name} and I am {age} years old")

who_am_i("Saga", 25)

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(5,9)

def multiply(x,y):
    return x * y

print(multiply(4,8))
print(multiply(7,6))

def square_root(x):
    print(x ** 0.5)

square_root(64)

def nl(): #new line
    print('\n')

nl()

#Boolean Expressions

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = 'True'
print(type(bool5))

nl()
#Relational and Boolean Operators

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
equals = 7 == 7
not_equals = 7 != 8

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True
test_not = not True #False

nl()
# Conditional Statements - if/else

def drink(money):
    if money >= 2:
        return "You can buy a drink"
    else:
        return "You cannot buy it"

print(drink(3))
print(drink(1))

def shubat(day, money): # day = shubattyn ashu uakyty
    if (day >= 7) and (money >= 1000):
        return "You got a sour shubat"
    elif (day >= 3 and day < 7) and (money >= 1000):
        return "You got a good shubat"
    elif (day < 3) and (money >= 1000):
        return "You got a normal shubat"
    else:
        return "You don't have enough money for shubat"

print(shubat(7, 1000))

nl()
#For loops 
vegetables = ["tomato", "potato", "carrot"]
for veggies in vegetables:
    print(veggies)

for i in range(5):
    print(i)

word = "Python"
for letter in word:
    print(letter)

# While loop - execute as long as True
i = 1

while i < 10:
    print(i)
    i += 1

'''
password = ""

while password != "spaghetti":
    password = input("Enter the secret password: ")

print("Access granted!")

'''
nl()
# Building a calculator

'''
x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me another number: "))

if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "/":
    print(x / y)
elif o == "*":
    print(x * y)
elif o == "**" or o == "^":
    print(x ** y)
else:
    print("Unknown operator")
'''

# Lists - brackets [] - inside is called an item

movies = ["Gran Turismo", "Fast and Furious", "Taxi", "NFS"]

print(movies[0]) #index
print(movies[1:3]) #returns the 1st number given until right before the last given number
print(movies[1:4]) #returns 1-3
print(movies[1:]) #return 1-end
print(movies[:1]) #everything before one
print(movies[:2]) # 0 and 1 index
print(movies[-1]) #last iem

print(len(movies)) #counts the items in the list
movies.append("Ford vs Ferrari") #adds an item to the end of list
print(movies)

movies.insert(2, "Transporter")
print(movies)

movies.pop() #removes the last item
print(movies)

movies.pop(0) #removes the first item
print(movies)

movies2 = ['Jackie Chan', 'Jet Li']
fav_movies = movies + movies2 #combined lists
print(fav_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jack", 70]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 94
print(grades)

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[1][2])

#Tuples - Immutable (can't be changed) - ()
coordinates = (40.7563, 35.0456) #some place
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
student = ("Saga", 345332, "Cybersecurity")

print(student[1])

nl()
# Dictionaries - key/value pairs {}

drinks = {"Water": 3, "Apple juice": 5, "Cola": 7} #drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Jerry", "Sarah"], "IT": ["Sake", "Aleke", "Eleke"], "HR": ["Alex", "Kolya"]}
print(employees)
employees['Legal'] = ["Scott"] #add a new key/value pair
print(employees)

employees.update({"Sales": ["Asan", "Bake"]}) #add a new key/value pair
print(employees)

drinks['Water'] = 2
print(drinks)

print(drinks.get("Apple juice"))

nl()
#Advanced Strings

my_name = "Saga"
print(my_name[0]) #1st letter
print(my_name[-1]) #last letter

sentence = "192.168.45.64"
print(sentence[:4])

print(sentence.split('.')) #delimiter - default is a space

sentence_split = sentence.split('.')
sentence_join = '.'.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "           hello     "
print(too_much_space.strip())

print("A" in "Apple") #return True
print("a" in "Apple") #return False - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved
'''
user_input = input("Enter yes or no: ")
if user_input.lower().strip() == "yes":
    print("You agree")
else:
    print("You disagree")
'''

movie = "Avengers"
print("My favourite movie is {}.".format(movie))
print("My favourite movie is %s." % movie)
print(f"My favourite movie is {movie}.")

print(sys.version)
print(dt.now())

