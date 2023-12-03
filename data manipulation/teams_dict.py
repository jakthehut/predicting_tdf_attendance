from bs4 import BeautifulSoup as bs
import requests

team_num = 1
team_dict = {}
for year in range(2010,2024,1):
    URL_teams_per_year = requests.get("https://www.procyclingstats.com/teams.php?year=" + str(year) + "&filter=Filter")
    soup_year = bs(URL_teams_per_year.content, features="html.parser")
    teams_wt_html = soup_year.find("div",{"class":"mt20"}).find_all("a")

    #teams_pt_html = soup_year.find_all("div",{"class":"mt20"})[2].find_all("a")
    #teams_html = teams_wt_html + teams_pt_html
    
    for team in teams_wt_html:
        URL_team = requests.get("https://www.procyclingstats.com/" + str(team["href"]))
        soup_team = bs(URL_team.content, features="html.parser")
        team_over_time = soup_team.find("div","pageSelectNav").find_all("option")
        team_ot_set = set([team.string[7:] for team in  team_over_time])
        if team_ot_set not in team_dict.values():
            team_dict[team_num] = team_ot_set
            team_num += 1

team_enum = {}
for key, teams in team_dict.items():
    for team in teams:
        team_enum[team] = key


