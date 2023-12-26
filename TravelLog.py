# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:43:26 2022

@author: Jules
"""

travel_log = [
    
   {
    "Country" : "France",
    "Cities" :  ["Paris", "Lille", "Dijon"],
    "Visits: " : 12
    
    },
   
  { 
   "Country" :  "Germany", 
   "Cities" :  ["Berlin", "Hamburg", "Stuttgart"],
   "Visits" : 5
   },
]


def add_new_country (country_visited, cities_visited, times_visited,):
    
    new_country = {}
    new_country["Country"] = country_visited
    new_country["Cities"] = cities_visited
    new_country["Visits"] = times_visited
    travel_log.append(new_country)
   


#TODO
# A program that adds to to a travel_log, its a list that contains two dictionaries.
# Write a function that will work with the following line of code on 35 to add the entry for Russia to the travel_log.
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia two times
# You've been to Moscow and Saint Petersburg.

add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)
