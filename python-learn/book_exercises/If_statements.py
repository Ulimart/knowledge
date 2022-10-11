"""Ask for two numbers. If
the first one is larger
than the second, display
the second number first
and then the first
number, otherwise show
the first number first and
then the second.
"""
# num_1 = int(input("Add the first number "))
# num_2 = int(input("Add the second number "))
# if num_1 > num_2:
#     print(f"the second number is {num_2} and the first number is {num_1}")
# else:
#     print(f"the first number is {num_1} and the second number is {num_2}")

"""Ask the user to enter a
number that is under
20. If they enter a
number that is 20 or
more, display the
message “Too high”,
otherwise display
“Thank you”.
"""
# num = int(input("Add a number under 20 \n"))
# if num >= 20:
#     print("Too high")
# else:
#     print("Thank you")

"""
Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”.
"""
# num = int(input("Add a number between 10 and 20 \n"))
# if num >= 10 and num <= 20:
#     print("Thanks")
# else:
#     print("Incorrect answer")

"""Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.
"""
# colour = input("What is your favorite colour? ")
# if colour == "red" or colour == "RED" or colour == "Red":
#     print("I like red too!!")
# else:
#     print("I don lile " + colour + " I prefer red" )

"""
Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”
"""
# raining = str.lower(input("Is it raining? (yes/no) \n"))
# if raining == "yes":
#     windy = str.lower(input("Is it windy? (yes/no) \n"))
#     if windy == "yes":
#         print("It is too windy for an umbrella")
#     else:
#         print("Take an umbrela")
# else:
#     print("Enjoy your day")

"""
Ask the user’s age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trick-
or-Treating”.
"""
# age = int(input("What is your age? \n"))
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can lear to drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# else:
#     print("You can go Trick-or-Treating")

"""Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.
"""
# number = int(input("Write a number \n"))
# if number >= 10 and number <= 20:
#     print("Correct")
# elif number < 10:
#     print("To low")
# else: 
#     print("To high")

"""Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.
"""
data = int(input("Write 1, 2, or 3 \n"))
if data == 1:
    print("Thank you")
elif data == 2:
    print("Well done")
elif data == 3:
    print("Correct")
else: 
    print("Error message")