import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from Components.General_Analysis.Analysis import Batsman_Scatter
from data.index import male_cricket


def BatsmanVsBatsman(batsman , data):


    st.title("Male Batsman Info")



    top = data[data['batsman_name'].isin(batsman)]
    top = top.groupby(['batsman_name' , 'batsman_run']).count()['inning'].reset_index().rename(columns={'inning' : 'count'})
    plt.rcParams['figure.figsize'] = 11.7,8.27
    figure,ax = plt.subplots(2,2 , figsize=(10 ,8))


    figure.tight_layout(h_pad=4 , w_pad=13)
    #One's
    ones = top[top['batsman_run'] == 1].sort_values(by='count')
    o = sns.barplot(data=ones , ax = ax[0][0] , y='batsman_name' , x = 'count' , color='#86efac')
    ax[0][0].set_title('One\'s' , fontsize=20)

    #Two's
    twos = top[top['batsman_run'] == 2].sort_values(by='count')
    o = sns.barplot(data=twos , ax = ax[0][1] , y='batsman_name' , x = 'count' , color='#fde047')
    ax[0][1].set_title('Two\'s' , fontsize=20)

    #Four's
    fours = top[top['batsman_run'] == 4].sort_values(by='count')
    o = sns.barplot(data=fours , ax = ax[1][0] , y='batsman_name' , x = 'count' , color= '#67e8f9')
    ax[1][0].set_title('Four\'s' , fontsize=20)

    #Six's
    sixes = top[top['batsman_run'] == 4].sort_values(by='count')
    o = sns.barplot(data=sixes , ax = ax[1][1] , y='batsman_name' , x = 'count' , color='#fda4af')
    ax[1][1].set_title('Six\'s' , fontsize=20)

    st.pyplot(figure)

    # fig = plt.figure()
    fig, ax = plt.subplots(figsize=(16, 9))
    top.groupby(['batsman_name' ,'batsman_run'])['count'].first().unstack().drop(columns=[0,3]).plot(stacked=True , ax=ax , kind='barh')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.xlabel(xlabel='Count')
    plt.ylabel(ylabel='Batsman Name')
    plt.title("Stacked Representation")
    st.pyplot(fig)

    st.header("Scatter plot")

    scatter = Batsman_Scatter(male_cricket)
    scatter.Dot_Plot(batsman)
    scatter.Line_Plot(batsman)
    scatter.Swarm_Plot(batsman)
    scatter.Show_Stats(batsman)
