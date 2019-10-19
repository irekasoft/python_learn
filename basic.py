# variables
character_name = "John"
character_age = "35"

# print to the console
print("Hello Phyton World")
print(character_name + " " + character_age)

# variable ( other data types )

number = 1
print("number", number)

is_male = True
print("bool", is_male)

# functions
def sayhi():
    print("hello")

def cube(num):
    return num*num*num

# call the functions

sayhi()

print(cube(3))

# If function

# I wake super
# If I'm hungry
#   I eat breakfast

is_hungry = False

if is_hungry:
    print('I eat breakfast')

# I leave my house
# if it's cloudy
#   If bring an umbrella
# otherwise
#   I bring sunglesses

is_cloudy = False

if is_cloudy:
    print("bring an umbrella")
else:
    print("bring sunglasses")

# I am at the restaurant
# if I want meat
#   I order a steak
# otherwise if I want pasta
#   I order spagetthi & meatballs
# otherwise
#   I order a salad

#

#num1 = float(input("Enter first number: "))
#print(num1)

monthConversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
}

print (monthConversion.get("Jan"))

# while condition

i = 1

while i <= 10:
    print(i)
    i = i + 1

for letter in "iReka Soft":
    print(letter)

# try catch

try:
    number = int(input("enter a number:"))
    print(number)
except ValueError:
    print("invalid input")

