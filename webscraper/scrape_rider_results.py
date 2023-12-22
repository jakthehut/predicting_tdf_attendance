from bs4 import BeautifulSoup as bs
import requests
import re
import csv
import pandas as pd


def rider_result_link(number, rider_href):

    # https://www.procyclingstats.com/rider/nicola-conci/statistics/season-statistics
    return "https://www.procyclingstats.com/rider.php?proresults=0&pproresults=largerorequal&stage_type=" +str(number) + "&filter=Filter&id=" + str(list(rider_href.split("/"))[1]) + "&p=statistics&s=season-statistics"

def result_table(number_result, rider_href):
    link = rider_result_link(number_result, rider_href)
    URL_test = requests.get(link)
    soup_result = bs(URL_test.content, features="html.parser")
    results_html = list(soup_result.find_all("div",{"class":"mt10"}))[-1] #.find("table", {"class": "basic"})

    head_html = results_html.find_all("thead")[0].find_all("th")
    head = [head.string for head in head_html] 
    raw_frame = []
    body_html = results_html.find_all("tbody")[0].find_all("tr")
    for row in body_html:
        
        row_html = row.find_all("td")
        row_vals = []
        for value in row_html:
            if value.string == "-" or value.string == None:
                row_vals.append(0)
            else:
                row_vals.append(float(value.string))
        row_vals[0] = int(row_vals[0])
        raw_frame.append(row_vals)

    rider_frame = pd.DataFrame(raw_frame, columns=head)
    rider_frame.set_index("Season", inplace=True)
    return rider_frame[["Points","Racedays"]]


def get_discipline_results(rider_href, riders_dict, scraping_season, link_dict):
    def check_if_index_exists(df, index=scraping_season):
        indexes = df.index.values.tolist()
        if index in indexes:
            return True
        else:
            return False

    rider_infos = riders_dict[rider_href]

    output = {}

    
    for key, matrix in rider_infos.items():
        columns = matrix.columns.to_list()

        this_flag = check_if_index_exists(matrix, scraping_season)
        pre_flag = check_if_index_exists(matrix, scraping_season-1)
        for column in columns:
            value_name = "season " + str(key) + " " + str(column)
            if this_flag:
                cell_value = matrix.loc[scraping_season, column]
                output[value_name] = cell_value
            else:
                output[value_name] = 0
            
            value_name_pre = "last season " + str(key) + " " + str(column)
            if pre_flag:
                cell_value_pre = matrix.loc[scraping_season-1, column]
                output[value_name_pre] = cell_value_pre
            else:
                output[value_name_pre] = 0
    return output


def rider_discipline_results(rider_href, riders_dict, scraping_season):
    scraped_riders = riders_dict.values()
    link_dictionary={4:"gc",1:"stages",2:"oneday",8:"tt"}  # 0:"accumulated", #acc, gc, stages, oneday, tt # reference type of results filter


    if rider_href in scraped_riders:
        return get_discipline_results(rider_href, riders_dict, scraping_season, link_dictionary)
    else:
        rider_results = {}
        for key, value in link_dictionary.items():
            rider_results[value] = result_table(key, rider_href)
        riders_dict[rider_href] = rider_results
        return get_discipline_results(rider_href, riders_dict, scraping_season, link_dictionary)

#riders_dictionary = {}
#print(rider_discipline_results("rider/fabio-van-den-bossche", riders_dictionary, 2023))
#print(len(rider_discipline_results(rider["href"], riders_dictionary, 2023)))


        
