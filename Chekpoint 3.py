#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv(r"C:\Users\dofla\Downloads\titanic-passengers.csv", sep=";")
df


# In[2]:


df.info()


# In[3]:


print(df.columns.values) #Information


# In[4]:


print(df.isnull().sum())


# In[5]:


print(df.isnull().sum().sum())


# In[6]:


print(df.isnull()) 


# In[7]:


df.dropna(axis=0,inplace=True) 


# In[8]:


print(df.isnull().sum())


# In[9]:



print(df.isnull().sum().sum())


# In[10]:



df['Age'].mean()


# In[11]:


df['Age'].fillna(df['Age'].mean(), inplace=True)


# In[12]:



print(df['Age'].isnull().sum()) 


# In[13]:


df


# In[14]:



print(df["Cabin"].value_counts())


# In[15]:



df["Cabin"].fillna('G6', inplace=True)


# In[16]:


print(df.isnull().sum())


# In[18]:


df


# In[19]:


print(df["Embarked"].value_counts())


# In[20]:



df["Embarked"].fillna('S', inplace=True)


# In[21]:


df["Embarked"].isnull().sum()


# In[22]:


df.isnull().sum().sum() 


# In[23]:



df.head()


# In[24]:


df.info()


# In[28]:


import matplotlib.pyplot as plt
plt.title("Titanic")
plt.xlabel("Age")
df['Age'].plot.hist(color = 'grey')


# In[29]:


import seaborn as sns
sns.distplot(df["Age"], bins=10, hist = True, kde = True, color = "cyan")


# In[30]:


sns.countplot(x='Sex', data=df)
plt.ylabel("distribution")
plt.xticks(rotation=-45)


# In[31]:


sns.countplot(x='Pclass', data=df)
plt.ylabel("distribution")
plt.xticks()


# In[32]:


sns.countplot(x='Survived', data=df)
plt.ylabel("distribution")
plt.xticks(rotation=-45)


# In[33]:


Convers={"Sex":{"Female":1, "Male": 0}} 
df.replace(Convers, inplace=True)
df[["Sex", "Age"]].groupby(["Sex"], as_index=True).mean()


# In[34]:


fig = plt.figure(figsize=(17,5))
fig.add_subplot(121)
plt.title('Observation')
sns.barplot(data=df, x='Sex',y='Age',hue='Survived')
plt.show()


# In[35]:


grid = sns.FacetGrid(df, row="Sex", col="Survived", height=3.5, aspect=1.6)
grid.map(sns.barplot, "Pclass", 'Age', alpha=.5, ci=None)
grid.add_legend()


# In[36]:


import matplotlib.pyplot as plt
import seaborn as sns
g=sns.FacetGrid(df,col='Survived')
g.map(plt.hist,'Embarked',bins=20)


# In[37]:


def plot_correlation_map(df):
    corr = df.corr()
    s , ax = plt.subplots( figsize =( 12 , 10 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    s = sns.heatmap(
        corr, 
        cmap = cmap,
        square=True, 
        cbar_kws={ 'shrink' : .9 }, 
        ax=ax, 
        annot = True, 
        annot_kws = { 'fontsize' : 12 }
    )


# In[38]:


df.corr()


# In[39]:


def plot_correlation_map(df):
    corr = df.corr()
    s , ax = plt.subplots( figsize =( 12 , 10 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    s = sns.heatmap(
        corr, 
        cmap = cmap,
        square=True, 
        cbar_kws={ 'shrink' : .9 }, 
        ax=ax, 
        annot = True, 
        annot_kws = { 'fontsize' : 12 }
    )

def category_values(Pclass, Survived):
    for c in Survived:
        print('\n', Pclass.groupby(by=c)[c].count().sort_values(ascending=False))
        print('Nulls: ', Pclass[c].isnull().sum())


# In[40]:


plot_correlation_map(df)


# In[41]:


Convers={"Survived":{"Yes":1, "No": 0}} 
df.replace(Convers, inplace=True)
df[["Pclass", "Survived"]].groupby(["Pclass"], as_index=True).mean()


# In[42]:


cleanup={"Survived":{"Yes":1, "No": 0}}  # at first, let's convert Survived to numerical format
df.replace(cleanup, inplace=True)
df[["Embarked", "Survived"]].groupby(["Embarked"], as_index=True).mean()


# In[43]:


new_data = df.drop(["PassengerId","SibSp","Parch","Ticket",], axis=1)


# In[44]:



new_data


# In[45]:


df['Title'] = df['Name'].str.split(',|\\.',expand = True)[1] 
df['Title'] = df['Title'].str.strip()
df['Title'].value_counts()


# In[46]:


grid = sns.FacetGrid(df, row="Sex", col="Survived", height=2.2, aspect=1.6)
grid.map(sns.barplot, "Title", 'Age', alpha=.5, ci=None)
grid.add_legend()


# In[47]:


df['Title'] = df['Name'].str.split(',|\\.',expand = True)[1] 
df['Title'] = df['Title'].str.strip()


# In[48]:


dict = {"Capt":       "Officer",
                    "Col":        "Officer",
                    "Major":      "Officer",
                      "Dr":         "Officer",
                    "Rev":        "Officer",
                    "Jonkheer":   "Royalty",
                    "Don":        "Royalty",
                    "Sir" :       "Royalty",
                   "Lady" :      "Royalty",
                  "the Countess": "Royalty",
                    "Dona":       "Royalty",
                    "Mme":        "Miss",
                    "Mlle":       "Miss",
                    "Miss" :      "Miss",
                    "Ms":         "Mrs",
                    "Mr" :        "Mrs",
                    "Mrs" :       "Mrs",
                    "Master" :    "Master" }


# In[49]:


df["Title"] = df["Title"].map(dict)


# In[50]:


print(df['Title'].value_counts())


# In[51]:


g = sns.catplot(x = "Title", y = "Survived", data = df, kind = "bar")
g.set_xticklabels(["Master","Female's","Male's","Office","Royalty"])
g.set_ylabels("Survival Probability")
plt.show()


# In[52]:


df.groupby(by="Title").agg(Survived_rates=("Survived","mean")).plot(kind='bar')


# In[53]:


df.groupby(by="Title").agg(age_rates=("Age","mean")).plot(kind='bar')   


# In[54]:


df.groupby(by="Title").agg(Fare_rates=("Fare","mean")).plot(kind='bar')    


# In[55]:


df["FamilySize"] = df["Parch"] + df["SibSp"]
df['Survived'].groupby(df['FamilySize']).mean().plot(kind='bar')


# In[ ]:




