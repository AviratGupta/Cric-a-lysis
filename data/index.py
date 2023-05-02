
import pandas as pd 
from Constants import TOP_COUNTRY_COUNT

t20_matches= pd.read_csv('data/t20_matches.csv')
personal_male = pd.read_csv('data/personal_male.csv')
matches = pd.read_csv('data/T20_international_matches.csv')
every_ball = pd.read_csv('data/Every_ball_data.csv')



t20 = every_ball.merge(matches , on = 'mergeid' , how='left')
t20['year'] = t20['date'].apply(lambda x : x.split("-")[0]).astype(int)

personal_male = personal_male[~personal_male['nationalTeam'].isna()]

male_cricket = t20[t20['gender'] == 'male']
male_cricket['year'] = male_cricket['date'].apply(lambda x : x.split("-")[0]).astype(int)
female_cricket = t20[t20['gender'] == 'female']
female_cricket['year'] = female_cricket['date'].apply(lambda x : x.split("-")[0]).astype(int)

male_matches = matches[matches['gender'] == 'male']
female_matches = matches[matches['gender'] == 'female']


countries = pd.concat([matches['team_1'] , matches['team_2']]).value_counts().index.tolist()

top_countries = pd.concat([matches['team_1'] , matches['team_2']]).value_counts().head(TOP_COUNTRY_COUNT).index.tolist()
male_top_countries = pd.concat([male_matches['team_1'] , male_matches['team_2']]).value_counts().head(TOP_COUNTRY_COUNT).index.tolist()
female_top_countries = pd.concat([female_matches['team_1'] , female_matches['team_2']]).value_counts().head(TOP_COUNTRY_COUNT).index.tolist()


# top_batsman = pd.concat([matches['team_1'] , matches['team_2']]).value_counts().head(TOP_COUNTRY_COUNT).index.tolist()
# male_top_batsman = pd.concat([male_matches['team_1'] , male_matches['team_2']]).value_counts().head(TOP_COUNTRY_COUNT).index.tolist()
# female_top_batsman = pd.concat([female_matches['team_1'] , female_matches['team_2']]).value_counts().head(TOP_COUNTRY_COUNT).index.tolist()



# Total Number of player
p1 = pd.DataFrame(t20.batsman_name.unique())
p2 = pd.DataFrame(t20.bowler.unique())
players_list = pd.concat([p1,p2])[0].unique().tolist()