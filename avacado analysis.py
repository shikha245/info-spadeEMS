#!/usr/bin/env python
# coding: utf-8

# # Loading in Libraries, Datasets and Data Prep

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv('avocado.csv')
df.head()


# In[4]:


df.dtypes


# In[5]:


df['Date'] = pd.to_datetime(df['Date'])
df.dtypes


# ## Change Over Time

# Visualizing change over time is easily represented with a line graph

# In[7]:


plt.figure(figsize=(12,6))
sns.lineplot(data=df,x='Date',y='AveragePrice',hue='type')


# ## Relationship

# One of the best ways to represent a relationship between two variables is a scatter plot.

# ## Scatter

# In[7]:


plt.figure(figsize=(12,6))
sns.scatterplot(data=df,x='Total Volume',y='Total Bags')


# ## Regplot

# In[8]:


plt.figure(figsize=(12,6))
sns.regplot(data=df,x='Total Volume',y='Total Bags')


# ##  Categories

# In[9]:


plt.figure(figsize=(12,6))
sns.catplot(x='type',y='AveragePrice',data=df);


# # Box and Wisker

# In[10]:


plt.figure(figsize=(12,6))
sns.boxplot(x='type',y='AveragePrice',data=df);


# # Distribution

# In[11]:


plt.figure(figsize=(12,6))
x=df['AveragePrice']
sns.distplot(x)


# In[13]:


plt.figure(figsize=(12,6))
sns.jointplot(data=df,x='Total Volume',y='AveragePrice')


# In[14]:


plt.figure(figsize=(12,6))
sns.jointplot(data=df,x='AveragePrice',y='AveragePrice',kind='kde')


# In[23]:


df_lite =df[['Total Volume','Total Bags','AveragePrice','Small Bags']]
sns.pairplot(df_lite)


# ## Correlation

# In[9]:


correlation = df.corr()
correlation


# In[10]:


plt.figure(figsize=(12,6))
sns.heatmap(correlation,annot=True,cmap='coolwarm')


# In[ ]:




