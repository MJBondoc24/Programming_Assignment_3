#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv("Cars.csv")


# In[6]:


rows = [0,2,4,6,8]


# In[7]:


df = pd.read_csv("cars.csv")


# In[29]:


print(df.iloc[rows])


# In[8]:


print("\nRow for Mazda RX4: \n", df[df['Model'] == 'Mazda RX4'])


# In[9]:


cylinders = df.loc[df['Model'] == 'Camaro Z28', 'cyl'].values[0]


# In[10]:


print(f"\nCamero Z28 has {cylinders} cylinders.")


# In[11]:


models = ('Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic')


# In[12]:


print("\nCylinders and gears for specific models: \n", df[df['Model'].isin(models)][['Model', 'cyl', 'gear']])


# In[ ]:




