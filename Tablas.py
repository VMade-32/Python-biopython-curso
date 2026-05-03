import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://docs.google.com/spreadsheets/d/1E3p5YqqQ72HsO1G6foUAmdvA_hBkA0eM8Zydr1r2ZYk/export?format=csv")
print(df['area_conocimiento'].value_counts())
print(df['diciplina'].value_counts())

fig, ax = plt.subplots(figsize=(10,5))
ax.pie(df['area_conocimiento'].value_counts(), labels=df['area_conocimiento'].value_counts().index, autopct='%1.1f%%')
plt.show()

fig, ax = plt.subplots(figsize=(10,5))
ax.pie(df['diciplina'].value_counts(), labels=df['diciplina'].value_counts().index, autopct='%1.1f%%')
plt.show()