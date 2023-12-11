"""
Main app which runs the streamlit dashboard
"""
import numpy as np
import pandas as pd
import streamlit as st
import statsapi

# define team abbreviations for lookup reference
teams_abb = ['LAD', 'LAA', 'SDP', 'SEA', 'SFG', 'TBR', 
             'DET', 'KCR', 'CLE', 'MIL', 'NYY', 'HOU', 
             'ARI', 'STL', 'BAL', 'MIA', 'MIN', 'PIT', 
             'ATL', 'CIN', 'TEX', 'TOR', 'NYM', 'PHI',
             'BOS', 'OAK', 'CHC', 'COL', 'CHW', 'WSN']

# define dictionary which maps the abbreviation to the team name\
abb_to_name = {'LAD': 'Los Angeles Dodgers', 'LAA': 'Los Angeles Angels', 'SDP': 'San Diego Padres', 'SEA': 'Seattle Mariners', 'TBR': 'Tampa Bay Rays',
               'DET': 'Detroit Tigers', 'KCR': 'Kansas City Royals', 'CLE': 'Cleveland Guardians', 'MIL': 'Milwaukee Brewers', 'NYY': 'New York Yankees', 'HOU': 'Houston Astros',
               'ARI': 'Arizona Diamondbacks', 'STL': 'St Louis Cardinals', 'BAL': 'Baltimore Orioles', 'MIA': 'Miami Marlins', 'MIN': 'Minesotta Twins', 'PIT': 'Pittsburgh Pirates',
               'ATL': 'Atlanta Braves', 'CIN': 'Cincinnati Reds', 'TEX': 'Texas Rangers', 'TOR': 'Toronto Blue Jays', 'NYM': 'New York Mets', 'PHI': 'Philadelphia Phillies',
               'BOS': 'Boston Red Sox', 'OAK': 'Oakland Athletics', 'CHC': 'Chicago Cubs', 'COL': 'Colorado Rockies', 'CHW': 'Chicago White Sox', 'WSN': 'Washington Nationals'}

st.title('MLB Teams')

# st.write("Please select one of the following teams:")
team_selection = st.selectbox('Please select one of the MLB Teams', options = list(abb_to_name.values()))

team = statsapi.lookup_team(team_selection)
st.write('You selected: ', team_selection)
