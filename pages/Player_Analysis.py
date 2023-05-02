import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from data.index import male_cricket , female_cricket , countries , players_list
from Components.Comparison.CountryVsCountry import Compare,General
from Helpers.Global import filtered_bowler , bats

st.sidebar.success("Select a player")

player = st.sidebar.selectbox("" , options=players_list)

st.title(player)

country = None
bt = bats[bats['batsman_name'] == player]
if not bt.empty:
    country = bt.country.iloc[0]
    st.subheader("Batting Stats")
    st.table(bt)



bs = filtered_bowler[filtered_bowler['bowler'] == player]
if not bs.empty:
    country = bs.bowler_nation.iloc[0]
    st.subheader("Bowling Stats")
    st.table(bs)

st.title("Country : " + country)