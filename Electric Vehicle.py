#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv(r"C:\Users\k.anandhasagar\Downloads\dataset.csv")
data


# In[3]:


data.info()


# In[4]:


data.describe()


# In[5]:


data.shape


# In[6]:


data.isnull().sum()


# In[7]:


data.shape


# In[8]:


data.dropna(inplace = True)


# In[9]:


data.shape


# ### Univariate analysis

# In[10]:


pip install plotly


# In[11]:


import plotly.express as px


# In[12]:


Ev_type = px.bar(data["Electric Vehicle Type"].value_counts(), title = "Count of Ev Types")
Ev_type.show()


# In[13]:


CAFV_eigibility = px.funnel(data["Clean Alternative Fuel Vehicle (CAFV) Eligibility"].value_counts(), title = "Count of CAFV Eligibility")
CAFV_eigibility.show()


# In[14]:


E_range = px.histogram(data,x="Electric Range",nbins = 30,title = "Distribution of Electric Range")
E_range.show()


# In[15]:


Base_msrp = px.histogram(data, x="Base MSRP", nbins=30, 
                         title="Distribution of Base MSRP", 
                         range_x=[0,210000], 
                         color_discrete_sequence=["#8B9467"]) 
Base_msrp.show()


# In[16]:


company_counts = data['Make'].value_counts().reset_index()
company_counts.columns = ['Company', 'EV Count']
company_counts = company_counts.sort_values(by='EV Count', ascending=False)

fig_bar = px.bar(company_counts, x='Company', y='EV Count', 
                 title='No of Electric Vehicles by Company', 
                 color_discrete_sequence=["teal"]) 

fig_bar.show()


# In[17]:


county_counts = data['County'].value_counts().reset_index()
county_counts.columns = ['County', 'EV Count']
county_counts = county_counts.sort_values(by='EV Count', ascending=False)
fig_bar = px.bar(county_counts, x='County', y='EV Count', title='No of Electric Vehicles by Country')
fig_bar.show()


# In[18]:


data_counts = data['Model Year'].value_counts().reset_index()
data_counts.columns = ['Model Year', 'Count']
data_counts.sort_values(by='Model Year', inplace=True)

fig = px.bar(data_counts, x='Model Year', y='Count', title='Electric Vehicles Count by Model Year', labels={'Model Year': 'Model Year', 'Count': 'Count'})
fig.show()


# In[19]:


ev_type_counts = data['Electric Vehicle Type'].value_counts().reset_index()
ev_type_counts.columns = ['Electric Vehicle Type', 'EV Count']
ev_type_counts = ev_type_counts.sort_values(by='EV Count', ascending=False)

fig_bar = px.bar(ev_type_counts, x='Electric Vehicle Type', y='EV Count', title='No of Electric Vehicles by EV Type')
fig_bar.show()


# In[20]:


electric_utility_counts = data['Electric Utility'].value_counts().reset_index()
electric_utility_counts.columns = ['Electric Utility', 'EV Count']

fig_bar = px.bar(electric_utility_counts, x='Electric Utility', y='EV Count', title='Electric Vehicles Count by Electric Utility')
fig_bar.show()


# ### Bivariate analysis

# In[21]:


scatter_ev_range_msrp = px.scatter(data, x='Electric Range', y='Base MSRP', title='Electric Range vs Base MSRP')
scatter_ev_range_msrp.show()


# In[22]:


scatter_ev_range_model_year = px.scatter(data, x='Model Year', y='Electric Range', title='Electric Range vs Model Year')
scatter_ev_range_model_year.show()


# In[23]:


box_ev_type_range = px.box(data, x='Electric Vehicle Type', y='Electric Range', title='Electric Vehicle Type vs Electric Range')
box_ev_type_range.show()


# In[24]:


scatter_model_year_ev_count = px.scatter(data['Model Year'].value_counts(), title='No of Electric Vehicles by Model Year')
scatter_model_year_ev_count.show()


# In[25]:


box = px.box(data, x='Electric Vehicle Type', y='Base MSRP', title='Electric Vehicle Type vs Base MSRP')
box.show()


# In[26]:


scatter_model_year = px.scatter(data, x='Model Year', y='Base MSRP', title='Model Year vs Base MSRP')
scatter_model_year.show()


# In[27]:


box_ev_type = px.violin(data, x='Electric Vehicle Type', y='Electric Range', title='Electric Vehicle Type vs Electric Range')
box_ev_type.show()


# In[28]:


fig_box = px.box(data, x='Clean Alternative Fuel Vehicle (CAFV) Eligibility', y='Electric Range',
                 title='Clean Alternative Fuel Vehicle (CAFV) Eligibility vs Electric Range',
                 labels={'Clean Alternative Fuel Vehicle (CAFV) Eligibility': 'CAFV Eligibility',
                         'Electric Range': 'Electric Range (miles)'})

fig_box.show()


# In[29]:


mean_electric_range = data.groupby('Model Year')['Electric Range'].mean().reset_index()

fig_line = px.line(mean_electric_range, x='Model Year', y='Electric Range', title='Model Year vs Mean Electric Range',
                   labels={'Model Year': 'Model Year', 'Electric Range': 'Mean Electric Range (miles)'})

fig_line.show()


# In[30]:


df_counts = data.groupby(['Model Year', 'Electric Vehicle Type']).size().reset_index(name='Count')

fig_bar = px.histogram(df_counts, x='Model Year', y='Count', color='Electric Vehicle Type',
                 title='Count of Different Electric Vehicle Types by Model Year')

fig_bar.show()


# In[31]:


ev_count_by_pincode = data.groupby(['Postal Code', 'Model Year', 'State']).size().reset_index(name='Number_of_EV_Vehicles')


# In[32]:


state_data = ev_count_by_pincode[ev_count_by_pincode['State'] == 'WA']


# ## Task 2

# In[33]:


fig = px.choropleth_mapbox(state_data,
                           geojson="https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/wa_washington_zip_codes_geo.min.json",
                           locations='Postal Code',
                           color='Number_of_EV_Vehicles',
                           featureidkey="properties.ZCTA5CE10",  
                           mapbox_style="carto-positron",
                           zoom=5,  # Adjust zoom level
                           center={"lat": 47.7511, "lon": -120.7401}, 
                           title="Number of EV vehicles based on location Washington Over Time",
                           animation_frame="Model Year",  
                           color_continuous_scale="Cividis",
                           hover_data=['Number_of_EV_Vehicles']  
                          )

# Update layout for better fit and aesthetics
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the animated map
fig.show()


# ## Task 3

# In[41]:


get_ipython().system('pip install bar-chart-race')


# In[35]:


import bar_chart_race as bcr


# In[36]:


df = data.groupby(['Make', 'Model Year']).size().reset_index(name='Number_of_Vehicles')


# In[37]:


import plotly.express as px
fig = px.bar(df,
             y='Make',
             x='Number_of_Vehicles',
             animation_frame='Model Year',
             orientation='h',
             title='EV Makes and their Count Over the Years',
             labels={'Number_of_Vehicles': 'Number of EV Vehicles'},
             range_x=[0, 3000],
             color='Make', 
             color_discrete_map={
                 'Tesla': 'red',
                 'Toyota': 'blue',
                 'Ford': 'green',
             }
             )

# Find the year with the highest number of vehicles
top_year = df['Model Year'].max()

# Check if the year exists and add the annotation
if (df['Model Year'] == top_year).any():
    make_2023 = df.loc[df['Model Year'] == top_year, 'Make'].iloc[0]
    fig.add_annotation(x=2500, y=make_2023,
                       text=f"Most EVs: {top_year}",
                       showarrow=False,
                       font_size=18)
else:
    print("Year 2023 not found in data")

# Customize the layout
fig.update_layout(
    xaxis=dict(showgrid=True, gridcolor='LightGray'),
    yaxis_title='EV Makes',
    xaxis_title='Number of EV Vehicles',
    showlegend=False,
    title_x=0.5,
    title_font=dict(size=20),
    margin=dict(l=50, r=50, t=50, b=50),
    width=800,
    height=600
)

# Customize trace appearance
fig.update_traces(texttemplate='%{x}',
                  textposition='outside',
                  textfont_size=16)

# Show the plot
fig.show()


# In[ ]:




