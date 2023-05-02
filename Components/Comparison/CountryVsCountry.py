import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data.index import matches

# def WinNTossCountry(country1 , country2):
#     cond  = np.where(((matches['team_1'] == country1 )&(matches['team_2'] == country2)) | ((matches['team_1'] == country2 )&(matches['team_2'] == country1)) , True , False )
#     data = matches[cond]
#     if data.empty : 
#         st.title("No matches...")
#         return
#     st.subheader("Win - Loss Data")
#     toss_data = pd.DataFrame( np.where(data['toss_winner'] == country1 , country1 , country2 )).value_counts().to_frame().rename(columns={0 : 'count'}).reset_index().rename(columns={0 : 'country'})
#     win_data = pd.DataFrame( np.where(data['result'] == country1 , country1 , country2)).value_counts().to_frame().rename(columns={0 : 'count'}).reset_index().rename(columns={0 : 'country'})
#     figure , ax = plt.subplots(1,2)
#     ax[0].set_title("Toss ratio")
#     ax[0].set_xlabel("Countries")
#     sns.barplot(y = 'count' ,  x='country' , data=toss_data , ax=ax[0])

#     ax[1].set_title("Win ratio")
#     ax[1].set_xlabel("Countries")
#     sns.barplot(y = 'count' ,  x='country' , data=win_data , ax=ax[1])


#     st.pyplot(fig=figure)

def Compare(c1,c2):
    m = matches[((matches['team_1'] == c1) | (matches['team_2'] == c1)) & ((matches['team_1'] == c2) | (matches['team_2'] == c2))]
    figure , ax = plt.subplots(1,2)
    # fig = plt.figure(figsize=(8,5))
    sns.countplot(data=m , x='result' , order=[c1,c2] , ax = ax[0])
    ax[0].set_title(f"{c1} vs {c2}" , fontsize=25)


    # fig = plt.figure(figsize=(8,5))
    sns.countplot(data=m , x='toss_winner' , order=[c1,c2] , ax=ax[1])
    ax[1].set_title(f"{c1} vs {c2}" , fontsize=25)

    st.pyplot(fig=figure)


def General(c1,c2):
    m = matches[((matches['team_1'] == c1) | (matches['team_2'] == c1)) & ((matches['team_1'] == c2) | (matches['team_2'] == c2))]
    st.table(m.result.value_counts().to_frame())
    col1,col2= st.columns(2)
    with col1 : 
        st.header("# Matches")
        st.subheader(m.shape[0])
    with col2 : 
        st.header("Venues list")
        st.dataframe(m.venue.value_counts().to_frame())

