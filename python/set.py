s={2,3,4,5}  
print(s)
print(type(s))
x={2,3,"ishika"}
print(x)
x.add(4) #addition 
print(x)
#x.remove(3)#remove element in set if element is it is easliy remove if there is no element it give u error 
print(x)
# add,remove,clear
#union 
print(s|x)
#intersaction
print(x&s)
#difference 
print(s-x)
#symmteric difference
print(s.symmetric_difference(x))
#subset
print(x.issubset(s))
#superset
print(x.issuperset(s))

#discard
print(x.discard(4)) # if there is not element discard give none but remove give error 
#update
x.update(s)
print(x)
#nested update 
a = {1, 2}
b = {3, 4}
c = [5, 6]
d = (7, 8)
a.update(b, c, d)
print(a)

