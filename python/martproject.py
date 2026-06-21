# Mart System - Save Data to File

file = open("mart_data.txt", "a")

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    quantity = input("Enter quantity: ")

    file.write(f"Product: {name}, Price: {price}, Quantity: {quantity}\n")

file.close()

print("Data saved successfully!")

# Read and display file data
file = open("mart_data.txt", "r")

print("\nSaved Products:")
print(file.read())

file.close()