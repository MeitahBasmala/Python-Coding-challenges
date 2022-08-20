#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Write a Python class named Point3D defined by x, y, and z.
Define a method that returns (x, y ,z). This tells Python to represent this object in the following 
format: (x, y, z). Then create a variable named my_point containing 
a new instance of Point3D with x=1, y=2, and z=3 and print it.'''

class Point3D:
    def __init__(self, x, y, z):
        self.x= x
        self.y= y
        self.z= z
    def printf(self):
        print('(',self.x,',',self.y,',',self.z, ')')
    
my_point = Point3D(1,2,3)
my_point.printf()


# In[2]:


'''Write a Python class named Rectangle constructed by a length and width.
Define two methods, area and perimeter, which will compute the area and the perimeter of the rectangle.
Then create a variable named my_rectangle containing a new instance of 
Rectangle with width=3 and length = 4 and compute both area and perimeter 
( the area is expected to be 3*4=12 and perimeter 2*(3+4)=14).
        '''
class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width
    def area(self):
        print("area = " , self.length * self.width)
    def perimeter(self):
        print("perimeter = " , (self.length + self.width) *2)
a = Rectangle(2,2)
a.area()
a.perimeter()


# In[5]:


'''Write a Python  class named Circle constructed by its center O and radius r.
Define two methods, area and perimeter, which will compute the area and the perimeter of the circle,
and is Inside() method which allows you to test whether a point A(x, y)
belongs to the circle C(O, r)or not.'''

import math
class Point2D:
    def __init__(self, x, y):
        self.x= x
        self.y= y
    def getX(self):
        return self.x 
    def getY(self):
        return self.y
    
class Circle:
    def __init__(self,O,r):
        self.O = O
        self.r = r
    def area(self):
        print("area = " , math.pi * (self.r **2))
    def perimeter(self):
        print("perimeter = " , 2 * self.r * math.pi)
    def getR(self):
        return self.r
    def check(self,A):
        if (A.getX() - O.getX())**2 + (A.getY() - O.getY())**2 <= C.getR()**2:
            print('the point belongs to the circle')
        else:
            print('the point does not belong to the circle')

x0=float(input('Enter X0: '))
y0=float(input('Enter Y0: '))
x=float(input('Enter X: '))
y=float(input('Enter Y: '))
r = float(input('Enter the radius : '))
O = Point2D(x0,y0)
C = Circle(O,r)       
A = Point2D(x,y)
C.check(A)


# In[1]:


'''Suppose we want to model a bank account with support for deposit and withdraw operations.
Let’s create a Python class named Bank defined by its balance.
Define two methods, deposit and withdraw, to compute the new amount of each operation.'''

class Bank:
    def __init__(self,balance):
        self.balance = balance 
    def deposit(self):
        deposited_money =float(input("Enter the amount you want to deposit: "))
        self.balance += deposited_money
    def withdraw(self):
        withdrawn_money = float(input("Enter the amount you want to withdraw: "))
        if self.balance>=withdrawn_money:
            self.balance-=withdrawn_money
        else:
            print("\n we could not complete this operation maybe you have an insufficient balance  ")
    def display(self):
        print('your balance',self.balance,'DA' )
        
        
a = Bank(10)
a.display()
a.deposit()
a.withdraw()
a.display()
    


# In[6]:


import numpy as np 
a=np.array([1, 2, 3, 4, 5])
b=np.array([5,7, 13])
print(a+b)

