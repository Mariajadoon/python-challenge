
# coding: utf-8

# In[8]:


# Dependencies
import pandas as pd


# In[10]:


# Save path to data set in a variable
data_file = "Resources/election_data.csv"


# In[11]:


# Use Pandas to read data
data_file_pd = pd.read_csv(data_file)
data_file_pd.head()


# In[12]:


data_file_pd.describe()


# In[13]:


unique = data_file_pd["Candidate"].unique()
unique


# In[36]:


count = data_file_pd["Voter ID"].value_counts()
total_votes = len(count)
total_votes


# In[18]:


data_file_pd.loc[:, ["Voter ID", "Candidate"]].head()


# In[37]:


only_Khan = data_file_pd.loc[data_file_pd["Candidate"] == "Khan", :]
only_Khan.head()


# In[28]:


count_Khan = only_Khan["Candidate"].value_counts()
count_Khan


# In[40]:


Khan_percentage = (count_Khan/total_votes)*100
Khan_percentage


# In[29]:


only_Correy = data_file_pd.loc[data_file_pd["Candidate"] == "Correy", :]
count_Correy = only_Correy["Candidate"].value_counts()
count_Correy


# In[41]:


Correy_percentage = (count_Correy/total_votes)*100
Correy_percentage


# In[30]:


only_Li = data_file_pd.loc[data_file_pd["Candidate"] == "Li", :]
count_Li = only_Li["Candidate"].value_counts()
count_Li


# In[42]:


Li_percentage = (count_Li/total_votes)*100
Li_percentage


# In[31]:


only_Tooley = data_file_pd.loc[data_file_pd["Candidate"] == "O'Tooley", :]
count_Tooley = only_Tooley["Candidate"].value_counts()
count_Tooley


# In[43]:


Tooley_percentage = (count_Tooley/total_votes)*100
Tooley_percentage


# In[46]:


winner = data_file_pd["Candidate"].mode()
winner


# In[47]:


print("The winner is " + str(winner))

