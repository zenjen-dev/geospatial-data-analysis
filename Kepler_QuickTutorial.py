#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install keplergl')


# In[2]:

# Run imports
import pandas as pd
import geopandas as gpd
import keplergl



# In[3]:


df = pd.read_csv("YOUR_FILE_HERE.csv") # KEPLER.GL CAN READ GeoJSON, JSON, CSV
df.head()


# In[5]:


# lat and lon to numeric, errors converted to nan
df['longitude'] = pd.to_numeric(df_BikeShares.longitude, errors='coerce')
df['latitude'] = pd.to_numeric(df_BikeShares.latitude, errors='coerce')


# In[7]:


# Configure the Kepler map visualization
kepler_map = keplergl.KeplerGl(height=400) # more map configs can be added for easier view
kepler_map

# Add data to map
kepler_map.add_data(data=df, name="NAME_OF_ANALYSIS")


# In[8]:


# Generate the map indexes
kepler_map


# In[21]:


# Generate the visualization and save as local HTML file
kepler_map.save_to_html(file_name='NAME_OF_FILE.html', 
                        data={"NAME_OF_ANALYSIS": file})






