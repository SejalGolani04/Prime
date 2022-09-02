#!/usr/bin/env python
# coding: utf-8

# In[8]:


lst=[]
for i in range(2,1001):
    temp=True
    for j in range(2,i):
        if i%j==0 and i!=j:
            temp=False
    if temp:
        lst.append(i)
print(lst)        


# In[ ]:




