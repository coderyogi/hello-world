# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:59:43 2017
Used for Analyizing portfolios
Generate CSV from SigFig or perhaps consider from Morning Star

@author: jamesbond
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('c:/users/mallu/Downloads/Dividend.csv',usecols=['Symbol', 'Shares', 'Last', 'Cost Basis/Share',
                                                                             'Gain/Loss', 'Value'])
df=df.fillna(0)
#print(df)

labels = df['Symbol']
sizes = df['Value']/df['Value'].sum()
#print(sizes)
plt.pie

plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

fig = plt.gcf()
fig.set_size_inches(12,12) # or (4,4) or (5,5) or whatever

plt.show()
#print(labels)

df = pd.read_csv('c:/users/mallu/Downloads/Long Term.csv',usecols=['Symbol', 'Shares', 'Last', 'Cost Basis/Share',
                                                                             'Gain/Loss', 'Value'])
df=df.fillna(0)
#print(df)

labels = df['Symbol']
sizes = df['Value']/df['Value'].sum()
#print(sizes)
plt.pie

plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

fig = plt.gcf()
fig.set_size_inches(12,12) # or (4,4) or (5,5) or whatever

plt.show()
#print(labels)
