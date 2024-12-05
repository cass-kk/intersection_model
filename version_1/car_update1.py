# working with car image: screen location, rotations, coloring, updating

import pygame as pg
import pygame.gfxdraw
from const1 import Constants as C
import numpy as np
import math
import os
from screen1 import bkgnd as B
from screen1 import scalingC2P

class car_initialize():

    def __init__(self):

        pg.init()
        self.screen = pg.display.get_surface()

        C.red_car = C.red_car.convert()
        C.red_car.set_colorkey((255,255,255)) # make the color white transparent
        C.red_car = pg.transform.scale(C.red_car, (C.red_car_width, C.red_car_height)) # resize image
        C.red_car = pg.transform.rotate(C.red_car, 90) # rotate image by 90 degrees

        C.blue_car = C.blue_car.convert()
        C.blue_car.set_colorkey((255,255,255)) # make the color white transparent
        C.blue_car = pg.transform.scale(C.blue_car, (C.blue_car_width, C.blue_car_height)) # resize image

class car_update():

    def __init__(self): # include parameters?
        
        pg.init()
        self.screen = pg.display.get_surface()
        
    def car_blit(self, var_update, frame):
        
        # CAR 1 = BLUE CAR
        # CAR 2 = RED CAR

        # CAR1 ONTO SCREEN AT NEW POSITION
        pixel_pos_car1 = scalingC2P(var_update.car1_position[frame])
        size_car1 = C.blue_car.get_size()
        self.screen.blit(C.blue_car, (pixel_pos_car1[0] - size_car1[0]/2, pixel_pos_car1[1] - size_car1[1]/2))

        # CAR2 ONTO SCREEN AT NEW POSITION
        pixel_pos_car2 = scalingC2P(var_update.car1_postion[frame])
        size_car2 = C.red_car.get_size()
        self.screen.blit(C.red_car, (pixel_pos_car2[0] - size_car2[0]/2, pixel_pos_car2[1]- size_car2[1]/2))

        
        # DRAW BOUNDING BOX? RECTANGLE AROUND IMAGE BORDER
        # DO NOT THINK THE blue_edge_rect IS BEING USED, MAYBE A BETTER METHOD WOULD BE TO USE IT??? WOULD THIS AFFECT EXTENDING THE BOUNDING BOX VISUAL TO SOMETHING FURTHER THAN IMAGE EDGE???
        # OR DO WE WANT ANOTHER LIGHT GRAY BOX FURTHER OUT FOR ANOTHER BUFFER?
        blue_edge_rect = C.blue_car.get_rect() # gets car image rectangle dimensions
        pg.draw.rect(self.screen, C.LTLTGREY, ((round(pixel_pos_car1[0]-C.blue_car_width/2), round(pixel_pos_car1[1]-C.blue_car_height/2)), (C.blue_car_width, C.blue_car_height)), width = 1)
        pg.draw.rect(self.screen, C.LTLTGREY, ((round(pixel_pos_car2[0]-C.red_car_height/2), round(pixel_pos_car2[1]-C.red_car_width/2)), (C.red_car_height, C.red_car_width)), width = 1)

        # UPDATE SCREEN
        pg.display.flip()
        pg.display.update()

        # GET RID OF THE CAR IMAGE SO NEXT POSITION CAN BE SHOWN (this is how to do so with pygame)
        del_blue_car = C.blue_car.copy()
        del_red_car = C.red_car.copy()
        del_blue_car.fill(C.GRAY)
        del_red_car.fill(C.GRAY)
        self.screen.blit(del_blue_car, (pixel_pos_car1[0] - size_car1[0]/2, pixel_pos_car1[1] - size_car1[1]/2))
        self.screen.blit(del_red_car, (pixel_pos_car2[0] - size_car2[0]/2, pixel_pos_car2[1] - size_car2[1]/2))
    