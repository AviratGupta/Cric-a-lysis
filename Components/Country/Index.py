import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from data.index import matches

def WinNToss(name):
    country = matches[(matches['team_1'] == name) | (matches['team_2'] == name)]
    st.subheader("Win - Loss Data")
    toss_data = pd.DataFrame( np.where(country['toss_winner'] == name , 'win' , 'loss' )).value_counts().to_frame().rename(columns={0 : 'count'})
    win_data = pd.DataFrame( np.where(country['result'] == name , 'win' , 'loss' )).value_counts().to_frame().rename(columns={0 : 'count'})
    figure , ax = plt.subplots(1,2)

    ax1 = plt.subplot2grid((1,2),(0,0))
    plt.pie(x='count' , data=win_data , autopct='%1.1f%%' , labels=['win' , 'loss'])
    ax1.set_xlabel("Win Data" , fontsize=20)
    

    ax2 = plt.subplot2grid((1,2),(0,1))
    plt.pie(x='count' , data=toss_data , autopct='%1.1f%%' , labels=['win' , 'loss'])
    ax2.set_xlabel("Toss Data" , fontsize=20)

    st.pyplot(fig=figure)