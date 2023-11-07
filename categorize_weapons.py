#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import math


# In[50]:


df = pd.read_csv('Police_Arrests_&_Incidents_Clean.csv')
pd.set_option('display.max_columns', None)


# In[19]:


unarmed = ['Unarmed', math.nan, 'THREATS']
firearm = ['Handgun', 'Firearm (Type Not Stated)', 'Gun', 'Other Firearm', 'Shotgun ']
knife = ['Knife - Pocket', 'Knife - Butcher', 'Knife - Other']
other_melee = ['Club', 'Stabbing Instrument', 'Lethal Cutting Instrument']
other = ['Other', 'Drugs', 'Vehicle', 'Rock', 'Poison', 'Burn', 'Missle/Arrow', 'Explosives ']
hands_feet = ['Hands/Feet', 'Strangulation']


# In[26]:


df.replace(to_replace=unarmed, value='unarmed', inplace=True)
df.replace(to_replace=firearm, value='firearm', inplace=True)
df.replace(to_replace=knife, value='knife', inplace=True)
df.replace(to_replace=other_melee, value='other melee', inplace=True)
df.replace(to_replace=other, value='other', inplace=True)
df.replace(to_replace=hands_feet, value='hands/ feet', inplace=True)


# In[49]:


def categorize_weapon(row):
    weapon_types = {'unarmed': 0, 'firearm': 1, 'knife': 2, 'other melee': 3, 'other': 4, 'hands/ feet': 5}
    weapon_type = row['ArWeapon']
    if weapon_type not in weapon_types:
        return math.nan
    return weapon_types[weapon_type]

df['WeaponCategory'] = df.apply(func=categorize_weapon, axis=1)


# In[ ]:




