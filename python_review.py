# Name: Matthew Jacobs
'''
print("It worked!")

x = None

example = "Im a string" # The variable called example is now holding the string value "Im a string".
a = 3 # The variable called a is now holding the integer value 3.
b = 4.0 # The variable called b is now holding the float value 4.0.
c = True # The variable called c is now holding the boolean value True.
d = False # The variable called d is now holding the boolean value False.
e = "Hey" # The variable called e is now holding the string value "Hey".
f = None # The variable called f is now holding the None value None.
age = 26 # The variable called age is now holding the integer value 26.
name = "Matthew" # The variable called name is now holding the string "Matthew".
instrument = "piano" # The variable called instrument is now holding the string value "piano".



'''


'''
prompt = "Enter your name: "

response = input(prompt)

print ("Hello", response)

print(response, " here is your agenda for the day...")

'''

'''
#Problem 1

name = "Enter your name: "
age = "Enter your age: "

response1 = input(name)
response2 = input(age)

print(name ,age ,type(response1), type(response2))
'''

'''
#Problem 2 
first_number = input ("Whats the first number?")
second_number = input("Whats the second number?")

first_number = int(first_number)
second_number = int(second_number)

if first_number > second_number:
    print(first_number, "is bigger")
elif first_number == second_number:
    print("The Numbers are equal")
else :
    print  (second_number, "is bigger")
'''

'''
#Problem 5
name = input ("Whats your full name? ")
length_of_name = len(name)


while " " in name: 
    name = name.replace(" ", "")

length_of_name = len(name)

print(length_of_name)
'''




