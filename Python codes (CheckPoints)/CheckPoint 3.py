#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Write a Python program that multiplies all the items in a list.
Sample list= [2, 3, 6]
Result = 36'''

list = [ ] 
n = int(input("Enter the list size "))
for i in range(0, n): 
    element = int(input())
    list.append(element) 
print("The list",list)
mul=1
for item in list:
    mul*=item
print("result" ,mul)


# In[1]:


'''Write a Python program to get a list, sorted in increasing order by the last element in each tuple, from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
Hint: You can use the sort function.'''

list1 = [ ] 
n = int(input("Enter the list size "))
print("Enter the first list")
for i in range(0, n): 
    element1 = int(input())
    list1.append(element1) 
list1.sort()
print(list1)
print("Enter the second list")

list2 = [ ] 
for i in range(0, n): 
    element2 = int(input())
    list2.append(element2) 
list2.sort(reverse=True)
print(list2)
#this
tupl = zip(list1,list2)
list_tuple = tuple(tupl)
print(list_tuple)
#or this
result = [(list1[i], list2[i]) for i in range(0, n)]
print(result)


# In[1]:


'''Write a Python program that combines two dictionaries by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}'''
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = Counter(d1) + Counter(d2)
print(d3)


# In[6]:


'''Write a Python program that combines two dictionaries by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}'''

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for key in d1.keys():
    if key in d2.keys():
        d3[key] = d1[key] + d2[key]
    if key not in d2.keys():
        d3[key] = d1[key]
for key in d2.keys():
    if key not in d1.keys():
        d3[key] = d2[key]

print(d3)


# In[17]:


'''Write a Python program that combines two dictionaries by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}'''

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for key in d1.keys():
    for key2 in d2.keys():
        if key == key2:
            d3[key] = d1[key] + d2[key2]
        elif key not in d2.keys():
            d3[key] = d1[key]
for key in d2.keys():
    if key not in d1.keys():
        d3[key] = d2[key]

print(d3)


# In[7]:


'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
so that is an integral number between 1 and n (both included).
Then the program should print the dictionary. 
Suppose the following input is supplied to the program: 8.
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''
num = int(input("Enter a number.. "))
d = dict()
for element in range(1,num+1):
    d[element] = element*element
print("The output: ")
print(d)


# In[26]:


'''Write a program to sort a tuple by its float element.'''
tupl= [('item3', '129.5'),('item1', '62.20'), ('item2', '18.13')]
tupl.sort(reverse = True)
print(tupl)

