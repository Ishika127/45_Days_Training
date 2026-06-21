
class Student:
    name = "IShika"
    age = 18
    course = "BTech"

s2 = Student()

print("Name:", s2.name)
print("Age:", s2.age)
print("Course:", s2.course)
# Question 2

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

c1 = Car("Tata", "Punch", 800000)
c2 = Car("Honda", "City", 1200000)

print(c1.brand, c1.model, c1.price)
print(c2.brand, c2.model, c2.price)
# Question 3

class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

e2 = Employee(202, "Karan", 60000)

print(e2.employee_id)
print(e2.name)
print(e2.salary)
# Question 4

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area =", self.length * self.width)

r2 = Rectangle(12, 4)
r2.area()
# Question 5

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area =", 3.14 * self.radius * self.radius)

c2 = Circle(5)
c2.area()
# Question 6

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance =", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Balance =", self.balance)

b2 = BankAccount("Aman", 15000)

b2.deposit(3000)
b2.withdraw(2000)
# Question 7

class Animal:
    def sound(self):
        print("Animal Noise")

class Dog(Animal):
    def sound(self):
        print("Bark")

d2 = Dog()
d2.sound()
# Question 8

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

s2 = Student("Priya", 19, 25)

print(s2.name)
print(s2.age)
print(s2.roll_number)
# Question 9

class Calculator:
    def add(self, a, b):
        print("Add =", a + b)

    def subtract(self, a, b):
        print("Subtract =", a - b)

    def multiply(self, a, b):
        print("Multiply =", a * b)

    def divide(self, a, b):
        print("Divide =", a / b)

x = 30
y = 6

c2 = Calculator()

c2.add(x, y)
c2.subtract(x, y)
c2.multiply(x, y)
c2.divide(x, y)
# Question 10

class LibraryBook:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book_info(self):
        print(self.book_name, self.author, self.price)

b1 = LibraryBook("HTML", "Anil", 350)
b2 = LibraryBook("CSS", "Sunil", 300)
b3 = LibraryBook("JavaScript", "Kapil", 650)

b1.display_book_info()
b2.display_book_info()
b3.display_book_info()