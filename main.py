#Set items are enclosed in curly brackets
#Set is unordered
#Set is mutable, can only contain immutable items
#Set elements are unique
#Elements can only contain immutable items


'''
Python Set Attributes
'''
#print(dir(set))


'''
Creating Python Sets
'''
#set = set{} #empty set
#set = {1,2,3}
#print(set)

'''
Modifying a set in Python
'''
#set_example = {'hello', 'world!'}
#set_example[0]
#set_example.add('yay!')
#set_example.add(('hey'))#change it to immutable

#set_example.update([1,2,3])

#print(help(set.add)) #bit more informtion
#print(set_example)



'''
Removing elements from a set
'''

#set_example ={1,2,3,4,5,6,7,8}
#set_example.discard(1)
#set_example.remove(10) remove gives index error
#set_example.pop()


#print(set_example)

#print({'hello', 'world', 'hello', 'hello'})
#it ignores the repetitions 


'''
Set Union Operations
'''
#a = {1,2,3,6,7}
#b = {4,5,6,7,8,9}

#print(a | b)
#print(a.union(b))

#Goves us a combination

'''
Set Intersection Operations
'''


#a = {1,2,3,6,7}
#b = {4,5,6,7,8,9}

#print(a & b)
#print(a.intersection(b))
#it finds what elements are in common
'''
Set Difference Operations
'''

#a = {1,2,3,4,6,7,9}
#b = {2,5,6,7,8,9}

#print(a - b)
#print(a.difference(b))
#1,3 ,4 doesnt exist in b


'''
Set Symmetric Difference
'''
#a = {1,2,3,4,6,7,9}
#b = {2,5,6,7,8,9}

#print(a ^ b)
#print(a.symmetric_difference(b))
#Combines the different elements in both sets
'''
Set Methods
'''

print(dir(set))