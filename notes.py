"""

# def is the keyword to name a function
# whatType is the name of the function
# userInput is the parameter of the function

def whatType(userInput):
    # print is a Python built-in function that prints to the console
    # type is a Python biult-in function that finds the datatype
    # userInput is the variable that the user enters
    print(type(userInput))


whatType(3)
whatType(True)
whatType("aurora")
whatType("p")
whatType(3.0)


print(4200)
print(42, "aurora", 3, "compsci", "computer")
print(42,000)

name = "aurora"
newName = "rora"
name = newName
newName = name

print(name)

# MLS formatting for geeks
# Global variable for things that cannot change

print(2 + 2)
print("hello")
print(len("hello"))

hour = 2
print(hour - 1)
print(hour * 60, "minutes in ", hour, " hours")

myName = "aurora"
print(myName * 5)

print(10/3) # 3.333333
print(10//3) # 3
print(10 % 3) # 1

print(8 * 2) #16
print(8 ** 2) #64

print(int(3.14))
print(int(1977))
print(int("1977"))
print(float(1977))
print(float(3.1415))

age = 17
print(type(age))
age = float(age)
print(type(age))

studentNames = ["Megan", "Anna", "Aurora", "Poly"]
emailAddress = "@ursulineacademy.org"
for student in studentNames:
    email = student + emailAddress
    print(email)

userName = input("what is your name? ")
userAddress = input("what is your address? ")
userCity = input("what city do you live in? ")
userZip = input("what is your zip code? ")

print(userName, userAddress, userCity, userZip)

"""
"""
circleRadius = input("what is the radius? ")
circleRadius = float(circleRadius)
circleArea = 3.14 * circleRadius * circleRadius
print(circleArea)

"""

yearsT = float(input("how many years is the money in the bank? "))
principalAmount = float(input("how much money do you have? "))
numberCompounds = float(input("how many times a year is your money compounded? "))
interestRate = float(input("what is the interest rate on this? "))
totalAmount = principalAmount * ((1.0 + (interestRate / numberCompounds))**(numberCompounds * yearsT))
print("after " + str(yearsT) + " years, you will have $" + str(int(totalAmount)) + " in the bank")
