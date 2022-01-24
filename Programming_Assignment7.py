#!/usr/bin/env python
# coding: utf-8

# In[221]:


# 1. Write a Python Program to find sum of array?
# l = [1,2,3,4,5,6]
lst = list(input("Enter the list : "))
s = 0
for i in lst:
    s = s + int(i)
print("The sum of the lsit is = {}".format(s))


# In[222]:


# 2. Write a Python Program to find largest element in an array?
lst = list(input("Enter the list : "))
print("The Largest element in the list is = {}".format(max(lst)))


# In[223]:


# 3. Write a Python Program for array rotation?
lst = list(input("Enter the list : "))
print("The Rotation of the given list is = {}".format(lst[::-1]))


# In[18]:


#  4. Write a Python Program to Split the array and add the first part to the end?
s = 'himanshu'
l = []
l.extend(s)
# l.insert(-1,'h')
l[0] = l[-1]
l


# In[64]:


# 5. Write a Python Program to check if given array is Monotonic?
l = [1,2,3,4,5,6,7]
# l.sort(reverse = True)
l.sort()
l.sort() is True


# In[66]:


l = [1, 2, 3, 4, 5, 7, 8, 9]
if l.sort():
    print("An array is Monotonic")
else:
    print("An array is not a Monotonic")


# In[70]:


l = [1,2,3,4,5,7,8,9]
l1 = [9,8,7,6,5,4,3,2,1]
for i in range(len(l)): #  0-7
    while i < len(l)-1:        #0,1,2 < 7
        if l[i] <= l[i+1] and l1[i] >= l1[i+1]: 
            print(i,l[i],l[i+1])     #1,3,44 <= 3,44,4
            a = 1                #   T,T
            i += 1       
            # break         #  i = 1,2
        else:
            a= 0
            break
    break
if a == 1:
    print("An array is Monotonic")
else: 
    print("An array is not a Monotonic")


# In[ ]:




