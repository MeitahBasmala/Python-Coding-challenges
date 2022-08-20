#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Write a Python program that accepts the user's first and last name,
and prints them in reverse order with a space between them.'''

firstName = str(input("Enter your first name : "))
lastName = str(input("Enter your last name : "))

print("Full Name : ", lastName,firstName)


# In[11]:


#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = str(input("Enter a positive integer: "))
nn = n + n
nnn = n + nn
sum = int(n) + int(nn) + int(nnn)
print("sum: " ,sum)


# In[ ]:


#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("Emnter a number : "))
if n%2 == 0:
    print("Even")
else:
    print("Odd")


# In[15]:


'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a sequence on a single line.
Hints: Consider use range(#begin, #end) method '''

for i in range(2000,3201):
    if i%7 == 0 and i%5 != 0:
        print(i , end = ",")


# In[11]:


'''Write a program that can compute the factorial of a given number. 
The results should be printed in a sequence on a single line.
Suppose the following input is supplied to the program: 8. Then, the output should be: 40320 '''
''''
n = int(input("Enter a number = "))
def fact(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1 
    else:
        return (a * fact(a-1)) 
print("The factorial number of",n, " = " ,fact(n))
'''
#OR

m = int(input("Enter a number = "))

fact = 1
if m == 0:
    print("The factorial number of 0 is 1 ")
else:
    for i in range(1,m+1):
        fact=fact*i
    print("The factorial number of",m,"is",fact)


# In[6]:


'''Write a program to remove the characters which have odd index values of a given string.
For example: string ="hello team"
The result should be: hlota'''

text = str(input("Enter a text: "))
print(text[::-1])
for i in range(0,len(text)):
    if i%2 == 0:
        print(text[i],end="")
#[::-1] reverse a text


    


# In[ ]:


'''In this challenge, you must discount a price according to its value.
- If the price is 500 or above, there will be a 50% discount.
- If the price is between 200 and 500 (200 inclusive), there will be a 30% discount.
- If the price is less than 200, there will be a 10% discount.'''

price = float(input("Enter the price: "))
if price>=500:
    newPrice = price * 0.5
    print("The new price is : " ,newPrice,"DA")
elif price>=200 and price<500:
    newPrice = price * 0.3
    print("The new price is : " ,newPrice,"DA")
else:
    newPrice = price * 0.1
    print("The new price is : " ,newPrice,"DA")


# In[17]:


lst = [1,2,'frog',4,3,'cat']
lst.append('sun')
print(lst)
lst.insert(7,6)
print(lst)
lst[1]= 3
print(lst)
lst.remove('frog')
print(lst)
del lst[3]
print(lst)
print(lst[2:4])
print(len(lst))

