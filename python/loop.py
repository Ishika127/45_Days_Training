# loop for string 
for x in "Ishika":
    print(x)
#loop in list     
r=[2,3,4,6,6,5,5,556,923,32]
for w in r:
    print(w)
#loop in tuple 
y=(2,3,4,56)
for i in y :
    print(i)
# loop in Dictionary
student = {
     "name": "Ishika",
     "age": 19,
     "marks": [90, 85, 88]
 }
for i in student:
    print(i)
for i in student.items():
    print(i)
for i in student.keys():
    print(i)
for i in student.values():
    print(i)

#loop for range
for i in range(2,10): # for variable in iitration syntax range(stat,stop,stepsize) by defalut stepsize is 1 
    print(i)
    i=i+1
    
#nested for loop
num=5
for i in range(num):
    for j in range(i+1):
        print("*",end=" ")
    print()