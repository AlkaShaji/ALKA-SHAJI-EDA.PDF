#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install pandas')


# In[ ]:


get_ipython().system('pip install matplotlib seaborn')


# In[ ]:


pip install matplotlib seaborn


# In[6]:


import pandas as pd
print(pd.__version__)  



# In[11]:


import os
print(os.listdir())  


# In[47]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.set_style("whitegrid")


# In[48]:


pip install --force-reinstall --no-user matplotlib seaborn


# In[13]:


customers_df = pd.read_csv(r"C:\Users\ALKA\OneDrive\Desktop\aaaa\Customers.csv")


# In[16]:


Products_df = pd.read_csv(r"C:\Users\ALKA\OneDrive\Desktop\aaaa\Products.csv")


# In[52]:


transactions_df = pd.read_csv(r"C:\Users\ALKA\OneDrive\Desktop\aaaa\Transactions.csv")


# In[53]:


print(transactions_df.head())


# In[30]:


print(customers_df.head())


# In[32]:


print(products_df.head())


# In[54]:


print(customers_df.isnull().sum())


# In[55]:


print(products_df.isnull().sum())


# In[56]:


print(transactions_df.isnull().sum())


# In[63]:


transactions_df["TransactionDate"] = pd.to_datetime(transactions_df["TransactionDate"])


# In[64]:


print(transactions_df.columns)


# In[69]:


transactions_df.columns = transactions_df.columns.str.strip()  
transactions_df.columns = transactions_df.columns.str.replace(" ", "")  
transactions_df.columns = transactions_df.columns.str.lower()  


# In[70]:


print(customers_df.info())
print(products_df.info())
print(transactions_df.info())




# In[71]:


print(transactions_df.describe())


# In[ ]:




