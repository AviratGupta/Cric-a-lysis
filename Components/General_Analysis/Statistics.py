import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Statistics:

    def __init__(self , data , title) -> None:
        self.data = data
        self.title = title

    def stats(self):

        st.title(f"Statistics for {self.title}")

        batsman_female = len(pd.concat([self.data['batsman_name'],self.data['non_striker']] , axis=0).unique())
        bowler_female = len(self.data['bowler'].unique())
        venues = len(self.data['venue'].unique())
        teams = len(self.data['team_name'].unique())
        matches = len(self.data['mergeid'].unique())


        col1 , col2 , col3 = st.columns(3)

        with col1:
            st.header('# Players')
            st.title(batsman_female+bowler_female)
        with col2:
            st.header('# Batsman')
            st.title(batsman_female)
        with col3:
            st.header('# Bowlers')
            st.title(bowler_female)

        col1 , col2 , col3 = st.columns(3)

        with col1:
            st.header('# Venues')
            st.title(venues)
        with col2:
            st.header('# Teams')
            st.title(teams)
        with col3:
            st.header('# Matches')
            st.title(matches)