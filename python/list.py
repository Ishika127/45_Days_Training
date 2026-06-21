#list is a collection ehich is ordered and changeable.allows duplicate members, heterogeneous data types,list is defined by using square brackets[]
#creating a list
#mylist=[3,4,5,6,7]
#print(mylist)
#a=[1,2,3,"ishika",4.5,True]
#print(a)
#
#accesing the lists
#print(mylist[3])
#print(a[4])
#negative indexing
#print(a[-2])
#slicing the list
#print(a[1:5])
#count function
#print(a.count(3))
#print(a.count("ishika"))
#length of the list
#print(len(a))
#changing the value of the list
#
# a[2]=1000
#print(a)
#adding element to the list
#a.append("java")
#print(a)
#reverse the list by using slicing method 
#print(a[ : :-1])
#operations on list
b=[3,90,89,"ishika",True,9.8]
#add element by using append method
b.append("hey")
print(b)
#index method is used to find the index 
print(b.index("ishika"))
#insert element at specific position by using insert methos
b.insert(0,100)
print(b)
#extend method is used to add multiple element to the list
b.extend([4,5,6])
print(b) 
#add two list 
c=[1,2,3]
d=[3,4,5,6]
e=c+d
print(e)
#the index of all the elemeent in the list
f=[1,3,434,[3,4,5]]
print(f)
print(f[3][1])
#remove element from the list by using remove method
f.remove(3)
print(f)
#pop method is used to remove element  by using index
f.pop(2)
print(f)
#clear method is used to remove all the element from the list
f.clear()
print(f)
#copy method is used to copy the list
g=[1,2,3,5,7]
h=g.copy()
print(h)
#count method is used to count the number of times an element appears in ths list
print(g.count(3))
#sort method is used to sort the list in ascending order
i=[3,8,1,8]
i.sort()
print(i)
x=[2,3,4,5]
y=[6,7,8,9]
#adding two list 
print(x+y)
#multiply two list
print(x*2)
#dividing two list is not possible
#subtracting two list is not possible
#multiplying two list is not possible