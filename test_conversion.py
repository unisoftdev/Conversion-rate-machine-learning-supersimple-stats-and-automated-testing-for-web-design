# For a GUI, better performance, more functions, and easiness to use... Check out: www.unisoftdev.tech

'''
* @ Automated web design conversion rate testing
* Created By: Juraj Vysvader
* Author's profile: https://www.linkedin.com/in/jurajvysvader
                    https://www.linkedin.com/company/unisoftdev 
* Creation date: 10.3.2019
* Business website: https://www.unisoftdev.tech
* @license http://www.gnu.org/copyleft/lgpl.html GNU/GPL
* @Copyright (C) 2019 Juraj Vysvader. All rights reserved.
'''


#! /usr/bin/python


import json
from json import loads
from json import dumps
import global_variable


def display_element(something_to_display):
    # handle this variable for a server rendering HTML   
    global_variable.color = something_to_display

def Start():
    # gets all of our data from the config file.
    with open('con.json', 'r') as nnn:
        config_data = json.load(nnn)


    test_result = config_data["test_result"]

    #check that the test didn't finish:
    if not len(test_result) < 1:
        print("The result: " + str(test_result))
        something_to_display = config_data["winning_color"]
        display_element(something_to_display)
    else:
        #sets a number of visitors that will be tested against each one design scheme 
        number_of_visits_per_each = 100 #At this time, it's 100 people for each one color

        #this checks which one color is currently tested, which this data are picked up about 
        # and later tests conversion rate of 100 visitors per each design scheme
        if config_data["green"]["prices_list_visits"] < number_of_visits_per_each:
            something_to_display = config_data["green"]["color"]
            config_data["results"]["green"] =+ 1 # this counts clicks
        elif config_data["orange"]["prices_list_visits"] < number_of_visits_per_each:
            something_to_display = config_data["orange"]["color"]
            config_data["results"]["orange"] =+ 1 # this counts clicks
        elif config_data["red"]["prices_list_visits"] < number_of_visits_per_each:
            something_to_display = config_data["red"]["color"]
            config_data["results"]["red"] =+ 1 # this counts clicks
        elif config_data["blue"]["prices_list_visits"] < number_of_visits_per_each:
            something_to_display = config_data["blue"]["blue"]
            config_data["results"]["color"] =+ 1 # this counts clicks

        #if it's the end of the test:
        else:
            find_the_highest = config_data["results"]
            event_finish = max(find_the_highest, key=find_the_highest.get)
            #event = max(config_data, key=lambda ev: ev['price_list_clicks'])
            print(event_finish)
            config_data["test_result"] = event_finish
            config_data["winning_color"] = config_data[event_finish]["color"]
            something_to_display = config_data["winning_color"]

            with open('con.json', 'w') as f:
                f.write(json.dumps(config_data))