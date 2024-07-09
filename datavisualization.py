#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas numpy kaggle


# In[6]:


import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 10)  
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', 1000)  

data = pd.read_csv('cumulative.csv')

print(data.head())



# In[7]:


print(data.head().to_markdown(index=False, numalign="left", stralign="left"))


# In[9]:


print(data.info())


# In[12]:


file = data.tail(10)
file


# In[15]:


from matplotlib import pyplot as plt
data['koi_score'].plot(kind='hist', bins=20, title='koi_score')
plt.gca().spines[['top', 'right',]].set_visible(False)


# In[16]:


from matplotlib import pyplot as plt
import seaborn as sns

bar_colors = sns.color_palette('Dark2') 
data.groupby('koi_tce_delivname').size().plot(kind='barh', color=bar_colors)
plt.gca().spines['top'].set_visible(False) 
plt.gca().spines['right'].set_visible(False)
plt.show()


# In[ ]:




