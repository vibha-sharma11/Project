#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np


# In[17]:


df = pd.read_csv("C:/Users/Dell/Desktop/research dataset/dataset 1/purchase data.csv")


# In[18]:


print(df.head(5))


# In[19]:


headings = df.columns.tolist()
print(headings)


# In[20]:


plt.hist(headings, bins = 25)
plt.title('Normality check through Histogram')
plt.show()


# In[27]:


def generate_data(middle, modifier = 1):
    array = np.array([])
    for i in range (20):
        value = i + 1
        number = max(1, middle -abs(middle -value)* modifier)
        for j in range(int(number)):
            array = np.append(array, [value])
    
    return array
x = generate_data(13)
plt.hist(x)


# In[26]:


print(stats.skew(x))


# In[29]:


w, p= stats.shapiro(x)
print(w , p)


# In[31]:


p = stats.kstest(x, 'norm')
print(p)


# In[ ]:




