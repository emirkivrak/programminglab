#!/usr/bin/env python
# coding: utf-8

# In[1]:


def selectionsort(dizi):
    for i in range (len(dizi)):
        min_indx=i
        for j in range(i+1,len(dizi)):
            if dizi[min_indx]>dizi[j]:
                min_indx=j
        dizi[i],dizi[min_indx]=dizi[min_indx],dizi[i]
    return dizi
                
            

dizii=[1,221,31,45,12,56,11]
selectionsort(dizii)
print(dizii)


# In[5]:


def bubblesort(dizi):
    for i in range(len(dizi)):
        for j in range(0,len(dizi)-i-1):
            if dizi[j]>dizi[j+1]:
                dizi[j+1],dizi[j] = dizi[j],dizi[j+1]
    return dizi

dizi2=[1,83,12,44,55,12]
bubblesort(dizi2)
print(dizi2)


# In[1]:


##searching in a list
def search(dizi,item):
    for i in range (len(dizi)):
        if item == dizi[i]:
            return 1
        else:
            return 0


dizi2=[2,3,4,5,6,7]
search(dizi2,2)


# In[ ]:




