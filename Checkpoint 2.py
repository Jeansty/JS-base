#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Question 1
numbers = [*range(2000,3200,1)]

# returns True if number fits in the conditions
def check_cond(number):
    if number % 7 == 0 and number % 5 != 0:
          return True  

    return False

# Extract elements from the numbers list for which check_cond() returns True
Result = filter(check_cond, numbers)

# converting to list
Final_Result = list(Result)

print(Final_Result)


# In[7]:


# Question 2
import math
 
def factorial(x):
    return math.factorial(x)
 
print(factorial(5))


# In[8]:


# Question 3 
number= int(input("type a number:"))
numberDict={}
for i in range(1, number+1 ): 
    numberDict[i]=i*i
    
print(numberDict)


# In[13]:


# Question 4
def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('Kitten', 3))


# In[21]:


# Question 5

import numpy as np
x = np.arange(6).reshape(3, 2)
print("[[0 1] [2 3] [4 5]] ")
print(x)
print("Array to list:")
print(x.tolist())


# In[22]:


#Question 6
import numpy as np
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nCovariance matrix of the said arrays:\n",np.cov(x, y))


# In[23]:


#Question 7
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))


# In[ ]:




