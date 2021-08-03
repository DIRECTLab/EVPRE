#import config #This is your api keys openroute, weatherapi, and google(google is a pain to set up FYI)
from math import sin, radians, cos
import sqlite3 as sq
import pandas as pd
import numpy as np
import requests
from os import sys

class ev_power_model:
    def __init__(self, mass, air_resistance, area, rf=0.02, air_density=1.225):
        self.mass = mass # in kilograms かな... 
        self.air_resistance = air_resistance
        self.area = area 
        self.rolling_friction = rf
        self.air_density = air_density # kg/m^3
        self.gravity = 9.8

    def convert_heading(self, heading):
        """
        takes a string of direction and converts it into an angle

         Args:
            heading - string of what the direction is (ex. SW)
         Returns:
            The angle of the direction
        """

        headings = ["E", "NE", "N", "NW", "W", "SW", "S", "SE"]
        angle = 0
        
        for h in headings:
            if heading is h:
                break
            angle += 45
        return angle


    def energy_consumption(self, angle, v_car, a, v_wind, car_heading=0, wind_h="S", length=1):
        """
        A simple model to predict the instantaneous energy consumption of a vehicle
        Based off of https://www.sciencedirect.com/science/article/pii/S030626191630085X

         Args:
            angle - angle of the car at a certain time point
            v_car - velocity of the car
            a - acceleration of the vehicle
            v_wind - velocity of the wind
            car_h - heading of the car with north being 0 degrees
            wind_h - heading of the wind
         Returns:
            A single value of the total energy cost for the time length

        """

        #calculate wind velocity, believing that the y-direction of the vehicle is always the y-axis.
        
        wind_heading = self.convert_heading(wind_h)

        wind_heading -= car_heading
        
        wind_speed = v_car - v_wind * cos(radians(wind_heading))

        calc1 = self.mass * a

        calc2 = self.mass * self.gravity * length * (1.75/1000)*(0.0328*v_car+4.575)

        calc3 = 0.5 * self.air_density * self.area * self.air_resistance * (wind_speed ** 2)

        calc4 = self.mass * self.gravity * sin(radians(angle))

        energy = ( ((calc1 + calc2 + calc3 + calc4) * v_car)/0.92/0.91) 

        return energy

def equalizer_constant(energy1, energy2):
    """
    Finds a constant variable that when multiplied to energy2 brings it to within two decimal points of energy1.
    This can be used to create a base difference for machine learning purposes
     Args: 
        energy1 - the energy from the first vehicle
        energy2 - the energy from the second vehicle
     Returns:
        A constant that can be used to convert one cars energy cost to another.
    """
    for x in range(len(energy1)):
        difference = 1
        equalizer = [100 for a in range(len(energy1))]
        change = 50
        while difference > 0.009 or difference < -0.009:
            add_diff =  (energy2[x] * (equalizer[x] + change)) - energy1[x]
            sub_diff = (energy2[x] * (equalizer[x] - change) - energy1[x]) if (energy2[x] * (equalizer[x] - change) - energy1[x]) > 0 else (energy2[x] * (equalizer[x] - change) - energy1[x]) * -1
            if sub_diff < add_diff:
                difference = sub_diff
                equalizer[x] -= change
            else:
                difference = add_diff
                equalizer[x] += change
            change /= 2
         
    return equalizer

if __name__ == "__main__":

    focus = ev_power_model(1337, 0.28, 1.825 * 1.469)
    f150  = ev_power_model(1500, 0.28, 1.825 * 1.469)

    #angle = [0,-0.01,-0.05,-0.07,-0.10]
    #v = [38,38,38,38,39]
    #accel = [0.13,0.13,0.13,0.13,0.13] 
    angle = [0]
    v = [27.8]
    accel = [.000010030864197531]
    wind_v = [6]

    focus_energy = focus.energy_consumption(angle, v, accel, wind_v)
    test_energy = test.energy_consumption(angle, v, accel, wind_v)

    equalizer = equalizer_constant(focus_energy, test_energy)
    print(equalizer)

    print(focus_energy)
    print(test_energy[0] * equalizer[0])
