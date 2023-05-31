#!/usr/bin/env python
# coding: utf-8

# # Data Analysis for Automobile car dealership with Python

# 1. Exploring  the  data for Automobile  car dealership

# In[2]:


# Import pandas library
import  pandas as pd 


# In[3]:


#The online  file by the URL provides  above ,and  assign  it to variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)


# In[4]:


# Showing the summary of the  first 5 row using dataframe.head()
print("The first 5 rows of the dataframe")
df.head(5)


# In[5]:


#Showing the bottom 10 rows

df.tail(10)


# In[7]:


# creating headers for the rows.

headers = ["symboling","normalized-loses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel_base","length","width","height","curb-weight","engine-type",
         "num-of-cylinders","engine-size","fuel-system","bore","stroke","compresion-rate","horsepower","peak-rpm","city-mpg","highway-mpg","price"]

print("headers\n" , headers)


# In[8]:


# I will replace headers and recheck the data frame
df.columns= headers
df.head(10)


# In[9]:


# Dropping missing values  along the  column "price" so that ican focus on the cars that were bought.
df.dropna(subset=["price"], axis =0)


# In[14]:


# Saving the Data set.
df.to_csv("automobile.csv", index =False)


# 2.Data Wrangling to convert the data  from the initial format to a format that may be  better for analysis.

# In[15]:


# libaries

import pandas  as pd
import matplotlib.pylab as plt
import numpy as np


# In[16]:


# replace "?" to NaN

df.replace("?",np.nan , inplace =True)
df.head(5)


# In[17]:


# Identifying  missing  values within the data.
missing_data= df.isnull()
missing_data.head(5)


# In[18]:


avg_norm_loss = df["normalized-loses"].astype("float").mean(axis=0)
print("Average of normalized-loses:",avg_norm_loss)


# In[19]:


# COUNT MISSING VALUES IN EACH COLUMN
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# 3.Replacing  missing  values/null values on the data frame

# In[20]:


# Calculating average for normalized losses
avg_norm_loss = df['normalized-loses'].astype('float').mean(axis=0)
print("Average of normalized-loses: ",avg_norm_loss)


# In[21]:


# Replacing missing value with  normalized losses average on the data frame.
df["normalized-loses"].replace(np.nan,avg_norm_loss, inplace=True)


# In[22]:


#calculating  average for bore
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore: ", avg_bore)


# In[23]:


#replacing missing value bore avaerage on the  dataframe
df["bore"].replace(np.nan, avg_bore, inplace=True)


# In[24]:


#calculating average for stroke
avg_stroke= df['stroke'].astype('float').mean(axis=0)
print('stroke: ', avg_stroke)


# In[25]:


# Replacing missing value with stroke on the dataframe
df["stroke"].replace(np.nan,avg_stroke, inplace=True)


# In[26]:


# Calculating average  for the  horse power
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average of horsepower: ",avg_horsepower)


# In[27]:


# Replacing missing  value with horsepower  on the dataframe.
df["horsepower"].replace(np.nan, avg_horsepower, inplace=True)


# In[28]:


# Calculating  the avaerage for peak-rpm
avg_peakrpm =df['peak-rpm'].astype('float').mean(axis=0)
print("peak-rpm: ", avg_peakrpm)


# In[29]:


#Replacing  missing value peak-rpm on the dataframe
df["peak-rpm"].replace(np.nan ,avg_peakrpm, inplace=True)


# In[30]:


# To see which values are oresentin a particular column

df["num-of-doors"].value_counts()


# In[31]:


# I can use  the ".idxmax()" method to calculate  the most commontype automatically:
df["num-of-doors"].value_counts().idxmax()


# In[32]:


# Dropping   the whole column with the missing data.
df.dropna(subset=["price"],axis=0, inplace=True)

#reset index ,because we dropped two rows
df.reset_index(drop=True, inplace=True)


# In[33]:


df.head()


# 4. Converting  data types  to proper  formats

# In[35]:


# Converting  data
df[["bore","stroke"]] = df[["bore","stroke"]].astype("float")
df[["normalized-loses"]] = df[["normalized-loses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] =  df[["peak-rpm"]].astype("float")


# In[37]:


#  list  the columns  after the conversion
df.dtypes


# 4. Example 
# 
# Transform  miles per gallon to Kilometers.
# 
# In our dataset,the  fuel consumption columns"city-mpg" and "highway-mpg" are represented by mpg(miles per gallon )unit.Assume we are  developing  an application in a country  that accept the fuel  consumption with l/100km standard.
# 
# We will need to apply data transformation to transform mpg into  L/100km?
# 
# The formula for unit conversion is 
# 
# L/100km =235/mpg

# In[38]:


df.head()


# In[39]:


# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# check tranformed data
df.head()


# In[40]:


# Tranforming mpg to L/100km in the column of " highway-mpg "
df['highway-L/100km'] = 235/df["highway-mpg"]

# Checking tranformed data
df.head()


# 5. Example : 
#  Objective  I want to normalize the variables so thier values  ranges from 0 to 1.
#   Approach :replace original value by (original value)/(maxium  value)

# In[41]:


#replace(original value) by (original value)/(maxium value)
df['lenghth'] = df['length']/df['length'].max()
df['width']  = df['width']/df['width'].max()


# In[42]:


# Normalizing the column "height"
df['height'] = df['height']/df['height'].max()


# 6. Example
# In our dataset,"horsepoer" is  a real valued variable ranging from 48 to 288,it has 57 unique values.What if we only care about the price  difference between cars with high horsepower,medium horsepower , and little (3types)?Can we rearrange  them into three "bins" to simplify analysis ?
# 
# I can only use the method  'cut' to segment the 'horsepower' column into 3 bins

# In[44]:


# Coverting  data to correct  format
df["horsepower"]=df["horsepower"].astype(int, copy=True)


# In[45]:


#Histogram of horspower ,to see what the distribution of horse looks like.
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot

plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# 7.  I would like 3 bins  of equal size bandwidth  so we use numply's linspace(start_valu, end_value, numbers_generated function. Since i want to include the minimum value of horsepower  we  want to  set start_value = min(df["horsepower"]).Also i want to include the maxium value  of horsepower we want to set end_value=max(df["horsepower"]).Lastly since am building 3 bins  of equal length ,there should be 4 dividers , so numbers _generated =4

# In[46]:


# Building array  ,with a minimum value to a maxium value, with bandwith calculated above.The bins will be values used to determine when one bin  ends and another begins.
bins = np.linspace(min(df["horsepower"]),max(df["horsepower"]),4)
bins


# In[47]:


# setting group names 
group_names = ['Low', 'Medium', 'high']


# In[48]:


# Applying the function "cut" the determine what each value of "df['horsepower']" belongs to.
df['horsepower-binned']=pd.cut(df['horsepower'],bins, labels=group_names, include_lowest = True )
df[['horsepower','horsepower-binned']].head(20)


# In[49]:


# The number  of vehicles in each bin
df["horsepower-binned"].value_counts()


# In[50]:


#Plotting the distribution  of each bin.
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt 
from matplotlib  import  pyplot
pyplot.bar(group_names,df["horsepower-binned"].value_counts())

#set x/y labels  and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower  bins")


# In[51]:


# Histogram is used to visualize  the distribution of  bins we  created above.
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib  as plt 
from matplotlib  import pyplot

a = (0,1,2)

# draw  histogram  of  attrivute  "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"])

#Set x/y labels  and  plot title 
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# In[52]:


df.to_csv('clean_df.csv')


# In[ ]:




