#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install keplergl')


# In[2]:


import pandas as pd
import geopandas as gpd
import keplergl


# In[ ]:


kepler_config = 


# In[3]:


df_BikeShares = pd.read_csv("2019_Pace_BikeActivity_Data.csv")
df_BikeShares.head()


# In[5]:


# lat and lon to numeric, errors converted to nan
df_BikeShares['longitude'] = pd.to_numeric(df_BikeShares.longitude, errors='coerce')
df_BikeShares['latitude'] = pd.to_numeric(df_BikeShares.latitude, errors='coerce')


# In[7]:


# Configure the Kepler map visualization
kepler_map = keplergl.KeplerGl(height=400) # more map configs can be added for easier view
kepler_map

# Add data to map
kepler_map.add_data(data=df_BikeShares, name="Pace_BikeShare_Data")


# In[8]:


# Generate the map indexes
kepler_map


# In[21]:


# Generate the visualization and save as local HTML file
kepler_map.save_to_html(file_name='Pace_BikeShare_Data.html', 
                        data={"Pace_BikeShare_Data": file})


# In[ ]:





# In[ ]:




