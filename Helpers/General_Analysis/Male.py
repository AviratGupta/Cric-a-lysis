import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from Constants import BALL_MALE_COUNT

from data.index import male_matches
from data.index import male_cricket , male_top_countries
from Components.General_Analysis.Statistics import Statistics
from Components.General_Analysis.Analysis import Batsman_Scatter

from Helper import Detailed_Analysis







def male():
    Detailed_Analysis(t20=male_cricket  , match=male_matches , top_countries=male_top_countries , gender_name='Male' )
    # pass
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # m = Statistics( male_cricket ,'Male')
    # m.stats()
    # st.title("Win types")
    # col1,col2,col3 = st.columns(3)
    # runs =  male_matches[male_matches['win_by'] == 'runs'].shape[0]
    # wickets = male_matches[male_matches['win_by'] == 'wickets'].shape[0]
    # tie = male_matches[male_matches['result'] == 'tie'].shape[0]
    # no_result = male_matches[male_matches['result'] == 'no result'].shape[0]
    # with col1:
    #     st.header("Runs/Wickets")
    #     st.title(f"{runs}/{wickets}")
    # with col2:
    #     st.header("Draw")
    #     st.title(tie)
    # with col3:
    #     st.header("No Result")
    #     st.title(no_result)




    # width = st.sidebar.slider("plot width", 1, 10, 3)
    # height = st.sidebar.slider("plot height", 1, 25, 1)

    # st.title("Toss decision w.r.t each year")

    # male_matches['year'] = male_matches['date'].apply(lambda x : x.split("-")[0])
    # elected_wrt_year = male_matches.groupby(['year' , 'elected_first']).count()['city'].reset_index().rename(columns= {'city' : 'count'})

    # fig, ax = plt.subplots(figsize=(20,10))
    # p = sns.color_palette("Paired")
    # sns.barplot(x='year' , y='count' , hue='elected_first' , data=elected_wrt_year , palette=p)
    # plt.title("Toss Decision w.r.t each year" , fontsize=30)
    # st.pyplot(fig=fig)

    # matches_year = male_matches['year'].unique().tolist()
    # matches_year.insert(0 , 'Overall')
    # year = st.selectbox(label='Select a year' , options=matches_year )


    # if year == 'Overall':

    #     st.title("Overall Toss Decsiion")
    #     fig, ax = plt.subplots(figsize=(9,7))
    #     male_matches['elected_first'].value_counts().plot.pie(autopct='%1.2f%%' , legend=True)
    #     st.pyplot(fig=fig)
    # else :
    #     st.title(f"{year} Toss Decsion")
    #     fig, ax = plt.subplots(figsize=(9,7))
    #     male_matches[male_matches['year'] == year]['elected_first'].value_counts().plot.pie(autopct='%1.2f%%' , legend=True)
    #     st.pyplot(fig=fig)
    
    
    # temp = male_matches
    # c= np.where( male_matches['toss_winner'] == male_matches['result'] , 'win' , 'loss')
    # temp['winner'] = c
    # temp = temp.groupby(['elected_first' , 'winner']).count()['city'].reset_index().rename(columns={'city' : 'count' })

    # col1,col2 = st.columns(2)

    # with col1:
    #     st.table(temp)
    
    # with col2:
    #     g = sns.FacetGrid(temp, col='elected_first' , height=3 , aspect=0.8)
    #     a = g.map(sns.barplot , 'winner' , 'count' , order=['win' , 'loss']  )
    #     st.pyplot(a)


    # st.title("Top 10 stadiums" )
    # fig = plt.figure(figsize=(11,8))
    # male_matches.venue.value_counts().sort_values()[-10:].plot(kind='barh' , color=['orange'])
    # plt.xlabel("Stadium Name")
    # plt.ylabel("Count")
    # st.pyplot(fig)


    # st.title("Trends of 4's and 6's over years" )
    # run = male_cricket.groupby(['year' , 'batsman_run']).count()['inning'].reset_index().rename(columns={'inning' : 'count'})
    # four_six = run[run.batsman_run.isin([4,6])]
    # some = four_six.groupby([four_six.year, 'batsman_run'])['count'].first().unstack()
    # some = some.rename(columns={4 : "4's" , 6 : "6's" })
    # some.index = some.index.astype('str')
    # fig,ax = plt.subplots(figsize=(11,8))
    # some.plot(marker='o' , ax=ax)
    # st.pyplot(fig)
    # with st.expander("Click to read data"):
    #     st.table(some)



    # st.title("Average score of matches per year" )
    # average = male_cricket.groupby([ 'year' , 'mergeid'])['batsman_run'].sum().reset_index().drop(columns=['mergeid'])
    # average['batsman_run'] = average['batsman_run']//2 
    # average = average.groupby(['year']).mean().astype('int')
    # average.reset_index()
    # fig = plt.figure(figsize=(11,7))
    # sns.barplot(data=average.reset_index() , x = 'year'  , y='batsman_run' , color='skyblue')
    # # plt.xticks(rotation=90)
    # plt.ylabel('Average score' , fontsize=20)
    # plt.xlabel('Year' , fontsize=20)
    # st.pyplot(fig)
    # st.dataframe(average)


    # st.title("Inning 1 vs Inning 2 trends")
    # box_plot = male_cricket.groupby([ 'year' , 'mergeid' , 'inning'])['batsman_run'].sum().reset_index().drop(columns=['mergeid'])
    # box_plot = box_plot[box_plot['inning'] < 3]
    # box_plot = box_plot[box_plot['year'] >= 2010]
    # fig = plt.figure(figsize=(20,10))
    # sns.boxplot(data=box_plot , hue='inning', x='year' , y='batsman_run' )
    # st.pyplot(fig)


    # st.title("Find win Matches by # runs")
    # runs = st.slider("select number of runs" , 1,200,1)
    # matches = male_matches[(male_matches['win_by'] == 'runs')&(male_matches['win_with'] == runs)].drop(columns=['mergeid' , 'second_umpire' , 'first_umpire' , 'tv_umpires','winner','win_by' , 'win_with']).reset_index(drop=True)
    # st.text(f"Total count - {matches.shape[0]}")
    # st.dataframe(matches)

    # st.title("Find win Matches by # wickets")
    # wickets = st.slider("select number of runs" , 1,10,1)
    # matches = male_matches[(male_matches['win_by'] == 'wickets')&(male_matches['win_with'] == wickets)].drop(columns=['mergeid' , 'second_umpire' , 'first_umpire' , 'tv_umpires','winner','win_by' , 'win_with']).reset_index(drop=True)
    # st.text(f"Total count - {matches.shape[0]}")
    # st.dataframe(matches)


    # st.title("General stats of Runs / Wickets")
    # filtered_match = male_matches[~male_matches['result'].isin(['no result' , 'tie' , 'Ghana'])]
    # wicket = filtered_match[filtered_match['win_by'] == 'wickets']
    # runs = filtered_match[filtered_match['win_by'] == 'runs']
    # fig = plt.figure(figsize=(13,5))
    # plt.subplot(1,2,1)
    # sns.boxplot(data=wicket , y='win_with' , x='win_by')
    # plt.xlabel(xlabel='')
    # plt.ylabel(ylabel='number of wickets')


    # plt.subplot(1,2,2)
    # sns.boxplot(data=runs , y='win_with' , x='win_by' , color='orange')
    # plt.xlabel(xlabel='')
    # plt.ylabel(ylabel='Runs')

    # st.pyplot(fig)

    # st.header("Stats for wickets and runs")
    # wicket_stats = wicket['win_with'].describe()
    # runs_stats = runs['win_with'].describe()
    # col1,col2 = st.columns(2)
    # with col1:
    #     st.subheader("Wickets")
    #     st.table(wicket_stats)
    # with col2:
    #     st.subheader("Runs")
    #     st.table(runs_stats)


    # st.title("Male Batsman Info")
    # count = st.slider("Select # of batsman" , 3 , 12 , 10)
    # Top_batsman = male_cricket.groupby(['batsman_name']).sum().sort_values(by='batsman_run' , ascending=False).drop(columns=['win_with','total_run' , 'mergeid' , 'extra_run' , 'over_num' ,'inning' , 'year']).head(count).reset_index()
    # top_batsman = Top_batsman.batsman_name.tolist()


    # top = male_cricket[male_cricket['batsman_name'].isin(top_batsman)]
    # top = top.groupby(['batsman_name' , 'batsman_run']).count()['inning'].reset_index().rename(columns={'inning' : 'count'})
    # plt.rcParams['figure.figsize'] = 11.7,8.27
    # figure,ax = plt.subplots(2,2 , figsize=(10 ,8))


    # figure.tight_layout(h_pad=4 , w_pad=13)
    # #One's
    # ones = top[top['batsman_run'] == 1].sort_values(by='count')
    # o = sns.barplot(data=ones , ax = ax[0][0] , y='batsman_name' , x = 'count' , color='#86efac')
    # ax[0][0].set_title('One\'s' , Size=20)

    # #Two's
    # twos = top[top['batsman_run'] == 2].sort_values(by='count')
    # o = sns.barplot(data=twos , ax = ax[0][1] , y='batsman_name' , x = 'count' , color='#fde047')
    # ax[0][1].set_title('Two\'s' , Size=20)

    # #Four's
    # fours = top[top['batsman_run'] == 4].sort_values(by='count')
    # o = sns.barplot(data=fours , ax = ax[1][0] , y='batsman_name' , x = 'count' , color= '#67e8f9')
    # ax[1][0].set_title('Four\'s' , Size=20)

    # #Six's
    # sixes = top[top['batsman_run'] == 4].sort_values(by='count')
    # o = sns.barplot(data=sixes , ax = ax[1][1] , y='batsman_name' , x = 'count' , color='#fda4af')
    # ax[1][1].set_title('Six\'s' , Size=20)

    # st.pyplot(figure)

    # # fig = plt.figure()
    # fig, ax = plt.subplots(figsize=(16, 9))
    # top.groupby(['batsman_name' ,'batsman_run'])['count'].first().unstack().drop(columns=[0,3,5]).plot(stacked=True , ax=ax , kind='barh')
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    # plt.xlabel(xlabel='Count')
    # plt.ylabel(ylabel='Batsman Name')
    # plt.title("Stacked Representation")
    # st.pyplot(fig)

    # st.header("Scatter plot")
    # count = 30
    # top_batsman = male_cricket.groupby(['batsman_name']).sum().sort_values(by='batsman_run' , ascending=False).drop(columns=['win_with','total_run' , 'mergeid' , 'extra_run' , 'over_num' ,'inning' , 'year']).head(count).reset_index().batsman_name.tolist()
    # batsman_selected = st.multiselect("Select the crickers" , options=top_batsman)
    # scatter = Batsman_Scatter(male_cricket)
    # scatter.Dot_Plot(batsman_selected)
    # if batsman_selected:
    #     scatter.Line_Plot(batsman_selected)
    #     scatter.Swarm_Plot(batsman_selected)
    # scatter.Show_Stats()

    # st.title("Histogram of Batsman")
    # fig,ax = plt.subplots(figsize=(10,8))
    # swarm = male_cricket.groupby(['mergeid' , 'batsman_name']).sum()['batsman_run'].reset_index(level=1).reset_index(drop=True)
    # swarm.plot.hist(bins=50 , color='#0ff0ff' , ax=ax)
    # plt.axvline(swarm['batsman_run'].mean() , color='b' , linewidth =3 , linestyle = ':')
    # plt.xlabel('Runs')
    # plt.ylabel('Count')
    # st.pyplot(fig)
    
    # st.title("Umpires Data")
    # field_umpire = male_matches[['first_umpire' , 'second_umpire']]
    # field_umpire = field_umpire['first_umpire'].append(field_umpire['second_umpire'] ).to_frame().rename(columns={0:'name'})
    # field_umpire = field_umpire.value_counts()[:10].to_frame().rename(columns={0:'count'}).reset_index()

    # third_umpire = male_matches['tv_umpires']
    # third_umpire= third_umpire.value_counts().to_frame().reset_index().rename(columns={'tv_umpires':'count' , 'index' : 'name'})

    # fig,ax = plt.subplots(1,2, figsize=(13, 5))

    # fig.tight_layout(w_pad=10)

    # sns.barplot(x='count' , y='name' , data=field_umpire , palette=sns.color_palette('RdYlGn',20) , ax=ax[0])
    # ax[0].set_title("Top 10 Field Umpires" , fontsize=25)
    # ax[0].set_xlabel("Number of matches")

    # sns.barplot(x='count' , y='name' , data=third_umpire[:10] , palette=sns.color_palette('RdYlGn',20) , ax=ax[1])
    # ax[1].set_title("Top 10 Third (T.V) Umpires" , fontsize=25)
    # ax[1].set_xlabel("Number of matches")


    # st.pyplot(fig)


    # st.title("Dismissal Kinds")
    # wicket_type = male_cricket['dismissal_kind'].value_counts().to_frame()
    # wicket_type = wicket_type.reset_index().rename(columns = {'index' : 'type' , 'dismissal_kind' : 'count'})
    # extras = male_cricket[male_cricket['extra_type'].notnull()]['extra_type'].value_counts().to_frame()
    # extras = extras.reset_index().rename(columns = {'index' : 'type' , 'extra_type' : 'count'})
    # fig = plt.figure(figsize=(10,10))
    # plt.subplot(1,2,1)
    # plt.pie(extras['count'] , labels=extras['type'] , explode=[0.02,0,0.1,0,0] , autopct='%1.0f%%' )
    # plt.title("Extras" , fontsize=22)

    # wicket_type_count = 5
    # plt.subplot(1,2,2)
    # plt.pie(wicket_type['count'][:-wicket_type_count] , labels=wicket_type['type'][:-wicket_type_count]  , autopct='%0.0f%%' )
    # plt.title("Dismissals" , fontsize=22)

    # st.pyplot(fig)


    # st.title("Bowlers Distribution")
    # delivery = male_cricket[~male_cricket['extra_type'].isin(['noballs' , 'wides'])]
    # eco = male_cricket.groupby(['bowler']).sum()['total_run'].to_frame()
    # a = delivery['bowler'].value_counts()
    # a = a.to_frame().reset_index().rename(columns={'index' : 'bowler' , "bowler" : 'count'})
    # eco = eco.merge(a , on='bowler')
    # eco['overs'] = eco['count']//6
    # eco['economy'] = eco['total_run']/eco['overs']
    # with st.expander("Select to read about bowlers"):
    #     st.table(eco)

    # st.header("Overs Distribution")
    # fig = plt.figure(figsize=(10,5))
    # sns.histplot(x='overs' , kde=True , data=eco[eco['overs']>100] , color='r')
    # st.pyplot(fig)

    # st.header('Economy Distribution')
    # mean = eco[eco["overs"]>100]['economy'].mean()-.17
    # fig = plt.figure(figsize=(10,5))
    # sns.histplot(x='economy' , kde=True , data=eco[eco['overs']>100])
    # plt.axvline(mean, color='r', linestyle='dashed', linewidth=2)
    # st.pyplot(fig)

    # st.title("Top 10 lead scores")
    # temp = male_cricket.groupby(['batsman_name']).sum().sort_values(by='batsman_run' , ascending=False).drop(columns=['win_with','total_run' , 'mergeid' , 'extra_run' , 'over_num' ,'inning']).head(10).reset_index()
    # fig = plt.figure(figsize=(15,5))
    # sns.barplot(y='batsman_run' , x= 'batsman_name' , data=temp)
    # st.pyplot(fig)

    # st.title("Top wicket bowlers")
    # bowled = [ 'caught', 'bowled',  'caught and bowled', 'lbw','stumped', 'hit wicket']
    # dismisses = male_cricket[male_cricket['dismissal_kind'].isin(bowled)]
    # player_wckt = dismisses.groupby(['bowler']).count()['inning'].reset_index().rename(columns= {'inning' : 'count'})
    # top_bowlers = player_wckt.sort_values(by='count' , ascending=False)[:10]
    # print(top_bowlers)
    # fig = plt.figure(figsize=(20,10))
    # sns.barplot( data=top_bowlers ,palette='summer' ,  y='bowler' , x='count' )
    # st.pyplot(fig)

    # st.title("Top win by countries")
    # toss = male_matches[male_matches.isin(male_top_countries)]['toss_winner'].value_counts().reset_index().rename(columns={'index' : 'country'})
    # fig = plt.figure(figsize=(20,10))
    # ax = sns.barplot(x='country' , y='toss_winner' , data=toss , palette=sns.diverging_palette(359,359,n=20, center='dark'))
    # for p in ax.patches:
    #     ax.annotate("{:.0f}".format(p.get_height()), (p.get_x()+p.get_width()/4+0.1, p.get_height()+1))
    # st.pyplot(fig)

