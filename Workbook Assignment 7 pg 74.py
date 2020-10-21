#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
names =['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
        columns=['Names','Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[8]:


import matplotlib.pyplot as plt
df.plot()


# In[54]:


df.plot()
displayText = "Wow!"
xloc = 0.05
yloc = 76
xtext = 8
ytext = 150
plt.xlabel('STUDENTS')
plt.ylabel('GRADES')
plt.title('GRADELIST')
plt.yticks([76,77,78,83,95],
         ['76/C','77/C','78/C+','83/B-','95/A'])
plt.xticks([0.0, 1.0, 2.0, 3.0, 4.0],
          ['Bob','Jessica','Mary','John','Mel'])
plt.annotate(displayText,
            xy=(xloc,yloc),
            arrowprops=dict(facecolor='black',
                           shrink=0.05),
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')


# In[24]:





# In[ ]:




