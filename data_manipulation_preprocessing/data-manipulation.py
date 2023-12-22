import pandas as pd
import numpy as np
from teams_dict import team_enum, team_dict
#from rider_dict import rider_enum, data


"""
This file alters the raw web scraped data in a way that
- Age is not relative age today, but age that season
- team names changed over time, make this more general, that one teamname is defined no matter the season
- all nan values are removed, because the info was not found webscrapign
"""




def team_to_num(team_name):
    return team_enum[team_name]
def team_to_string(team_index):
    return list(team_dict[team_index])[0]

#def rider_to_num(rider_name):
#    return rider_enum[rider_name]

def age_to_age_season(age, season_year):
    if age == None or season_year != 2023:
        return age
    else:
        return age - (2013-season_year)

def fill_nan_with_avg(df, column):
    nan_index = []
    values = []
    for indices in df.index.to_list():
        value = df.loc[df.index[indices], column]
        if np.isnan(value):
            nan_index.append(indices)
        elif value == 0:
            nan_index.append(indices)
        else:
            values.append(value)
    avg_value = sum(values)/len(values)
    if column == "age":
        avg_value = int(avg_value)
    for indices in nan_index:
        df.loc[df.index[indices], column] = avg_value
    return df



def manipulate(df):
    for column in ["team","age"]:
        for indices in df.index.to_list():
            value = df.loc[df.index[indices], column]
            if column == "team":
                team_index = team_to_num(value)
                df.loc[df.index[indices], column] = team_to_string(team_index)
            elif column == "age":
                season = df.loc[df.index[indices],"season"]
                df.loc[df.index[indices], column] = age_to_age_season(value, season)
    for column in ["age","weight", "height"]:
        fill_nan_with_avg(df, column)

df = pd.read_csv("Machine Learning Intro\course_project\data manipulation\cycling_tdf.csv")
manipulate(df)

df.to_csv("cleaned_cycling_tdf.csv")
