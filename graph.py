#!/bin/python3
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 


# Modifiable variables
transactions = 25

# Import data
data = pd.read_csv('./bk_download.csv')
#data.head()
df = pd.DataFrame(data)

# Define data points 
category_dict = df.head(transactions).groupby('Category')['Amount'].sum().to_dict()
category = list(category_dict.keys())
amount = list(category_dict.values())

# configure graph dimensions
fig, ax = plt.subplots(figsize = (15,10))

#ax.barh(keys, values)
ax.barh(category, amount)

# Remove axes spines
#for s in ['top', 'bottom', 'left', 'right']:
#    ax.spines[s].set_visible(False)



# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 5)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
    linestyle ='-.', linewidth = 0.5,
    alpha = 0.2)
 
# Show top values 
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.5, i.get_y()+0.5, 
        str(round((i.get_width()), 2)),
        fontsize = 10, fontweight ='regular',
        color ='red')

# Add Plot Title
ax.set_title('Previous 25 financial transactions\n~ Kenneth (AKA Davis CFO and python extraordinaire)',
    loc ='left', )
 
# Add Text watermark
fig.text(0.9, 0.15, 'Davis Incorporated', fontsize = 12,
    color ='grey', ha ='right', va ='bottom',
    alpha = 0.7)
######################################################

#plt.bar(x, height, width, bottom, align)
#plt.bar(category, amount)
plt.show().tight_layout()













#--------------- Interesting ----------------------

# Common data points
#mean = data['column_name'].mean()
#median = data['column_name'].median()
#std_dev = data['column_name'].std()

# Filtering data by amounts; scatter plots
#filtered_data = data.loc[data['column_name'] > 10]
