#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[10]:


df = pd.read_csv("Cars.csv")


# In[18]:


print("First five rows: \n", df.head())


# In[19]:


print("Last five rows: \n", df.tail())

