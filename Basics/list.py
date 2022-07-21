a = [1,2,3,4,5,6,7]

# append - -add the list at the end as a list
a.append([1,2,7])
print(a)

#Extend -- add the list at the end as items
a = [1,2,3,4,5,6,7]

a.extend([9,10,11])
print(a)

# clear -- clear the list

a.clear()
print(a)

# copy -- copy the items to a different object
a = [1,2,3,4,5,6,7]
b = a.copy()
print(a)
print(b)

#count -- count the number of instances of passed item
a = [1,2,2,2,2,2,4,5,6,7]
print(a.count(2))

#index -- returns the item index

print(a.index(2,3))

# insert -- insert(location,value)

b.insert(7,98)
print(b)

# pop -- removes item at given index, if none is passes remove item at the beginning of the list

b.pop()
print(b)
b.pop(1)
print(b)

#remove -- removes the first element in the list if the value is there, if the value is not there then it will thorow ValueError
b = [1,2,2,2,2,2,2,23,5,6]
b.remove(2)
print(b)

# reverse -- reverse the order of items in list
b.reverse()
print(b)

#sort
b.sort()
print(b)

#Slicing

print("first 2 elements are ", b[:2])

