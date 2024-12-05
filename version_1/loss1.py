import numpy as np
import matplotlib.pyplot as plt
import math
import time
from numpy.core.multiarray import ndarray

class LossFunctions:

    def __init__(self, vehicle):
        self.P_CAR = vehicle
        self.total_loss = []
        self.other_car

    def calc_loss(self):
        safety_loss = self.traj_collide_loss()
        task_loss = self.goal_loss()
        self.total_loss = safety_loss + self.P_CAR.intent*task_loss
        return self.total_loss
        # add up all the losses

    def traj_collide_loss(self): # NEED INTERSECTION LINES, VEHICLE VELOCITY, OTHER VEHICLE POSITION AT TIME T AND T+1
        loss = loss
        top_intersect = top_intersect # horizontal
        bot_intersect = bot_intersect # horizontal
        left_intersect = left_intersect # vertical
        right_intersect = right_intersect # vertical
        if self.other_car.position[0] <= right_intersect and self.other_car.position[0] >= left_intersect:
            if self.other_car.positin[1] <= top_intersect and self.other_car.position[1]:
                self.P_CAR.velocity = 0
                loss = 1e5
        else:
            loss = 0
        return loss
        # do vehicle paths collide
        # colliding in near or distant future
            # more loss for near, less loss for distant

        # DO I MAKE A COLLISION BOX FOR THE INTERSECTION -> only place in this scenario where the vehicles will collide

        # FIX!!!
        # CHECK REFERENCE CODE COLLISION_BOX.PY

    def goal_loss(self):
        loss = loss
        dist_to_goal_t = self.distance(self.P_CAR.position, self.P_CAR.f_position)
        dist_to_goal_t_1 = self.distance(self.P_CAR.next_position, self.P_CAR.f_position)
        if dist_to_goal_t_1 <= dist_to_goal_t:
            loss=0
        else:
            loss=1e2
        return loss
    
        # can calculate with a scale based on distance from 1 to 1000

    def distance_to_other_car(self):
        distance=distance
        return distance
        # calculate distance to trajectory intersection
            # can look at both planned and predicted? depending on when we calculate what
            # if we have both trajectories at this point, take whichever loss is highest for confidence level

        # DO THIS DIFFERENTLY IF BOXING THE LITERAL INTERSECTION

    def distance(self, pos_1, pos_2):
        dist  = math.sqrt(pow((pos_1[0]-pos_2[0]), 2) + pow((pos_1[1] - pos_2[1]), 2))
        return dist