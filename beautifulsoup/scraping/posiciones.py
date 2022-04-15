"""
    Created 14-03-2022

    @author: Erik Carcelen

    Description: Web scraping about positions teams in NBA
"""

from operator import index
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2021_standings.html'

response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')

teams = soup.find_all('tr', class_='full_table')
team_list = []

for team in teams:
    team_name = team.find('th', class_= 'left').text.replace('*', '')
    team_list.append(team_name)

match_wins = soup.find_all('td', class_= 'right')
wins_list = []
for win in match_wins:
    if win.get('data-stat') == 'wins':
        wins_list.append(win.text)

match_losses = soup.find_all('td', class_= 'right')
lost_list = []
for lost in match_losses:
    if lost.get('data-stat') == 'losses':
        lost_list.append(lost.text)

# Creating a dataframe
df = pd.DataFrame({'Team': team_list, 'Wins': wins_list, 'Losses': lost_list},)

df.to_csv('nba-teams.csv')