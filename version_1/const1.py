# save all of the constant variables in here
# define values associated with individual cars (image file, i and f positions, etc.)

# includes class(es): Constants, CarParameters, CarDef

import numpy as np
import pygame as pg
import math

class Constants:

    # Hard-coding in: screen width/height, horz/vert road widths, car image dimensions

    pg.init()

    # PYGAME COLORS
    DKGREEN = (0,100,0)
    BLACK = (0,0,0)
    GRAY = (127,127,127)
    YELLOW = (255,255,0)
    GOLD = (255,215,0)
    KHAKI = (240,230,140)
    DKKHAKI = (189,183,107)
    WHITE = (255,255,255)
    LTLTGREY = (230,230,230)
    PURPLE = (156, 81, 182)

    # MISCILLANEOUS
    draw_screen = True

    # CAR IMAGE FOLDER LOCATIONS
    asset_location = "assets/"
    blue_car = pg.image.load("cp_blue_car.png") # import car image
    red_car = pg.image.load("cp_red_car.png") # import car image


    # SCREEN PIXELS
    screen_x = 720 # do not set to zero! # screen width
    screen_y = 720 # do not set to zero! # screen height
    origin = [round(screen_x/2), round(screen_y/2)] # set origin to middle of screen using pixels
    origin_c = np.array([0.0, 0.0]) # set origin as coordinates

    # SCREEN COORDINATE
    screen_x_c = 5 # screen width coord scale
    screen_y_c = 5 # screen height coord scale

    # SCALE
    scale_x = screen_x/screen_x_c # number of pixels per 1 coordinate
    scale_y = screen_y/screen_y_c # number of pixels per 1 coordinate
    coord_scale = 150    # only for def scaling1 in screen.py, otherwise delete

    # ROAD PARAMETERS (road = rd)
    # rd widths for both directions
    horz_rd_width = 300
    vert_rd_width = 300

    # Horz for double lane rd both directions
    h_single_direct_width = round(horz_rd_width/2) # single direction rd width
    screen_mid_y = round(screen_y/2)
    hrect = (0, screen_mid_y - h_single_direct_width, screen_x, horz_rd_width) # define horz rd rectangle

    rd_217 = round(screen_mid_y - horz_rd_width/4) # top horz white line
    rd_514 = round(screen_mid_y + horz_rd_width/4) # bottom horz white line

    # Vert for double lane rd both directions
    v_single_direct_width = round(vert_rd_width/2) # single direction rd width
    screen_mid_x = round(screen_x/2)
    vrect = (screen_mid_x - v_single_direct_width, 0, vert_rd_width, screen_y) # define vert rd rect

    rd_823 = round(screen_mid_x - vert_rd_width/4) # left vert white line
    rd_1120 = round(screen_mid_x + vert_rd_width/4) # right vert white line

    # Rd line parameters
    rd_724 = round(screen_mid_x - vert_rd_width/2)
    rd_1219 = round(screen_mid_x + vert_rd_width/2)
    rd_118 = round(screen_mid_y - horz_rd_width/2)
    rd_613 = round(screen_mid_y + horz_rd_width/2)

    # Double yellow center lines
    yellow_width_x = round((1/144) * (screen_y)) # width of the yellow lines (l and r)
    yellow_spacing_x = yellow_width_x # distance between two yellow lines
    yellow_width_y = round((1/144)*(screen_x)) # width of the yellow lines (t and b)
    yellow_spacing_y = yellow_width_y # distance between two yellow lines
        
    # Top (t) and left (l) yellow line position
    rd_316 = screen_mid_y - round(yellow_spacing_x/2) - yellow_width_x # top of top yellow line, (l and r)
    rd_922 = screen_mid_x - round(yellow_spacing_y/2) - yellow_width_y # left of left yellow line, (t and b)
        
    # Bottom (b) and right (r) yellow line position
    rd_415 = screen_mid_y + round(yellow_spacing_x/2) # top of bottom yellow line, (l and r)
    rd_1021 = screen_mid_x + round(yellow_spacing_y/2) # left of right yellow line, (t and b)


    # CAR DIMENSIONS
    # define pixel dimensions for car image (no rotation)
    red_car_height = 120
    red_car_width = 60
    blue_car_height = 120
    blue_car_width = 60

    action_timesteps = 100
    track_back = 1
    theta_set = np.array([1, 1e3]) # WHAT DOES THIS CHANGE?
    traj_set = np.array([3., 2., 1., 0., 1., 2.])

    turnangle = 0
  

class CarParameters:
# shared variable concepts between all vehicles; used to define cars in CarDef()

    def __init__(self, model, car_color, i_pos, f_pos, orientation, xi_vel, yi_vel, xi_accel, yi_accel, max_vel, max_accel, plan_traj, intent, aggression, theta, next_pos):
        
        self.model = model
        self.car_color = car_color # vehicle color to relate to image file
        self.i_position = i_pos # initial position
        self.f_position = f_pos # final goal position (i.e. location)
        self.orientation = orientation # vehicle image rotation
        self.xi_velocity = xi_vel # initial velocity in the x-direction
        self.yi_velocity = yi_vel # initial velocity in the y-direction
        self.xi_acceleration = xi_accel # initial acceleration in x-direction
        self.yi_acceleration = yi_accel # initial acceleration in y-direction
        self.max_velocity = max_vel # maximum allowable velocity
        self.max_acceleration = max_accel # maximum allowable acceleration/deceleration
        self.planned_trajectory = plan_traj # planned trajectory path
        self.intent = intent
        self.aggression = aggression # measure of how aggressive a vehicle is
        self.theta = theta
        self.next_position = next_pos


class CarDef: # Car Definitions/Parameters
# define the set vehicle parameters for all vehicles
# define vehicle road bounds


    def __init__(self, CAR1, CAR2):
        
        self.CAR1 = CAR1 # BLUE CAR
        self.CAR2 = CAR2 # RED CAR



    # CAR ROAD BOUNDS (i.e. x as horizontal line, not a limit in horz direction)
    bd_CAR2_x = np.array([Constants.rd_316/5, Constants.rd_217/5]) # red car
    bd_CAR2_y = None
    bd_CAR1_x = None # blue car
    bd_CAR1_y = np.array([(Constants.rd_1021 + Constants.yellow_width_x)/5, Constants.rd_1120/5])


    CAR1 = CarParameters(model = 1, # M (machine - vertical)
                         car_color = Constants.blue_car,
                         i_pos = np.array([0.18, -2.0]), # on coordinate axis with center of screen at (0,0)
                         f_pos = np.array([0.18, 2.0]), # on coordinate axis with center of screen at (0,0)
                         orientation = 0, # rotation of image file in degrees
                         xi_vel = 0,
                         yi_vel = 0.025,
                         xi_accel = 0,
                         yi_accel = 0.002,
                         max_vel = 0.1,
                         max_accel = 0.002,
                         plan_traj = np.array([-2.0, -1.0, 0, 1.0, 2.0]),
                         intent =1e3,
                         aggression = 5, # scale from 1 to 10; 1 is passive, 5 is reactive, 10 is aggressive
                         theta = 0,
                         next_pos= []
                         )
    
    # CONTINUE FIXING BELOW
    CAR2 = CarParameters(model = 2, # H (human - horizontal)
                         car_color = Constants.red_car,
                         i_pos = np.array([2.0, 0.35]), # on coordinate axis with center of screen at (0,0)
                         f_pos = np.array([-2.0, 0.35]), # on coordinate axis with center of screen at (0,0)
                         orientation = -90., # rotation of image file in degrees
                         xi_vel = 0.025,
                         yi_vel = 0,
                         xi_accel = 0.002,
                         yi_accel = 0,
                         max_vel = 0.1,
                         max_accel = 0.002,
                         plan_traj = np.array([-2.0, -1.0, 0, 1.0, 2.0]),
                         intent = 1,
                         aggression = 5, # scale from 1 to 10; 1 is passive, 5 is reactive, 10 is aggressive
                         theta = 0,
                         next_pos=[]
                         )

