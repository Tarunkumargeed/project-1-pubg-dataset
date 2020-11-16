#!/usr/bin/env python
# coding: utf-8

# In[2]:


#libraries importing 

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# # Task 1:Read the dataset.
# 

# In[3]:


df=pd.read_csv("C:\\Users\\91860\\Downloads\\pubg - Dr. Darshan Ingle.csv")
df.head()


# # Task 2:Check the datatype of all the columns
# 

# In[4]:


data_type = df.dtypes
data_type


# # Task 3: Find the summary of all the numerical columns and write your findings about it .
# 

# In[5]:


num_summary = df.describe()
num_summary


# # Task 4: The average person kills how many players?
# 

# In[6]:


avg = df['kills'].mean()
print("The average person kills :", avg,"player")


# # Task 5: 99% of people have how many kills?
# 

# In[7]:


n_per = df["kills"].quantile(0.99)
print("99% of people have",n_per,"kills")


# # Task 6:The most kills ever recorded are how much?
# 

# In[8]:


most_kills = df["kills"].max()
print("The most kills ever recorded are :",most_kills)


# # Task 7:Print all the columns of the dataframe
# 
# 

# In[9]:


df.columns


# # Task 8:Comment on distribution of the match's duration. Use seaborn.
# 

# In[10]:


sns.distplot( df['matchDuration'] );
plt.show()


# # Task 9:Comment on distribution of the walk distance. Use seaborn
# 
# 

# In[11]:


sns.distplot( df['walkDistance'] );
plt.show()


# # Task 10: Plot distribution of the match's duration vs walk distance one below the other.
# 

# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('classic')
plt.figure()

# ploting for matchDuration
plt.subplot(2,1,1)
plt.plot(df["matchDuration"],"-")
plt.xlabel("Match Duration")

# ploting for walkDistance
plt.subplot(2,1,2)
plt.plot(df["walkDistance"],"--")
plt.xlabel("Walk Distance")


# # Task 11: Plot distribution of the match's duration vs walk distance side by side.
# 

# In[13]:


plt.style.use('classic')
plt.figure(figsize=(10,5))

# ploting for matchDuration
plt.subplot(1,2,1)
plt.plot(df["matchDuration"])
plt.xlabel("Match Duration")

# ploting for walkDistance
plt.subplot(1,2,2)
plt.plot(df["walkDistance"])
plt.xlabel("Walk Distance")


# # Task 12: Pairplot the dataframe. Comment on kills vs damage dealt, Comment on maxPlace vs numGroups.
# 

# In[14]:


sns.pairplot(df.head(400));


# # Task 13: How many unique values are there in 'matchType' and what are their counts?
# 

# In[15]:


uni = pd.unique(df['matchType'])
print("\nUnique value in matchType is :",uni)
n_uni = len(uni)
print("\nCount of unique value in matchType is :",n_uni)


# # Task 14:Plot a barplot of ‘matchType’ vs 'killPoints'
# 

# In[19]:


sns.barplot(df['matchType'],df['killPoints']);
plt.show()


# # Task 15 : Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’
# 

# In[20]:


sns.barplot(df['matchType'],df['weaponsAcquired']);
plt.show()


# # Task 16 : Find the Categorical columns.
# 

# In[21]:


df.select_dtypes(exclude=['number'])


# # Task 17 : Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’
# 

# In[22]:


sns.boxplot(df['matchType'],df['winPlacePerc']);
plt.xticks(rotation=70);


# # Task 18 : Plot a boxplot of ‘matchType’ vs ‘matchDuration’
# 

# In[23]:


sns.boxplot(df['matchType'],df['matchDuration']);
plt.xticks(rotation=70);


# # Task 19 : Change the orientation of the above plot to horizontal
# 

# In[24]:


sns.boxplot(df['matchDuration'],df['matchType']);


# # Task 20: Add a new column called ‘KILL’ which contains the sum of following columns viz. headshotKills,teamKills, roadKills.
# 

# In[25]:


df['KILL']=(df.headshotKills+df.roadKills+df.teamKills)
kd=pd.DataFrame(df[['headshotKills','roadKills','teamKills','KILL']])
print(kd.head())


# # Task 21: Round off column ‘winPlacePerc’ to 2 decimals.
# 

# In[26]:


df['winPlacePerc']=round(df['winPlacePerc'],2)

df['winPlacePerc']


# # Task 22: Take a sample of size 50 from the column damageDealt for 100 times and calculate its mean. Plot it on a histogram and comment on its distribution
# 

# In[27]:


x = []
for i in range(100):
    x.append(df['damageDealt'].sample(50).mean())
means = np.array(x)
sns.distplot(means);


# In[ ]:




