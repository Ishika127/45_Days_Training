#Question 1 create a tuple 
my_tuple=(10,20,30,40,50)
print(my_tuple[0])
print(my_tuple[4])
print(my_tuple[1:4])

#Question 2 create a tuple 
fruits =("apple","banana","mango","orange")
print(fruits[2])
print(fruits[2:4])

#question 3 create a set 
numbers ={10,20,30,40,50}
print(numbers)
print(len(numbers))
if 30 in numbers:
    print("30 is present in the set  ")
else:
    print("30 is not present in the set  ")   
 #Question 4  create two sets 
set1 ={1,2,3,4}
set2={3,4,5,6}
print(set1|set2)
print(set1.union(set2))
print(set1&set2)
print(set1.intersection(set2))     

#question 5 create a dictionary 
student ={"name":"Kriti","age":20,"couse":"Python"}
print(student)
print(student.values())
print(student.keys())
print(student["age"])
print(student["name"])
print(student["couse"])

#
numbers = [12, 45, 7, 23, 56, 89, 34]

# Find Largest Element
largest = max(numbers)

# Find Second Largest Element
temp = sorted(numbers)
second_largest = temp[-2]

# Find Smallest Element
smallest = min(numbers)

print("Largest Element =", largest)
print("Second Largest Element =", second_largest)
print("Smallest Element =", smallest)

arr = [10, 20, 30, 40, 50, 60]

# Function to reverse a list without using reverse()

def reverse_list(lst):
    return lst[::-1]

print("Original List:", arr)
print("Reversed List:", reverse_list(arr))

data = (5, 10, 15, 20, 25, 30, 35)

# Count elements divisible by 5
count = 0

for i in data:
    if i % 5 == 0:
        count += 1

# Sum of all elements
total = sum(data)

# Average of tuple
average = total / len(data)

print("Count =", count)
print("Sum =", total)
print("Average =", average)

 #Create a dictionary 
students = {
    "Aman": 78,
    "Riya": 92,
    "Kriti": 88,
    "Rahul": 95
}
 
# Student with highest marks
highest = max(students, key=students.get)

# Student with lowest marks
lowest = min(students, key=students.get)

print("Highest Marks Student:")
print(highest, students[highest])

print("\nLowest Marks Student:")
print(lowest, students[lowest])

print("\nStudents Scoring More Than 85 Marks:")

for name, marks in students.items():
    if marks > 85:
        print(name, marks)

 #write a function 

def count_frequency(arr):

    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for key, value in freq.items():
        print(key, "->", value, "times")


arr = [1, 2, 2, 3, 1, 4, 2]

count_frequency(arr)

# Question 10 Write a function: find_duplicates(arr)
def find_duplicates(arr):

    duplicate = []

    for i in arr:
        if arr.count(i) > 1 and i not in duplicate:
            duplicate.append(i)

    print("Duplicate Elements Are:")

    for i in duplicate:
        print(i)


arr = [10, 20, 30, 20, 40, 10, 50, 30]

find_duplicates(arr)
