# include the update function, AV class

from const1 import Constants as C
from const1 import CarDef as CD
from dynamic_func1 import dyn

import pygame as pg
import numpy as np
from scipy.interpolate import splprep
import matplotlib.pyplot as plt

class AV:

    def __init__(self, scenario_parameters, carSelfP):

        self.P = scenario_parameters
        self.P_CAR = carSelfP
        self.model = self.P_CAR.model

        # INITIALIZE CURRENT DYNAMICS
        self.position = [self.P_CAR.i_pos]
        self.velocity = [self.P_CAR.xi_vel, self.P_CAR.yi_vel]
        self.acceleration = [self.P_CAR.xi_accel, self.P_CAR.yi_accel]
        self.theta = [self.P_CAR.theta]
        self.futureSteps = []


        # INITIALIZE OTHER'S DYNAMICS
        self.pos_o = [] # other's position
        self.vel_o = []
        self.accel_o = []
        self.theta_o = []
        self.aggression_o = []
        self.intent_o = []
        self.other_car = []




    def update(self,frame): # called on by simulation function in main.py
        # update position of both vehicles every frame

        self.frame = frame
        model = self.model
        other = self.other_car

    # WHY ARE WE GETTING THE BEGINNING OF ONE ARRAY AND THE END OF THE OTHER FOR POSITIONS?
        if model == 1: # machine (vertical, blue, car1) moves first
            self.pos_o = np.array(other.position)
            # get the other's past velocity set with current velocity
            self.vel_o = np.array(other.velocity)
            # get the other's past acceleration set with current acceleration
            self.accel_o = np.array(other.acceleration)
            # get the other's past theta set with current theta
            self.theta_o = np.array(other.theta)
            # get aggression assumption for other vehicle

            # get intent assumption for other vehicle

        if model == 2: # human (horzontal, red, car2) moves first
            # keep both on the current time in main.py so look at positions before model 1 latest update
            self.pos_o = np.array(other.position[:-1])
            # get the other's past velocity set with current velocity
            self.pos_o = np.array(other.velocity[:-1])
            # get the other's past acceleration set with current acceleration
            self.pos_o = np.array(other.acceleration[:-1])
            # get the other's past theta set with current theta
            self.theta_o = np.array(other.theta)
            # get aggression assumption for other vehicle

            # get intent assumption for other vehicle

    
        # Get current loss for both cars



        # Get other car's future position, velocity, and acceleration with ode model
        # use dynamic function
        # use only the first value for this position
        other_car_future = []
        other_car_future = dyn(self.other_car)

        # use past traj and future position to calculate trajectory
        # either with ODE function or by trendline


        # go to game theory/prediction or loss file
        """
        if we can handle loss
            far away? yes - accelerate no more than max accel or max velocity
                      no - maintain velocity for another time step
        if self.loss == okay
            if self.distance_to_other_car >= 5
                accelerate[t]
                velocity up[t]
            if self.distance_to_other_car <=5
                maintain velocity[t]

                
        if we cannot handle loss
            slow down for another time step
                increase our deceleration
                decrease our velocity
        if self.loss == no good
            decelerate[t]
            velocity down[t]
        """

        # UPDATE VARIABLES
        # - append to variables held in var_update, will then use this position value in car_update to update image position on screen
        self.position.append(NEXT POSITION i.e. POSITION TRAJECTORY[0])
        self.velocity.append(NEXT VELOCITY i.e. VELOCITY TRAJECTORY[0])
        self.acceleration.append(NEXT ACCELERATION i.e. ACCELERATION TRAJECTORY[0]) # the self.ACCELERATION goes to sim loop in main.py to let self.var_update.car1_append(..., accel=self.car1.ACCELERATION)
        self.theta.append(NEXT THETA i.e. THETA TRAJECTORY[0])
        self.futureSteps.append(NEXT TRAJECTORY)
        # double check variable names as I have changed them
        # NEED TO COMPARE TO REFERENCE CODE
