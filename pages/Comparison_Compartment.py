import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data.index import male_cricket , female_cricket , countries , t20
from Components.Comparison.CountryVsCountry import Compare,General
from Components.Comparison.BatsmanVsBatsman import BatsmanVsBatsman

from Helpers.Global import filtered_bowler

gender_data = male_cricket
batsman_list = None
bowlers_list = None

# countries = mat

st.title("Player comparison")

st.header("Batsman v/s Bowler")
col1,col2,col3 = st.columns(3)

with col1 :
    gender = st.selectbox("Choose Gender" , options=['Male' , 'Female'])
    gender_data = male_cricket if gender == 'Male' else female_cricket
    batsman_list = gender_data.batsman_name.unique().tolist()
    bowlers_list = gender_data.bowler.unique().tolist()
with col2:
    batsman = st.selectbox("Choose Batsman" , options=batsman_list)
    
with col3:
    bowler = st.selectbox("Choose Bowler" , options=bowlers_list)

def Batsman_Bowler(bat , ball):
    data = gender_data.groupby(['batsman_name' , 'bowler' , 'year','batsman_run']).count()['inning'].rename("count").to_frame()
    data = data.reset_index()
    bowled = [ 'caught', 'bowled',  'caught and bowled', 'lbw','stumped', 'hit wicket']
    dismissed = gender_data[gender_data['dismissal_kind'].isin(bowled)]
    b = dismissed.groupby(['bowler' , 'batsman_name' , 'year','dismissal_kind'] ).count()['inning'].to_frame().rename(columns={'inning' : 'count'}).reset_index()
    t = data[(data['batsman_name'] == bat) & (data['bowler'] == ball)]
    u = t.groupby(['batsman_name' , 'bowler' , 'batsman_run']).sum()['count'].to_frame().reset_index(level=2)
    te = b[(b['bowler'] == ball)&(b['batsman_name'] == bat)]
    bu = te.groupby([ 'bowler', 'batsman_name' , 'dismissal_kind']).sum().reset_index()

    plt.suptitle(f"{bat} v/s {ball}"  , fontsize=30 , y=1.01 , x=0.60)
    figure , ax = plt.subplots(2,2)



    if t.empty and te.empty:
        st.header("No data available 🙂")
        return
        
    if t.empty:
        st.header("No runs...")
    else : 
        plt.title("Barchat" , fontsize=20 , y=1.01)
        sns.barplot(x= 'year' , y='count' , hue='batsman_run' , data=t , ax=ax[0][0] )

        ax1 = plt.subplot2grid((2,2),(0,1))
        ax1.set_title("Batsman run",fontsize=20)
        plt.pie(x = 'count' , data=u , labels=u['batsman_run'] , autopct='%1.1f%%')
    
    if te.empty:
        st.header("Not Out...")
    else:
        sns.barplot(y = 'count' , hue='dismissal_kind' ,  x='year' , data=te , ax=ax[1][0])

        ax2 = plt.subplot2grid((2,2),(1,1))
        plt.title("Dismissal Kind piechart" , fontsize=20)
        plt.pie(x = 'count' , data=bu , labels=bu['dismissal_kind'] , autopct='%1.1f%%')

    plt.subplots_adjust(left=0.1,bottom=0.1,right=1.2,top=0.9,wspace=0.01,hspace=0.4)
    st.pyplot(figure)




Batsman_Bowler(batsman , bowler)


st.header("Batsman v/s Batsman")

count = 30
top_batsman = t20.groupby(['batsman_name']).sum().sort_values(by='batsman_run' , ascending=False).drop(columns=['win_with','total_run' , 'mergeid' , 'extra_run' , 'over_num' ,'inning' , 'year']).head(count).reset_index().batsman_name.tolist()
batsman_selected = st.multiselect("Select the crickers" , options=top_batsman)

if batsman_selected:
    BatsmanVsBatsman(batsman=batsman_selected , data=t20)

st.header("Bowler v/s Bowler")
selected_bowler = st.multiselect("select the bowler",  options=filtered_bowler.bowler.unique().tolist())
def Marker(name=[]):
    fig = plt.figure(figsize=(10,5))
    sns.scatterplot(x='wickets' , y='economy' , data=filtered_bowler[:90] , size='wickets' , hue='bowler_nation' , sizes=(20,100))
    def Helper(test):
        ecn,wkt,bwlr = test
        plt.text(x=wkt, y=ecn+0.1 ,s=bwlr,fontsize=10 )
    if name:
        filtered_bowler[filtered_bowler['bowler'].isin(name)][['economy' , 'wickets' , 'bowler']].apply(Helper , axis=1)
    

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    st.pyplot(fig)

if selected_bowler:
    Marker(selected_bowler)
    st.table(filtered_bowler[filtered_bowler.bowler.isin(selected_bowler)])

 


st.title("Country v/s Country")

col1,col2 = st.columns(2)

with col1:
    country1 = st.selectbox("Select country 1" , options=countries)

with col2:
    country2 = st.selectbox("Select country 2" , options=[x for x in countries if x != country1])

st.header("Face to Face Stats")
# WinNTossCountry(country1 , country2)
Compare(country1 , country2)
General(country1 , country2)




