"""
Main app which runs the streamlit dashboard
"""
import numpy as np
import pandas as pd
import streamlit as st
import statsapi

# # define team abbreviations for lookup reference
# teams_abb = ['LAD', 'LAA', 'SDP', 'SEA', 'SFG', 'TBR', 
#              'DET', 'KCR', 'CLE', 'MIL', 'NYY', 'HOU', 
#              'ARI', 'STL', 'BAL', 'MIA', 'MIN', 'PIT', 
#              'ATL', 'CIN', 'TEX', 'TOR', 'NYM', 'PHI',
#              'BOS', 'OAK', 'CHC', 'COL', 'CHW', 'WSN']

# define dictionary which maps the abbreviation to the team name\
name_to_abb = {'Los Angeles Dodgers': 'LAD', 'Los Angeles Angels': 'LAA', 'San Diego Padres': 'SDP', 'Seattle Mariners': 'SEA', 'Tampa Bay Rays': 'TBR',
               'Detroit Tigers': 'DET', 'Kansas City Royals': 'KCR', 'Cleveland Guardians': 'CLE', 'Milwaukee Brewers': 'MIL', 'New York Yankees': 'NYY', 'Houston Astros': 'HOU',
               'Arizona Diamondbacks': 'ARI', 'St Louis Cardinals': 'STL', 'Baltimore Orioles': 'BAL', 'Miami Marlins': 'MIA', 'Minesotta Twins': 'MIN', 'Pittsburgh Pirates': 'PIT',
               'Atlanta Braves': 'ATL', 'Cincinnati Reds': 'CIN', 'Texas Rangers': 'TEX', 'Toronto Blue Jays': 'TOR', 'New York Mets': 'NYM', 'Philadelphia Phillies': 'PHI',
               'Boston Red Sox': 'BOS', 'Oakland Athletics': 'OAK', 'Chicago Cubs': 'CHC', 'Colorado Rockies': 'COL', 'Chicago White Sox': 'CHW', 'Washington Nationals': 'WSN'}

st.title('MLB Teams')

# st.write("Please select one of the following teams:")
team_selection = st.selectbox('Please select one of the MLB Teams', options = list(name_to_abb.keys()), 
                              index = None, placeholder = 'Select MLB team')

if team_selection: 
    st.write('You selected: ', team_selection)

    team = statsapi.lookup_team(team_selection)[0]
    roster = statsapi.roster(team['id'])
    roster_df = pd.DataFrame(roster.split('\n')).rename(columns = {0: 'Number'})
    roster_df['Number'] = roster_df['Number'].str.replace(' +', ' ', regex = True).str.replace(' ', '-', n = 2)
    roster_df[['Number', 'Position', 'Name']] = roster_df['Number'].str.split('-', expand = True, n = 2)

    st.dataframe(roster_df, hide_index = True)
