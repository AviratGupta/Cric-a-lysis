
from data.index import every_ball , t20
import numpy as np
from data.index import top_countries

bowled = [ 'caught', 'bowled',  'caught and bowled', 'lbw','stumped', 'hit wicket']
dismisses = every_ball[every_ball['dismissal_kind'].isin(bowled)]
player_wckt = dismisses.groupby(['bowler']).count()['inning'].reset_index().rename(columns= {'inning' : 'count'})


delivery = t20[~t20['extra_type'].isin(['noballs' , 'wides'])]
eco = every_ball[~every_ball['extra_type'].isin(['noballs' , 'wides'])].groupby(['bowler']).sum()['total_run'].to_frame()
a = delivery['bowler'].value_counts()
a = a.to_frame().reset_index().rename(columns={'index' : 'bowler' , "bowler" : 'count'})
eco = eco.merge(a , on='bowler')
eco['overs'] = eco['count']//6
eco['economy'] = eco['total_run']/eco['overs']

t20['bowler_nation'] = t20.apply(lambda x : x['team_1'] if x['team_name'] != x['team_1'] else x['team_2'] , axis=1)
nation_bowler = t20[['bowler' , 'bowler_nation']].value_counts().reset_index().drop(columns= [0])
nation_bowler = nation_bowler.drop_duplicates(subset=['bowler'])

bowler_data = eco.merge(player_wckt , on='bowler' , how='left').fillna(0).rename(columns={'count_x' : 'bowls' , 'count_y' : 'wickets'})
bowler_data = bowler_data[bowler_data['economy'] != np.inf]

filtered_bowler = bowler_data.merge(nation_bowler , on='bowler' , how='left')
# filtered_bowler = filtered_bowler[(filtered_bowler['wickets'] >= 5) & (filtered_bowler['overs'] >= 100) & (filtered_bowler['bowler_nation'].isin(top_countries))]






# Batsman Data
data = t20
batsman_nation = data[['team_name' ,'batsman_name']].value_counts().to_frame().reset_index().drop(columns=[0])
filtered_batsman_nation = batsman_nation.drop_duplicates(subset='batsman_name')
filtered_batsman_nation = filtered_batsman_nation.rename(columns={'team_name' : 'country' , 'batsman_name' : 'name'})
# filtered_batsman_nation = filtered_batsman_nation[filtered_batsman_nation['country'].isin(male_top_countries)]
batsman_info = data.groupby('batsman_name').sum()['batsman_run'].reset_index()
temp= data[~data['extra_type'].isin(['wides', 'penalty'])].groupby('batsman_name').count()['inning'].reset_index().rename(columns={'inning' : 'balls'})
batsman_info = batsman_info.merge(temp , on='batsman_name' )
bats= batsman_info.merge(filtered_batsman_nation, left_on='batsman_name' , right_on='name' , how='left').dropna()
bats = bats.drop(columns=['name'])
bats['strike_rate'] = round((bats['batsman_run']/bats['balls'])*100 , 2)
top_bats_stats = bats[bats['balls'] > 150]