# # Dictionary Methods: copy(), deepcopy(), update(), fromkeys(),
# # setdefault(), pop(), popitem()

# import copy

# # Original Dictionary
# student = {
#     "name": "Ishika",
#     "age": 19,
#     "marks": [90, 85, 88]
# }

# print("Original Dictionary:")
# print(student)

# # --------------------------------------------------
# # 1. copy() - Shallow Copy
# # --------------------------------------------------
# shallow_copy = student.copy()
# print("\n1. Shallow Copy:")
# print(shallow_copy)

# # --------------------------------------------------
# # 2. deepcopy() - Deep Copy
# # --------------------------------------------------
# deep_copy = copy.deepcopy(student)
# deep_copy["marks"][0] = 100

# print("\n2. Deep Copy:")
# print("Original:", student)
# print("Deep Copy:", deep_copy)

# # --------------------------------------------------
# # 3. update() - Update Dictionary
# # --------------------------------------------------
# student.update({"city": "Udaipur", "age": 20})

# print("\n3. After update():")
# print(student)

# # --------------------------------------------------
# # 4. fromkeys() - Create New Dictionary
# # --------------------------------------------------
# keys = ["id", "course", "semester"]
# new_dict = dict.fromkeys(keys, "Not Assigned")

# print("\n4. fromkeys():")
# print(new_dict)

# # --------------------------------------------------
# # 5. setdefault() - Add Key if Not Present
# # --------------------------------------------------
# student.setdefault("branch", "CSE")

# print("\n5. setdefault():")
# print(student)

# # --------------------------------------------------
# # 6. pop() - Remove Specific Key
# # --------------------------------------------------
# removed_age = student.pop("age")

# print("\n6. pop():")
# print("Removed Value =", removed_age)
# print(student)

# # --------------------------------------------------
# # 7. popitem() - Remove Last Item
# # --------------------------------------------------
# removed_item = student.popitem()

# print("\n7. popitem():")
# print("Removed Item =", removed_item)
# print(student)

# # --------------------------------------------------
# # Final Dictionary
# # --------------------------------------------------
# print("\nFinal Dictionary:")
# print(student)
    