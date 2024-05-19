#!/usr/bin/env python
# coding: utf-8

# # Zomato Dataset Exploratory Data Analysis

# In[1]:


#Importing The necessary Python Libraray
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("C:/Users/HP/Downloads/zomato.csv",encoding="latin-1")


# In[3]:


#To show the top 5 records 
df.head()


# In[4]:


#to see the shape (number of rows and number of columns
df.shape


# In[5]:


#To see all the columns of the data set
df.columns


# In[6]:


#To know the information of the data set
df.info()


# Df.describe command will provide the statistical summary of all the columns of integer data types as staitistics measurements can not be calculated for the text data types.

# In[7]:


df.describe()


# # EDA steps
# 1) Finding out the Missing values
# 2) Exploring the Numerical Variables
# 3) Exploring the Categorical Variables
# 4) Finding the relationship Between the features

# In[8]:


#To find out the missing values over here 
df.isnull().sum()


# In[9]:


#Another way of finding out the columns having null values or missing values
[features for features in df.columns if df[features].isnull().sum() >0]


# In[10]:


#Importing another file
df_country = pd.read_excel("C:/Users/HP/Downloads/Country-Code.xlsx")
df_country.head()


# In[11]:


df_country.shape


# In[12]:


a=df.columns
b=df_country.columns
print(a)
print(b)


# In[13]:


#We have country code column common in the both data set so we can merge both data sets
final_df = pd.merge(df,df_country,on='Country Code',how='left')


# In[14]:


final_df.head(5)


# In[15]:


#another way of finding data types
final_df.dtypes


# In[16]:


final_df.columns


# In[17]:


final_df.Country.value_counts()


# In[18]:


country_names=final_df.Country.value_counts().index
country_names


# In[19]:


country_val=final_df.Country.value_counts().values
print(country_val)


# In[20]:


#Pie charts - Top 3 countries using Zomato based on the transactions
plt.pie(country_val[:3],labels=country_names[:3],autopct="%1.2f%%")


# Maximum Transactions are from India (94.39%) and then from Unites states and then United Kingdom

# In[36]:


final_df.columns


# In[37]:


final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index()


# In[23]:


ratings=final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:"Rating Count"})


# In[38]:


print(ratings)


# # Observations
# when rating is between 4.5 to 4.9 it is excellent
# when rating is between 4.0 to 4.4 it is very good
# when rating is between 3.5 to 3.9 it is Good
# when rating is between 2.5 to 3.4 it is average
# when rating is between 1.8 to 2.4 it is Poor

# In[39]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x='Aggregate rating',y='Rating Count',hue='Rating color',data=ratings)


# # observations
# 1)Not rated Count is very High
# 2)Maximum Number of ratings between 2.5 to 3.9

# In[40]:


## Count Plot
sns.countplot(x='Rating color',data=ratings)


# In[41]:


# Countries name that has given zero ratings
final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# # Observation
# max number of zero ratings are from Indian Customers
# 

# In[42]:


#  Which Currency are used by which country
final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[43]:


#Which Countries has Online delievery options
final_df[final_df['Has Online delivery']=="Yes"].Country.value_counts()


# # Observations
# Online delievery are available in India and UAE
# 

# In[44]:


final_df.columns


# In[45]:


final_df.columns


# In[32]:


final_df.City.value_counts().index


# In[33]:


# Top 5 citites doing highest transactions from India
city_values = final_df.City.value_counts().values
city_labels = final_df.City.value_counts().index
plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# # """"#Obsercations 
# # Top 5 Cities from India Doing Highest Number of the Transactions
# 1)New Delhi
# 2)Gurgaon
# 3)Noida
# 4)Faridabad
# 5)Gaziabad

# In[ ]:


# Find the Top 10 Cuisines
final_df


# In[ ]:


final_df[['Cuisines']].groupby(['Cuisines']).value_counts().reset_index()


# In[ ]:


# Afgani cuisines is the most sold cuisine

