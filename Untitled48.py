#!/usr/bin/env python
# coding: utf-8

# In[212]:


import pandas as pd


# In[213]:


house =pd.read_csv(r"C:\Users\Sai Deekshith\Downloads\house.csv") 


# In[214]:


house 


# In[215]:


house.count() 


# In[216]:


house.info()


# In[217]:


house.count() 


# In[218]:


house.isnull().sum()  


# In[219]:


import seaborn as sns 


# In[220]:


sns.heatmap(house.isnull())  


# In[221]:


house.dtypes


# In[222]:


house.columns


# In[223]:


house.shape 


# In[224]:


house.describe() 


# In[225]:


house.head(5) 


# In[226]:


house.date 


# In[227]:


house.date.unique() 


# In[228]:


house.date.nunique() 


# In[229]:


house.date.value_counts() 


# In[230]:


house.date = pd.to_datetime(house.date) 


# In[231]:


house.date 


# In[232]:


house.dtypes 


# In[233]:


house.date 


# In[234]:


#adding new column
house['year'] = house.date.dt.year 


# In[235]:


house.year


# In[236]:


house


# In[237]:


house.insert(1,'month',house.date.dt.month) 


# In[238]:


house.head(5)


# In[239]:


house 


# In[240]:


house.drop(['month','year'],axis=1,inplace=True)


# In[241]:


house 


# In[242]:


house.head(5)


# In[243]:


house.no_of_crimes 


# In[244]:


house.no_of_crimes.count() 


# In[247]:


house.no_of_crimes.isnull().sum()


# In[249]:


house[house.no_of_crimes == 0]


# In[250]:


len(house[house.no_of_crimes == 0]) 


# In[252]:



house.head(5)


# In[254]:


house.average_price 


# In[255]:


house.average_price.count()


# In[256]:


house.average_price.isnull().sum() 


# In[257]:


house.average_price.min() 


# In[258]:


house.average_price.max()


# In[259]:


house['year'] = house.date.dt.year 


# In[260]:


house 


# In[261]:


house1 = house[house.area == "england"] 
house1 


# In[262]:


house1.groupby('year').average_price.min() 


# In[263]:


house1.groupby('year').average_price.max() 


# In[264]:


house.head(4) 


# In[265]:


house.no_of_crimes 


# In[266]:


house.no_of_crimes.count()


# In[267]:


house.no_of_crimes.isnull().sum() 


# In[271]:


house.no_of_crimes.unique()


# In[272]:


house.no_of_crimes.max() 


# In[273]:


house.no_of_crimes.min()


# In[276]:


house.groupby('area').no_of_crimes.min().sort_values(ascending = False)  


# In[277]:


house 


# In[278]:


house.area.count() 


# In[291]:


house[house.average_price < 100000].area.value_counts()


# In[ ]:





# In[ ]:




