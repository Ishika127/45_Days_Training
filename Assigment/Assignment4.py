
# Question  1:
n = int(input("Enter number of elements: "))

numbers = []

# Input list elements
for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

print("\nPrime Numbers are:")

# Check each number
for num in numbers:

    if num < 2:
        continue

    prime = True

    # Check divisibility
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
#Question 2

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()


# ------------------------------------------
# Question  3: 
# ------------------------------------------

def calculate(numbers):

    even_count = 0
    odd_sum = 0

    for num in numbers:

        if num % 2 == 0:
            even_count += 1
        else:
            odd_sum += num

    return even_count, odd_sum


n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

even, odd = calculate(lst)

print("Count of Even Numbers =", even)
print("Sum of Odd Numbers =", odd)


# ------------------------------------------
# Question 4:
# ------------------------------------------

def simple_interest(principal, rate=10, time=1):

    si = (principal * rate * time) / 100

    return si


print("Using Positional Arguments")

print("Simple Interest =", simple_interest(10000))

print()

print("Using Keyword Arguments")

print("Simple Interest =", simple_interest(principal=5000, rate=12, time=3))



# ------------------------------------------
# Question  5:
# ------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A+"

        elif self.marks >= 80:
            return "A"

        elif self.marks >= 70:
            return "B+"

        elif self.marks >= 60:
            return "B"

        elif self.marks >= 50:
            return "C"

        else:
            return "Fail"


# ------------------------------------------
# Question  6: Create Objects
# ------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A+"

        elif self.marks >= 80:
            return "A"

        elif self.marks >= 70:
            return "B+"

        elif self.marks >= 60:
            return "B"

        elif self.marks >= 50:
            return "C"

        else:
            return "Fail"


student1 = Student("ABC", 88)
student2 = Student("Rahul", 65)

print("Student 1")
print("Name :", student1.name)
print("Marks :", student1.marks)
print("Grade :", student1.grade())

print()

print("Student 2")
print("Name :", student2.name)
print("Marks :", student2.marks)
print("Grade :", student2.grade())

# ------------------------------------------
# Question  7: 
# ------------------------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited Successfully.")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")

    def show_balance(self):
        print("Balance =", self.__balance)


account = BankAccount(10000)

account.deposit(5000)

account.withdraw(3000)

account.show_balance()

# ------------------------------------------
# Question  8: 
# ------------------------------------------

try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = num1 / num2

    print("Division =", result)

except ZeroDivisionError:
    print("Error: Division by Zero is Not Allowed.")

except ValueError:
    print("Error: Invalid Input! Please Enter Numbers Only.")

# ------------------------------------------
# Question 9:
# ------------------------------------------

# Open file in write mode
file = open("student.txt", "w")

name = input("Enter Student Name: ")
marks = input("Enter Student Marks: ")

file.write("Student Name : " + name + "\n")
file.write("Marks : " + marks)

file.close()

print("\nData Written Successfully.\n")

# Read File
file = open("student.txt", "r")

print("File Content:\n")
print(file.read())

file.close()


# Question 10:
try:
    file = open("numbers.txt", "r")

    total = 0
    count = 0

    for line in file:
        number = int(line)

        total += number
        count += 1

    average = total / count

    print("Total =", total)
    print("Average =", average)

    file.close()

except FileNotFoundError:
    print("Error: File Does Not Exist.")