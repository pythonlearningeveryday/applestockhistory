#!/usr/bin/env python
# coding: utf-8

# In[102]:


import pandas
from pandas_datareader import data, wb as pdr
import pandas_datareader.data as web


# In[108]:


import datetime as dt


# In[119]:


start = dt.datetime(2015,4,1)
end = dt.datetime(2016,1,1)


# In[120]:


df = web.DataReader('AAPL', 'yahoo', start, end)


# In[121]:


df.head()


# In[132]:


df[['Open', 'Close']].tail(30)


# In[133]:


df[['Open', 'Close']].tail(30).plot()


# In[ ]:




