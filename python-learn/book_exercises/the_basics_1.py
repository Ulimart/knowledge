"""Ask for the user’s first name and
display the output message
Hello [First Name] 
"""

# nombre = input("What is yor first name? ")
# print(nombre)

"""
Ask for the user’s first name and then ask for
their surname and display the output message
Hello [First Name] [Surname]
"""

# name = input("What is your first name? ")
# last_name = input("What is your lastname? ")
# print("Hello " + name + " " + last_name)

"""
Write code that will display the joke “What do you call a bear with no
teeth?” and on the next line display the answer “A gummy bear!” Try to
create it using only one line of code.
"""

#print("What do you call a bear with no teeth? " +  "\n A gummy bear!")

"""
Ask the user to enter two numbers. Add them together and display the answer as
The toal is [Answer]
"""

# num_1 = int(input("Add the first value: "))
# num_2 = int(input("Add the second value: "))
# sum = (num_1 + num_2)
# print("The total is: ", sum)

"""
Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as The answer is
[answer]
"""
# num_1 = int(input("Add the first number "))
# num_2 = int(input("Add the second number "))
# num_3 = int(input("Add the third number "))
# total = (num_1 + num_2) * num_3
# print("The answer is ", total)


"""Ask the user for their name and their age. Add 1 to their age
and display the output [Name] next birthday you
will be [new age] .
"""
# name = input("What is your name? ")
# age = int(input("What is your age? "))
# print(name + " next birthday you will be " + str(age + 1 ))

"""
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay.
"""
# bill = int(input("What is the bill? "))
# diners = int(input("How many diners there are? "))
# total = bill / diners
# print("The total that you have to pay is:", total)

"""
Write a program
that will ask for a
number of days
and then will
show how many
hours, minutes
and seconds are
in that number of
days.
"""
# days = int(input("How many days do you whant to convert "))
# hours = (days * 24)
# muninutes = (hours * 60)
# seconds = (muninutes * 60)
# print(f"You have {hours} hours and {muninutes} minutes and {seconds} seconds in that day")

"""There are 2,204 pounds in a kilogram. Ask the
user to enter a weight in kilograms and convert it
to pounds.
"""
# kilograms = int(input("how many kilograms do you what to convet to pounds? "))
# pounds = kilograms * 2.204
# print(f"There are {pounds} pounds in {kilograms} kilograms")

"""
Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the larger
number in a user-friendly format.
"""
larger = int(input("Enter a number over 100: "))
smaler = int(input("Enter a number under 10: "))
total = larger//smaler
print(f"{smaler} goes into {larger} {total} times")