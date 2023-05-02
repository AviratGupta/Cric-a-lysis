import streamlit as st
import numpy as np

from data.index import top_countries , matches , t20

st.sidebar.success("Select a country and gender for detailed analysis")
country = st.sidebar.selectbox("Select Country" , options=top_countries)
gender = st.sidebar.selectbox("Select Gender" , options=[ "Both" ,  "Male" , "Female"])

if gender != 'Both':
    cond_matches = np.where((( matches['team_1'] == country ) | ( matches['team_2'] == country ) ) & (matches['gender'] == gender.lower())  , True , False)
    cond_t20 = np.where((( t20['team_1'] == country ) | ( t20['team_2'] == country ) ) & (t20['gender'] == gender.lower())  , True , False)
else:
    cond_matches = np.where((( matches['team_1'] == country ) | ( matches['team_2'] == country ) )  , True , False)
    cond_t20 = np.where(( t20['team_1'] == country ) | ( t20['team_2'] == country )   , True , False)

m = matches[cond_matches]
t = t20[cond_t20]


from Helper import Detailed_Analysis


Detailed_Analysis(match=m , t20=t , gender_name=f"{country} {gender}" , top_countries=[])




