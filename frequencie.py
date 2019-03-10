#!/usr/bin/env python
# coding: utf-8

# In[5]:


## this func able to find a list's frequency with dictionary
experimental=[2,3,4,5,2,2,1,4,7,9]

def frequencyindict(mylist):
    frequency={}
    
    for i in mylist:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

frequencyindict(experimental)
            
    


# In[12]:


## this func able to find a list's frequency without dictionary
experimental=[2,3,4,5,2,2,1,4,7,9]
def frequencyinlist(mylist2):
    frequencylist=[]
    for i in range(len(mylist2)):
        check=False
        for j in range(len(frequencylist)):
            if(mylist2[i]==frequencylist[j][0]):
                frequencylist[j][1]=frequencylist[j][1]+1
                check=True
            else:
                if(check==False):
                    frequencylist.append(mylist2[i],1)
    return frequencylist
print(frequencyinlist(experimental))
                


# In[ ]:




