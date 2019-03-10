#!/usr/bin/env python
# coding: utf-8

# In[9]:


def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))


# In[8]:


calc_factorial(10)


# In[14]:


def factorial(x):
    degisken=1
    if x==0:
        return 1
    else:
        for i in range(1,x+1):
            degisken*=i
        return degisken
factorial(5)


# In[2]:


def fibonacciwloop(n):
    a,b=0,1
    if(n==0):
        return 0
    else:
        for i in range(n-1):
            a,b = b,a+b
        return b
fibonacciwloop(10)
        


# In[1]:


def fibonacciwrecursive(n):
    if(n<2):
        return n
    else:
        return fibonacciwrecursive(n-1) + fibonacciwrecursive(n-2)
fibonacciwrecursive(10)


# In[6]:


def powerwloop(x,y):
    summ = 1
    for i in range(y):
        summ*=x
    return summ
powerwloop(10,3)    
    
    


# In[ ]:


def powerwrecursive(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    elif(n%2==0):
        return powerwrecursive(m*m,n//2)
    elif(n%2!=0):
return powerwrecursive(m*m,n//2)*m


# In[ ]:




