                   #tuple  same like list but immutable 
a=(1,2,3,4,4,"ishika")  #tuple is created by using parenthesis
print(a)
print(type(a))
print(len(a)) #check the length of the tuple 
#no function to change the value of tuple because it is immutable
print(a.count(4))
print(a.index("ishika"))
print(a[3])#accesing the element of tuple by using indexing
b= 1,2,3,4,5,"hii","hello"# we can also create tuple without using parenthesis
print(b)
print(type(b))

x ,y ,z = (1,2,3) #unpacling of tuple
print(x)
print(y)
#print(z)

# print(3*4)
# a=4
# b=5
# print(a*b)
#how to convert tuple into list # typecasting
w=(1,2,3)
l=list(w)
print(l)
print(type(l))
y=(1,2,3)
v=(4,5,6)
#print(y*v) #we cannot perform multiplication on tuple but we can perform it on list
print(y*4)

#                     #set 
# c={2,3,4,5}
# print(c)
# print(type(c))
#                     #dic
# b={"Name ":"Ishika","age":20}
# print(b)
# print(type(b))
# print(b.keys())
# print(b.values())
# print(b["Name "]) #tp acess specific value we use it 
# b["age"]=22 # to update any value 
# print(b)
# # add key and value in dict 
# b["rollno"]=34
# print(b)
# b["city"]="loharu"
# print(b)
# b.update({"phone number":8926389212})# uppdate dict 
# print(b)
# print(b.values())
# print(b.items())
# print(b.get("age"))
# for keys , values in b.items():
#     print(keys,values)

# #nested dict 
# students = {
#     "student1": {
#         "name": "Ishika",
#         "age": 22,
#         "course": "Computer Science"
#     },
#     "student2": {
#         "name": "priya",
#         "age": 19,
#         "course": "Computer science"
#     }
# }

# print(students)
# print(students.items())

# Function
# def greet(names):
#     i = 0
#     while i < len(names):
#         print("Good Morning", names[i])
#         i = i + 1

# # List
# students = ["Ishika", "Priya", "prachi"]

# # Function call
# greet(students)

# x= lambda a:a*a # lambda is nameless (anonmyus )function
# print(x(5))

# i= lambda a,b,c:a+b+c
# print(i(9,8,67))

# # print(len(a)+len(b))

# #a=5
# #b=9.8
# #c=3+4j # single values stored in variables don't have length 
# #d=True
# #x=len(a)+len(b)+len(c)+len(d)
# #print(x)


# # a=1
# # b=2
# # c=-1
# # if(a and b):
# #     print("hello")
# #     if(b and c):
# #         print("hii")
# #     else:
# #         print("hey")
# # else:
# #     print("bye")           

# # for i in range(1,11,2):
# #    print(i)

a={"name":"ishika","age":20,"city":"loahru"}

print(a)
print(type(a))
print(a["name"])
print(a.keys())
print(a.values())
print(a.items())
print(a.get("age"))
print(len(a))