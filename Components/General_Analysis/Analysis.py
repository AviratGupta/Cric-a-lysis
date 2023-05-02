import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from data.index import male_matches, male_top_countries
from Constants import BALL_MALE_COUNT


class Analysis:
    def __init__(self , data) -> None:
        pass

# male_matches['year'] = male_matches['date'].apply(lambda x : x.split("-")[0])
# elected_wrt_year = male_matches.groupby(['year' , 'elected_first']).count()['city'].reset_index().rename(columns= {'city' : 'count'})

# fig, ax = plt.figure(figsize=(20,10))
# p = sns.color_palette("Paired")
# sns.barplot(x='year' , y='count' , hue='elected_first' , data=elected_wrt_year , palette=p)
# plt.title("Toss Decision w.r.t each year" , fontsize=30)
# st.pyplot(fig=fig)

class Batsman_Scatter:
    def __init__(self , data) -> None:
        self.data = data
        self.batsman_nation = self.data[['team_name' ,'batsman_name']].value_counts().to_frame().reset_index().drop(columns=[0])
        self.filtered_batsman_nation = self.batsman_nation.drop_duplicates(subset='batsman_name')
        self.filtered_batsman_nation = self.filtered_batsman_nation.rename(columns={'team_name' : 'country' , 'batsman_name' : 'name'})
        self.filtered_batsman_nation = self.filtered_batsman_nation[self.filtered_batsman_nation['country'].isin(male_top_countries)]
        self.batsman_info = self.data.groupby('batsman_name').sum()['batsman_run'].reset_index()
        temp= self.data[~self.data['extra_type'].isin(['wides', 'penalty'])].groupby('batsman_name').count()['inning'].reset_index().rename(columns={'inning' : 'balls'})
        self.batsman_info = self.batsman_info.merge(temp , on='batsman_name' )
        self.bats= self.batsman_info.merge(self.filtered_batsman_nation, left_on='batsman_name' , right_on='name' , how='left').dropna()
        self.bats = self.bats.drop(columns=['name'])
        self.bats['strike_rate'] = round((self.bats['batsman_run']/self.bats['balls'])*100 , 2)
        self.top_bats_stats = self.bats[self.bats['balls'] > BALL_MALE_COUNT]

    def Dot_Plot(self,name=[]):
        st.header("2-D Scatterplot")
        figure = plt.figure(figsize=(15,8))
        sns.scatterplot(x='balls' , y='strike_rate' , data=self.top_bats_stats , size='balls' , hue='country' , sizes=(20,100))
        def Helper(test):
            balls,strike,name = test
            plt.text(x=balls, y=strike+.5 ,s=name,fontsize=10 )
        if name:
            self.top_bats_stats[self.top_bats_stats['batsman_name'].isin(name)][['balls' , 'strike_rate' , 'batsman_name']].apply(Helper , axis=1)
        

        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.ylabel("# Strike Rate" , fontsize=22)
        plt.xlabel("# Balls" , fontsize=22)
        st.pyplot(figure)
        

    def Line_Plot(self , name=[]):
        batsman_year_performance = self.data.groupby(['batsman_name' , 'year']).sum()['batsman_run'].reset_index()
        d = batsman_year_performance[batsman_year_performance['batsman_name'].isin(name)]
        fig = plt.figure(figsize=(20,10))
        sns.lineplot(data=d , x='year' , y='batsman_run' , hue='batsman_name' , marker='o')
        st.pyplot(fig)

    def Swarm_Plot(self , name=[]):
        swarm = self.data.groupby(['mergeid' , 'batsman_name']).sum()['batsman_run'].reset_index(level=1).reset_index(drop=True)
        temp = swarm[swarm['batsman_name'].isin(name)]
        highest = temp.groupby('batsman_name').max().rename(columns={'batsman_run' : 'Highest Score'})
        fig = plt.figure(figsize=(13,7))
        sns.swarmplot(x='batsman_name' , y='batsman_run' , data= temp)
        st.table(highest)
        plt.ylabel("Runs" , fontsize=23) 
        plt.xlabel("Name" , fontsize=23) 
        st.pyplot(fig)
    
    def Show_Stats(self , batsman=[]):
        if batsman:
            with st.expander("Show Batsman Stats"):
                st.table(self.top_bats_stats[self.top_bats_stats.batsman_name.isin(batsman)])
        else:
            with st.expander("Show Batsman Stats"):
                st.table(self.top_bats_stats)

    
    # def Show_Stats(self):
    #     with st.expander("Show Batsman Stats"):
    #         st.table(self.top_bats_stats)
        