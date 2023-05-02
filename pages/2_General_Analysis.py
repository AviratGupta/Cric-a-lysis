import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Data importing 
from data.index import t20_matches,personal_male

# Helper Importing
from Helpers.General_Analysis import  Male , Female , All


option = st.sidebar.selectbox("Select gender 😊" , ('All' , 'Male' , 'Female'))


if option == 'All':
    All.all()
elif option == 'Male':
    Male.male()
elif option == 'Female':
    Female.female()
else:
    st.title("Not Valid")






















# st.title("Analysis")


# batsman_male = personal_male[ personal_male['battingStyle'].notnull()]


# st.subheader("Players in a country")
# fig,ax = plt.subplots(figsize=(10,10))
# ax = sns.countplot(data= personal_male , y='nationalTeam' , order=personal_male['nationalTeam'].value_counts().index )
# ax.set_xticklabels(ax.get_xticklabels() , rotation=90)
# for p in ax.patches:
#     val = "{}".format(p.get_width())
#     width,height = p.get_width()  , p.get_height()
#     x=width+3
    
#     y=p.get_y()+height/2+0.1
#     ax.annotate(val,(x,y))

# plt.xlabel("National Team" , fontsize=20)
# plt.ylabel("Count" , fontsize=20)
# st.pyplot(fig) 


# st.dataframe(data=personal_male['nationalTeam'].value_counts().reset_index().rename(columns={'index' : 'Country' , 'nationalTeam' : 'Count of players'}))


# st.subheader("Left v/s Right Batsman")
# fig, ax = plt.subplots(figsize=(3,3))
# ax.pie( personal_male.battingStyle.value_counts().tolist(), labels = personal_male.battingStyle.value_counts().index.tolist() , autopct='%.0f%%' , explode=[0,0.1])
# plt.title("Batsman left/right pie chart")
# st.pyplot(fig)


# st.subheader("Country wise")

# country_style_batsman = batsman_male.groupby(['nationalTeam' , 'battingStyle']).count()['dob'].reset_index().rename(columns={'nationalTeam' : 'country' , 'dob' : 'count'})
# fig, ax = plt.subplots()
# ax = sns.barplot(x='country' , y ='count',hue="battingStyle" , data=country_style_batsman  )
# plt.xticks(rotation=90)
# st.pyplot(fig)


