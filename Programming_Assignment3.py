#!/usr/bin/env python
# coding: utf-8

# In[70]:


# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
number = int(input("ENter the number to check the status : "))
if number > 0: print("Positive")
elif number < 0 : print("Negative")
else: print("Zero")


# In[81]:


#  2. Write a Python Program to Check if a Number is Odd or Even?
number = int(input("ENter the number to check ODD/EVEN : "))
if number % 2 == 0 : print("EVEN")
else : print("ODD")


# In[ ]:


#  3. Write a Python Program to Check Leap Year?
year = int(input("Enter the year : "))
if year % 4 != 0 : print("Not a Leap year")
elif year %100 !=0 : print("Leap Year")
elif year %400 !=0 : print("Not a Leap Year")
else: print("Leap Year")


# In[197]:


# 4. Write a Python Program to Check Prime Number?
number = int(input("Enter the number to check if it's prime or not : "))

for i in range(2,number):
    while i < number:
        if number % i != 0:
            i = i+1
            a = 1
            continue
             
        else:
            a = 0
            break
    break
if a ==1:
    print("Prime Number")
else:
    print("NOT a Primt Number")


# In[ ]:


#  5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
for i in range(1, 10000 + 1):
    if i > 1:
        for j in range(2,i):
               if (i % j) == 0:
                break
        else:
            print(i)


# In[ ]:





# In[ ]:





# In[ ]:




