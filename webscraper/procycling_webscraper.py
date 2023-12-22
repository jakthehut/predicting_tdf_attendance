# FIXED: BUG for Vuelta, starting 2018 its name was "La Vuelta...." https://www.procyclingstats.com/rider/primoz-roglic/2019

# DONE do all grand tour teams
# DO # WITH PANDAS nummerize teams, summarize on number if same team (vut different team)

# DONE start 2010 if possible
# ONGOING rider: 
    # DONE add all uci points, 
    # DONE pcs points, 
    # DONE hieght, 
    # DONE weight, 
    # GT position in each classification, 
    # DONE pre tdf type of race positions, 
    # with PANDAS: ranking in team that season till tdf AND end of last season 
    # DO: add whole team numbers
    # DO: will attend tdf next year
# TEAM STRATEGY THIS YEAR at tour: sprint, daywin, gc, mountain
# DONE include past data (tdf last year)

#visualize data, color by team



# make more efficient
# DO remove csv, change to pandas
# DICTIONARY SYSTEM?
# STORING AND SEARCHING
# DOWNLOAD ALL PAGE LINKS FIRST? --> load html code
from bs4 import BeautifulSoup as bs
import requests
import re
import csv


from scrape_rider_results import rider_discipline_results


def find_demographic(soup_rider):
    """return birthyear, height, kg of rider """
    rider_info_age = soup_rider.find("div",{"class":"rdr-info-cont"})
    
    pattern = {}
    pattern["age"] = r'\((\d+)\)<br/><b>Nationality'
    pattern["height"] = r'Height:</b> (\d+\.\d+) m<br/>'
    pattern["weight"] = r'Weight:</b> (\d+)'
    
    solution={}
    for key, patter in pattern.items():
        match = re.search(patter, str(rider_info_age))
        if match:
            if key == "age":
                solution[key] = match.group(1)
                if solution[key] == "-":
                    solution[key] = None
                else:
                    solution[key] = int(solution[key])
            if key == "height":
                solution[key] = float(match.group(1))
            if key == "weight":
                solution[key] = int(match.group(1))
        else:
            solution[key] = None
            print("Error finding demographic infos of at ", key, ", rider:", profile["name"], profile["season"],"\n")#, str(rider_info_age))
    return solution
def get_pcsp(soup_rider):
    """give rider web url, get float pcs points"""
    rider_points =soup_rider.find("div",{"class":"rdrResultsSum"}).find_next("div")
    pcs_points = rider_points.find_all("b")[1].string
    if pcs_points!= None:
        return float(pcs_points)  # Extract the captured number
    else:   
        return 0.0
def get_ucip(soup_rider):
    """give rider web url, get float uci points"""
    rider_points =soup_rider.find("div",{"class":"rdrResultsSum"}).find_next("div")
    uci_points = rider_points.find_all("b")[2].string
    if uci_points != None:
        return float(uci_points)  # Extract the captured number
    else:
        return 0.0
def rider_events(soup_rider):
    """returns 1. pcs points till tdf 2. uci points till tdf 3. racedays till tdf 4. if tdf attended 5. if vuealta attended 6. if giro attended"""
    def if_points_value_num(points_string):
        if points_string != None:
            return float(points_string)
        else:
            return 0.0

    rider_races_html = soup_rider.find("div",{"id":"resultsCont"}).find_all("tr")

    raceday_points = {}
    gc_pcs = 0
    gc_uci = 0

    tdf_attended = False
    vae_attended = False
    giro_attended = False
    
    for entity_index in range(1,len(rider_races_html)):
        event = rider_races_html[entity_index]

        # check if grand tour attended
        race_title = str(event.find("td",{"class":"name"}).a).split(">")[1][:13]
        if race_title == "Tour de Franc":
            tdf_attended = True
        if race_title == "Vuelta a Espa" or race_title == "La Vuelta cic":
            vae_attended = True
        if race_title == "Giro d'Italia":
            giro_attended = True

        
        all_entries = event.find_all("td")

        date = all_entries[0].string 

        pcs_points_raw = all_entries[6].string
        pcs_points = if_points_value_num(pcs_points_raw)

        uci_points_raw = all_entries[7].string
        uci_points = if_points_value_num(uci_points_raw)

        if date == None:  # GC classifications
            if gc_pcs != None:
                gc_pcs += float(pcs_points)
            if gc_uci != None:
                gc_uci += float(uci_points)
        elif "»" not in date:  #  one day entry
            day, month = date.split(".")
            day, month = int(day), int(month)
            date_numerical = (month-1)*31+day

            raceday_points[date_numerical]=[pcs_points+gc_pcs, uci_points+gc_uci]
            gc_pcs = 0
            gc_uci = 0

    pcsp_till_tdf = 0
    ucip_till_tdf = 0
    race_days = 0

    tdf_date =  5*31 +28   # 28.June
    for day in raceday_points.keys():
        if day < tdf_date:
            pcsp_till_tdf += raceday_points[day][0]
            ucip_till_tdf += raceday_points[day][1]
            race_days += 1

    return  pcsp_till_tdf, ucip_till_tdf, race_days, tdf_attended, vae_attended, giro_attended


file="Machine Learning Intro\course_project\scraper\cycling_tdf_extended.csv"

flag = True
riders_dictionary = {}

with open(file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    for year in range(2010,2024,1):
        profile = {}
        profile["season"]=year

        URL_teams_per_year = requests.get("https://www.procyclingstats.com/teams.php?year=" + str(year) + "&filter=Filter")
        soup_year = bs(URL_teams_per_year.content, features="html.parser")
        
        teams_wt_html = soup_year.find("div",{"class":"mt20"}).find_all("a")
        #teams_pt_html = soup_year.find_all("div",{"class":"mt20"})[2].find_all("a")
        #teams_html = teams_wt_html + teams_pt_html
        
        for team in teams_wt_html:
            profile["team"]=team.string
            
            URL_team = requests.get("https://www.procyclingstats.com/" + str(team["href"]))
            soup_team = bs(URL_team.content, features="html.parser")
            riders_html = soup_team.find("div",{"class":"ridersTab"}).find_all("a")
            for rider in riders_html:
                profile["name"] = rider.string
                URL_rider = requests.get("https://www.procyclingstats.com/" + str(rider["href"]) + "/" + str(year))
                soup_rider = bs(URL_rider.content, features="html.parser")

                profile.update(find_demographic(soup_rider))

                profile["pcs points"]=get_pcsp(soup_rider)
                profile["uci points"]=get_ucip(soup_rider)
                profile["pcs points till tdf"], profile["uci points till tdf"], profile["race days till tdf"],profile["tdf attended"], profile["vuelta attended"], profile["giro attended"] = rider_events(soup_rider)

                URL_rider_before = requests.get("https://www.procyclingstats.com/" + str(rider["href"]) + "/" + str(year-1))
                soup_before = bs(URL_rider_before.content, features="html.parser")
                profile["last season pcs points"]=get_pcsp(soup_before)
                profile["last season uci points"]=get_ucip(soup_before)
                
                # get elaborate infos: error  in line 17 with rider after "2013,Team Saxo - Tinkoff,CONTADOR Alberto,"
                #profile.update(rider_discipline_results(rider["href"], riders_dictionary, year))

                if flag:
                    writer.writerow(profile.keys())
                    flag = False
                writer.writerow(profile.values())