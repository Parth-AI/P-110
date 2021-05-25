#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd 
import statistics

df = pd.read_csv('medium_data.csv')
ls = df['claps'].to_list()

c_m = statistics.mean(ls)
c_std = statistics.stdev(ls)

print(f'Mean {c_m}')
print(f'Standard Deviation {c_std}')


# In[2]:


import plotly.figure_factory as pff
import random
import plotly.graph_objects as go
import statistics


def random_set_of_mean(counter):
     dataset = []
     for i in range(0, counter):
          random_index = random.randint(0, len(ls)-1)
          value = ls[random_index]
          dataset.append(value)
     mean = statistics.mean(dataset)
     return mean

mean_list = []
for i in range(0, 1000):
     set_of_means = random_set_of_mean(100)
     mean_list.append(set_of_means)

mn_m = statistics.mean(mean_list)
mn_std = statistics.stdev(mean_list)

print(f'Mean of sampling distribution {mn_m}')
print(f'Mean of sampling distribution {mn_std}')


# In[7]:


m_std_first, m_std_end = mn_m - mn_std, mn_m + mn_std
m_std_sec_s, m_std_sec_e = mn_m - (mn_std*2), mn_m + (mn_std*2)
m_std_three_s, m_std_three_e = mn_m - (mn_std*3), mn_m + (mn_std*3)

gph = pff.create_distplot([mean_list], ['Score'], show_hist = False)

gph.add_trace(go.Scatter(x=[m_std_first, m_std_first], y=[0, 0.17], mode = "lines", name = "std 1 s"))
gph.add_trace(go.Scatter(x=[m_std_end, m_std_end], y=[0, 0.17], mode = "lines", name = "std 1 e"))
gph.add_trace(go.Scatter(x=[m_std_sec_s, m_std_sec_s], y=[0, 0.17], mode = "lines", name = "std 2 s"))
gph.add_trace(go.Scatter(x=[m_std_sec_e, m_std_sec_e], y=[0, 0.17], mode = "lines", name = "std 2 e"))
gph.add_trace(go.Scatter(x=[m_std_three_s, m_std_three_s], y=[0, 0.17], mode = "lines", name = "std 3 s"))
gph.add_trace(go.Scatter(x=[m_std_three_e, m_std_three_e], y=[0, 0.17], mode = "lines", name = "std 3 e"))

gph.add_trace(go.Scatter(x=[c_m, c_m], y=[0, 0.17], mode = "lines", name = "Mean 1"))

