#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''Write a Python function to find the largest (max) of three numbers'''
def maxi(a,b,c):
    if a>=b and a>=c:
        maximum = a
    elif b>=a and b>=c:
        maximum = b
    else:
        maximum = c
    return maximum
    
maxi(20, 35, 19)
    


# In[7]:


'''Write a function calculation() so it can accept two variables and 
calculate the addition and subtraction of them.
It must return both addition and subtraction in a single return call.'''

a = int(input("a : "))
b = int(input("b : "))
def calculation(a,b):
    print(a, "+" , b ,"=", a+b)
    print(a, "-" , b ,"=", a-b)

calculation(a,b)


# In[8]:


'''Write a function that sums the elements of a list of integers.
Write a function that multiplies the elements of an integer list.
Use the two functions to sum the elements whose position is an even number (0,2,4…) and multiply the rest.
Hint: Consider extracting two lists from a first list.'''

list = [ ] 
list1 = [ ]
list2 = [ ]
n = int(input("Enter the list size "))
for i in range(0, n): 
    element = int(input())
    list.append(element) 
    if i%2 == 0:
        list1.append(element) 
    else:
        list2.append(element) 
    
print("The list",list)
sum=0
for item in list1:
    sum+=item
print("result of sum = ", sum)
mul=1
for item in list2:
    mul*=item
print("result of mul" ,mul)


# In[3]:


'''Write a function that sums the elements of a list of integers.
Write a function that multiplies the elements of an integer list.
Use the two functions to sum the elements whose position is an even number (0,2,4…) and multiply the rest.
Hint: Consider extracting two lists from a first list.'''
ls = [1,2,3,4,5]

def sum(ls):
    sum=0
    for item in ls:
        sum+=item
    return(sum)
print("the sum of all the list : " ,sum(ls))

def mul(ls):
    mul=1
    for item in ls:
        mul*=item
    return(mul)
print("the multiplication of all the list : " ,mul(ls))

def sum_mul(ls):
    list1 = [ ]
    list2 = [ ]
    for i in range(0, len(ls)): 
        element = int(ls[i])
        if i%2 == 0:
            list1.append(element) 
        else:
            list2.append(element)

    print("sum of numbers with even position = ",  sum(list1))
    print("multiplication of numbers with odd position = " , mul(list2))  
sum_mul(ls)


# In[18]:


'''Write a Python program that accepts a hyphen-separated sequence of words as input 
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample items: green-red-yellow-black-white
Expected result: black-green-red-white-yellow
Hint: There's a split function to separate your input string into words and a sort function to sort.'''

def sortf(Str):
    words = Str.split('-')
    words.sort()
    return(words)

str1 = 'green-red-yellow-black-white'

print(sortf(str1))


# In[1]:


'''Write a function that calculates and prints the value according
to the given formula: Q = square root of [(2 * C * D)/H]. 
Following are the fixed values of C and H: C is 50, and H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example: Let us assume the following comma-separated input sequence is given to the function: 100,150,180. 
Expected result: 18,22,24 
Hints: If the output received is in decimal form, it should be rounded off to its nearest value.
For example, if the output received is 26.0, it should be printed as 26.
In the case of input data being supplied to the question, it should be assumed to be a console input. '''

import math
def calc(D_list):
    D_list = D_list.split(',')
    result = []
    for d in D_list:
        q = round(math.sqrt(2 * 50 * eval(d) / 30))
        result.append(q)
    m = ", ".join([str(r) for r in result])
        #m  = ", ".join(map(str, result))
    print(m)
   # return(result)
D = input("input D: ")
print(calc(D))


# In[2]:


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

