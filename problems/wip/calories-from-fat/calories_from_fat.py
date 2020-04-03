#!/bin/python3

fat, protein, sugar, starch, alcohol = [0 for i in range(5)]
total_cals = fat * 9 + (protein + sugar + starch) * 4 + alcohol * 7

def parse_caloric_string(string):
    meal_calories = 0
    macros = string.split()
    # TODO
    # If % -> make it factor of meal_calories
    # If c -> divid by proper macro
    # If g -> multiply with proper macro
    
parse_string(input())
