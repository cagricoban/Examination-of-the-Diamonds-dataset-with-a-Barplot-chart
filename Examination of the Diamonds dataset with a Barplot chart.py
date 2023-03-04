#!/usr/bin/env python
# coding: utf-8

# # Examination of the Diamonds dataset with a Barplot chart

# #### Dataset Story
# 
# Price estimation according to the structural and quality information of diamonds in a jewelery company.
# 
# 
# price: price in dollars (326-18.23)
# 
# carat:weight (0.2-5.01)
# 
# cut:quality(J(worst),D(best))
# 
# clarity:cleanliness,clarity(I1(worst),SI2,SI1,VS2,VS1,VVS2,IF(best))
# 
# x:length (0-10-24)
# 
# y: witch in mm (0-58.9)
# 
# x: depth mm(0-31.8)
# 
# depth: percentage of the depth of the diamond
# 
# disaster: the width of the diamond relative to the widest point (43-95)
# 
# 
# 

# #### Veri Setine Bakış

# In[1]:


import seaborn as sns


# In[2]:


diamonds= sns.load_dataset('diamonds')
df=diamonds.copy()
df.head()


# In[3]:


df["cut"].value_counts() #number of observations in categorical variable


# In[4]:


df["color"].value_counts()# of observations in a categorical variable


# In[5]:


#ordinal tanımlama:Hiyerarşik bir sıralama vardır.
from pandas.api.types import CategoricalDtype


# In[6]:


df.cut.head()


# In[7]:


df.cut=df.cut.astype(CategoricalDtype(ordered= True))


# In[8]:


cut_kategoriler=["Fair","Good","Very Good","Premium","Ideal"]# kategorileri küçükten büyüğe sıralamalıyız.
df.cut=df.cut.astype(CategoricalDtype(categories= cut_kategoriler,ordered= True))


# In[9]:


df.cut.head()


# In[10]:


#barplot


# In[11]:


(df["cut"]
 .value_counts()
 .plot.barh()
 .set_title("Class Frequencies of the Cut Variable")); # Category frequencies in the variable


# In[12]:


sns.barplot(x= "cut",y=df.cut.index ,data=df);


# # Crossovers

# In[13]:


sns.catplot(x="cut",y="price", data=df)# Display of cute and price variables crosswise


# Price and cute variables are crossed and given in column chart. The variable is cute on the X axis and Price is given on the Y axis. On the X-axis, the distribution of classes according to the Price variable is given. The price variable of the Fair category has the highest demand, especially at 5000 and 2500 price points. As the category quality increases, the demand for the upper amount of the Price variable increases as expected.

# In[14]:


sns.barplot(x="cut",y="price",hue="color",data=df)#Price variable is divided into categories both on the basis of color and on the basis of cut variable.


# In our chart, the distribution of the categories in the cut variable, together with the category in the color variable, according to the price variable is given. Our chart has gained more explainability. Since Seaborn is an advanced library, data representation values have been created. It created a breakdown of categorical variables within itself. In fact, the ends of the painted scales are the mean of two categorical variables according to Price. The black bars at the ends are the standard deviation.

# In[15]:


#The breakdown was made according to two categorical variables. We said to do the average operation according to the price variable.
df.groupby(["cut","color"])["price"].mean()

