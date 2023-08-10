var1 = "Hello World!"
print(type(var1))
print('{} is a type of {}'.format(var1, type(var1)))

var1 = 10
print(type(var1))

var1 = 10.8
print(type(var1))

var1 = False
print(type(var1))


var1 = 12
print('Number is ' +str(var1))

num3 = 10+5j
print(type(num3))

print(2**5) #2 to the power 5

print(10/5) #Here answer will be floating point
print(10//5) #will give answer as int

#logical operators
num1 =10
num2 = 10.5
print((num1<num2) and ('ra' in 'Shradha'))
print((num1>num2) or ('aa' in 'Shradha'))

#Activity: 1
#Take agr of a person and tell them in which year they will turn 100

# name = input( "What is your name: " )
# age = int( input( "How old are you: " ) )
# year = str( ( 2020 - age ) + 100 )
# print( name + " will be 100 years old in the year " + year )


#Lists
fruits = ['apple','banana', 'cherry', 'mango']
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for i in range(-5,5,2):
    print(i)

for i in range(4):
    print(fruits[i])

#Activity2

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")


#Activity 3
#Rock Paper Scissors game. Take 2 user input and see which wins. Ask if user wants to play again.

#Get names of users
user1 = input("Enter name of Player1")
user2 = input("Enter name of Player2")

#While loop endlessly
while True:
    #Ask user 1's choice
    user1_answer = input(user1+ " do you want to choose rock, paper or scissor?").lower()

    #Ask user 2's choice
    user2_answer = input(user2+ " do you want to choose rock, paper or scissor?").lower()

    #Run the algorithm to see hwo wins
    if user1_answer == user2_answer:
        print("It's a tie")
    elif user1_answer == 'rock':
        if user2_answer == 'scissor':
            print("Rock wins!")
        else:
            print("Paper wins!")
    elif user1_answer == 'scissor':
        if user2_answer == 'paper':
            print("Scissor Wins!")
        else:
            print("Rock wins!")
    elif user1_answer == 'paper':
        if user2_answer == 'rock':
            print("Paper wins!")
        else:
            print("Scissor wins!")
    else:
        print("Invalid input provided")

    #Ask if user wants to repeat the game
    repeat = input("Do you want to play again? Answer yes/no").lower()

    #If user says yes, dont do anything
    if(repeat == 'yes'):
        pass
    #If they say no, exit the game
    elif(repeat == 'no'):
        raise SystemExit

    #If they say anything else, exit with error message
    else:
        print("You entered invalid option")
        raise SystemExit

#Activity4

# Get the names of the users
user1 = input("What is Player 1's name? ")
user2 = input("What is Player 2's name? ")

# While looping endlessly
while True:
    # Ask User1's choice
    user1_answer = input(user1 + ", do you want to choose rock, paper or scissors? ").lower()

    # Ask User2's choice
    user2_answer = input(user2 + ", do you want to choose rock, paper or scissors? ").lower()

    # Run the algorithm to see who wins
    if user1_answer == user2_answer:
        print("It's a tie!")
    elif user1_answer == 'rock':
        if user2_answer == 'scissors':
            print("Rock wins!")
        else:
            print("Paper wins!")
    elif user1_answer == 'scissors':
        if user2_answer == 'paper':
            print("Scissors win!")
        else:
            print("Rock wins!")
    elif user1_answer == 'paper':
        if user2_answer == 'rock':
            print("Paper wins!")
        else:
            print("Scissors win!")
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")

    # Ask them if they want to play again
    repeat = input("Do you want to play another round? Yes/No: ").lower()

    # If they say yes, don't do anything
    if(repeat == "yes"):
        pass
    # If they say no, exit the game
    elif(repeat == "no"):
        raise SystemExit
    # If they say anything else, exit with an error message.
    else:
        print("You entered an invalid option. Exiting now.")
        raise SystemExit

#Activity5

number = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
    print(number, ' x ', i, ' = ', number*i)

#Activity6
for i in range(10):
    print(str(i) * i)

#Activity7

numbers = list(input("Enter a sequence of comma separated values: ").split(", "))
sum = 0

for number in numbers:
    sum += int(number)

print(sum)

#Activity8

# Given list of numbers
numList = [10, 20, 30, 40, 10]
print("Given list is ", numList)

# Get first element in list
firstElement = numList[0]
# Get last element in list
lastElement = numList[-1]

# Check if first and last element are equal
if (firstElement == lastElement):
    print(True)
else:
    print(False)


#Activity9

# Given lists
listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

# Print the lists
print("First List ", listOne)
print("Second List ", listTwo)

# Declare a third list that will contain the result
thirdList = []

# Iterate through first list to get odd elements
for num in listOne:
    if (num % 2 != 0):
        thirdList.append(num)

# Iterate through first list to get even elements
for num in listTwo:
    if (num % 2 == 0):
        thirdList.append(num)

# Print result
print("result List is:")
print(thirdList)


#Activity10

# Given tuple
num_tuple = (10, 20, 33, 46, 55)
print("Given list is ", num_tuple)

# Print elements that are divisible by 5
print("Elements that are divisible by 5:")
for num in num_tuple:
    if (num % 5 == 0):
        print(num)

#Activity11

fruit_shop = {
    "apple": 10,
    "banana": 15,
    "orange": 8,
    "peaches": 15
}

key_to_check = input("What are you looking for? ").lower()

if(key_to_check in fruit_shop):
    print("Yes, this is available")
else:
    print("No, this is not available")



#Activity 12
def calculateSum(num):
    if num:
        #Recursive function call
        return num + calculateSum(num-1)
    else:
        return 0
res = calculateSum(10)
print("Sum is: ", res)

#Activity13

# Custom function to calculate sum
def calculate_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# Define the list of numbers
numList = [10, 40, 60, 90]

# Call the sum() function with numList as argument
result = calculate_sum(numList)

# Print result with message
print("The sum of all the elements is: " + str(result))

#Activity14

def fibonacci(number):
    if number <= 1:
        return number
    else:
        return(fibonacci(number-1) + fibonacci(number-2))

nterms = int(input("Enter a number: "))

if nterms <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Sequence: ")
    for i in range(nterms):
        print(fibonacci(i))

#Activity15

try:
    print(x)
except NameError:
    print("x hasn't been defined yet.")


#Activity16
class Car:
    'This class represents a car'

    def __init__(self, manufacturer, model, make, transmission, color):
        self.manufacturer = manufacturer
        self.model = model
        self.make = make
        self.transmission = transmission
        self.color = color

    def accelerate(self):
        print(self.manufacturer + " " + self.model + " has started moving")

    def stop(self):
        print(self.manufacturer + " " + self.model + " has stopped moving")

car1 = Car("Toyota", "Corolla", "2015", "Manual", "White")
car2 = Car("Maruti", "800", "2013", "Manual", "Red")
car3 = Car("Suzuki", "Swift", "2017", "Automatic", "Black")

car1.accelerate()
car1.stop()

#Activity17

# Import pandas
import pandas

# Create a Dictionary that will hold our data
data = {
    "Usernames": ["admin", "Charles", "Deku"],
    "Passwords": ["password", "Charl13", "AllMight"]
}

# Create a DataFrame using that data
dataframe = pandas.DataFrame(data)

# Print the DataFrame
print(dataframe)

"""
 Write the DataFrame to a CSV file
 To avoid writing the index numbers to the file as well
 the index property is set to false
"""
dataframe.to_csv("sample.csv", index=False)


#Activity18
# Import pandas
import pandas

# Read the CSV file and store it into a DataFrame
dataframe = pandas.read_csv("sample.csv")

# Print the full data
print("Full Data: ")
print(dataframe)

# Print the values in the Usernames column only
print("===============")
print("Usernames:")
print(dataframe["Usernames"])

# Print the username and password of the second row
print("===============")
print("Username: ", dataframe["Usernames"][1], " | ", "Password: ", dataframe["Passwords"][1])

#Sort the Usernames column in ascending order
print("====================================")
print("Data sorted in ascending Usernames:")
print(dataframe.sort_values('Usernames'))

#Sort the Passwords column in descending order
print("====================================")
print("Data sorted in descending Passwords:")
print(dataframe.sort_values('Passwords', ascending=False))


#Activity19

# Import pandas
import pandas
from pandas import ExcelWriter

# Create a dictionary that will be used to create the DataFrame
data = {
    'FirstName':["Satvik", "Avinash", "Lahri"],
    'LastName':["Shah", "Kati", "Rath"],
    'Email':["satshah@example.com", "avinashK@example.com", "lahri.rath@example.com"],
    'PhoneNumber':["4537829158", "4892184058", "4528727830"]
}

# Create the DataFrame that will be written to the excel file
dataframe = pandas.DataFrame(data)

# Print the dataframe
print(dataframe)

# Write the dataframe to a Excel file
writer = ExcelWriter('sample.xlsx')
dataframe.to_excel(writer, 'Sheet1', index = False)

# Commit data to the Excel file
writer.save()


#Activity20

# Import pandas
import pandas

# Read data from Excel sheet
dataframe = pandas.read_excel('sample.xlsx')

# Print the dataframe
print(dataframe)

# Print the number of rows and columns
print("====================================")
print("Number of rows and columns:", dataframe.shape)

# Print the data in the emails column only
print("====================================")
print("Emails:")
print(dataframe['Email'])

# Sort the data based on FirstName in ascending order and print the data
print("====================================")
print("Sorted data:")
print(dataframe.sort_values('FirstName'))


#Activity21

import pytest

# Additon test
def test_addition():

    # Initialize two numbers
    num1 = 10
    num2 = 15

    # Add them
    sum = num1 + num2

    # Assertion
    assert sum == 25

# Subtraction test
def test_subtraction():

    # Initialize two numbers
    num1 = 50
    num2 = 35

    # Subtract them
    diff = num1 - num2

    # Assertion
    assert diff == 15

# Multiplication test
def test_multiplication():

    # Initialize two numbers
    num1 = 5
    num2 = 20

    # Multiply them
    prod = num1 * num2

    # Assertion
    assert prod == 100

# Division test
def test_division():

    # Initialize two numbers
    num1 = 100
    num2 = 5

    # Divide them
    quot = num1 / num2

    # Assertion
    assert quot == 20


#Activity22

import pytest

# Additon test
def test_addition():

    # Initialize two numbers
    num1 = 10
    num2 = 15

    # Add them
    sum = num1 + num2

    # Assertion
    assert sum == 25

# Subtraction test
def test_subtraction():

    # Initialize two numbers
    num1 = 50
    num2 = 35

    # Subtract them
    diff = num1 - num2

    # Assertion
    assert diff == 15

# Multiplication test
@pytest.mark.activity
def test_multiplication():

    # Initialize two numbers
    num1 = 5
    num2 = 20

    # Multiply them
    prod = num1 * num2

    # Assertion
    assert prod == 100

# Division test
@pytest.mark.activity
def test_division():

    # Initialize two numbers
    num1 = 100
    num2 = 5

    # Divide them
    quot = num1 / num2

    # Assertion
    assert quot == 20


#Activity23

import pytest

# Create fixture
@pytest.fixture
def num_list():

    # Create list
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Alternatively
    # list = list(range(11))

    return list

# Write test method
def test_sum(num_list):

    # Initialize sum
    sum = 0

    # Add number in the list
    for n in num_list:
        sum += n

    # Assertion
    assert sum == 55


#Activity24

import pytest

# Define a fixture for the wallet amount
@pytest.fixture
def wallet_amount():
    amount = 0
    return amount

# Set up the paremeterized test method
@pytest.mark.parametrize("earned, spent, expected", [ (30, 10, 20), (20, 2, 18), ])
def test_transactions(wallet_amount, earned, spent, expected):

    # Add money to your wallet
    wallet_amount += earned

    # Subtract amount from wallet
    wallet_amount -= spent

    # Assertion
    assert wallet_amount == expected






