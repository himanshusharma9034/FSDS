#!/usr/bin/env python
# coding: utf-8

# In[41]:


# 1. Write a Python program to convert kilometers to miles?
a = int(input("Enter the Value in 'km' : "))
miles = 0.62137 * a
print("Value in 'Miles' = {}".format(miles))


# In[43]:


# 2. Write a Python program to convert Celsius to Fahrenheit?
a = int(input("Enter the Value in 'Celsius' : "))
fer = (a * 9/5) + 32
print("Value in 'Fehrenheit' = {}".format(fer))


# In[51]:


# 3. Write a Python program to display calendar?
import calendar
print(calendar.month(int(input("Enter the Year : ")),int(input("Enter the Month : "))))


# In[60]:


#  4. Write a Python program to solve quadratic equation?
# (-b + sqrt(b**2-4ac))/2a
# (-b - sqrt(b**2-4ac))/2a
import cmath
b = int(input("Enter the Value of 'b' : ")) 
a = int(input("Enter the Value of 'a' : ")) 
c = int(input("Enter the Value of 'c' : ")) 
p = (-b + (cmath.sqrt(b**2-(4*a*c))))/2*a
n = (-b - (cmath.sqrt(b**2-4*a*c)))/2*a
print("The Values of the quadratic equation is : {},{}".format(p,n))


# In[63]:


# 5. Write a Python program to swap two variables without temp variable?
b = input("Enter the Value of 'b' : ") 
a = input("Enter the Value of 'a' : ")
# 2---> b
# 3---> a
a,b = b,a

print(b,a)


# In[ ]:




