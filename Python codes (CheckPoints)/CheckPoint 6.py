#!/usr/bin/env python
# coding: utf-8

# In[5]:


#01
'''Write a Python program to convert an array to an ordinary list with the same items.
We can use the np.tolist() function.'''

import numpy as np
list1 = [ ] 
n = int(input("Enter the list size "))
print("Enter the first list")
for i in range(0, n): 
    element1 = int(input())
    list1.append(element1) 
arr=np.array(list1)

'''#list of lists
arr= array.reshape(2,2)
print(array)
'''
list2 = arr.tolist()
print(list2)
'''
# matrix 
arr=np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
print(arr)'''


# In[66]:


#2
'''Write a NumPy program to compute the sum of the diagonal elements of a given array.
Hint: There are two possible methods to solve this problem: 
Manually (without direct function). 
Using the trace function'''

import numpy as np
'''    
sum of two matrixes diagonals
M1=np.array([[4,1, 9],[ 12 ,3 ,1] ,[ 4, 5, 6]])
M2=np.array([[1 ,2 ,3] ,[ 5, 4, 6] ,[ 7, 8 ,9]])

M3 = np.empty((M1.shape))
for i in range(len(M1)):
  M3[i][i] = M1[i][i] + M2[i][i]
  print('the sum of the' , i+1,'element of the two diagonals = ' , int(M3[i][i]))
'''
#method 1
M1=np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
sum = 0
for i in range(len(M1)):
    sum += M1[i][i] 
print("The sum = ", sum)
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
#method 2
res = np.trace(arr)
print("The sum = ", res)


# In[53]:


'''Given an array of your choice, get all the values higher than X:
If a = [[1,2],[3,5]] and x = 2 :  then 3 and 5 are higher than 2. '''

import numpy as np
number = int(input('Enter a number: '))
M1=np.array([[9 ,2 ,5] ,
             [ 4, 3, 6] ,
             [ 7, 1 ,8]])
M2 = np.empty((M1.shape))
for i in range(len(M1)):
    for j in range(len(M1)):
        if number in M1:
            if M1[i][j] > number:
                M2[i][j] = M1[i][j]
                print(int(M2[i][j]),end=' ')

        else:
            print('the number in not in the array')


# In[58]:


'''Given two arrays, A & B have the same shape. 
The task is to apply addition by hand: C is the new array.'''

import numpy as np
M1=np.array([[4,1, 9],
             [ 12 ,3 ,1] ,
             [ 4, 5, 6]])

M2=np.array([[1 ,2 ,3] ,
             [ 5, 4, 6] ,
             [ 7, 8 ,9]])
M3 = np.empty((M1.shape))

for i in range(len(M1)):
    for j in range(len(M2)):
        M3[i][j] = M1[i][j] + M2[i][j]
for m in M3:
    print(m)
    


# In[68]:


'''Write a NumPy program to subtract the mean of each row of a given matrix.
Hint: use the mean function'''

import numpy as np
M1=np.array([[4,1, 9],
             [ 12 ,3 ,1] ,
             [ 4, 5, 6]])
print("The mean values:\n", np.mean(M1, axis=1, keepdims=True))
print("Subtract the mean of each row of the said matrix:")
M2 = M1 - M1.mean(axis=1, keepdims=True)
print(M2)

