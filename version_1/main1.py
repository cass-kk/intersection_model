from screen1 import bkgnd
from const1 import Constants as C
from const1 import CarDef
from car_update1 import car_initialize
from car_update1 import car_update
from var_update1 import Variable_Data
"""
from av1 import AV
"""
import pygame as pg

class Main():
    def __init__(self):

        # initialize screen and display background
        pg.init()
        self.screen = pg.display.set_mode((C.screen_x, C.screen_y))
        self.bkgnd = bkgnd()
        pg.display.flip() # update full display to screen

        
        # SIMULATION CONTROLS
        self.frame = 0 # frame = current screen iteration
        self.running = True
        self.paused = False
        self.end = False
        self.duration = 100
        self.car_num_display = 0
        
        

        self.car_init = car_initialize() # everything in terms of C.blue_car and C.red_car from images
        self.car_update = car_update() # screen blit the cars in terms of C.blue_car and C.red_car
        pg.display.update() # screen update
        

        # INITIALIZE PARAMETERS FOR VEHICLES AND SCENARIO
        self.var_data = Variable_Data()
        self.P = CarDef # initialize some variables
        self.scenario_parameters = self.P
        self.car1_param = self.P.CAR1
        self.car2_param = self.P.CAR2

        # Get first actions for both cars
        """
        # work in progress
        self.car1 = AV(self.scenario_parameters, self.car1_param)
        self.car2 = AV(self.scenario_parameters, self.car2_param)
        """

        # Assign the "other" car image, position, action set
        self.car1.other_car = self.car2
        self.car2.other_car = self.car1
        self.car1.pos_o = self.car2.position
        self.car2.pos_o = self.car1.position
        self.car1.actions_seto = self.car2.actions_set # future actions/trajectory
        self.car2.actions_seto = self.car1.actions_set # future actions/trajectory

        # call on simulation function
        self.sim()
    

    def sim(self):
        while self.running:

            if not self.paused:
                self.car1.update(self.frame) # From av.py
                self.car2.update(self.frame)


                self.var_update.car1_append(positions=self.car1.position,
                                            vel=self.car1.velocity,
                                            accel=self.car1.acceleration,
                                            theta=self.car1.theta,
                                            futureSteps=self.car1.futureSteps)
                
                self.var_update.car2_append(positions=self.car2.position,
                                            vel=self.car2.velocity,
                                            accel=self.car2.acceleration,
                                            theta=self.car2.theta,
                                            futureSteps=self.car2.futureSteps)
            if self.frame >= self.duration:
                break

            if C.draw_screen:

                # UPDATE SCREEN WITH NEW INFORMATION HERE
                self.car_update.car_blit(self.var_data, self.car_num_display, self.frame)
                    # car_num_dipslay used in reference code to show updated predicted positions of the other vehicle

                for event in pg.event.get(): # pygame's handling of queues
                    if event.type == pg.QUIT: # https://www.pygame.org/docs/ref/event.html
                        pg.quit()
                        self.running = False
                    elif event.type == pg.KEYDOWN: # https://www.pygame.org/docs/ref/key.html
                        if event.key == pg.K_p:
                            self.paused = not self.paused
                        if event.key == pg.K_q:
                            pg.quit()
                            self.running = False
                        if event.key == pg.K_d:
                            self.car_num_display = ~self.car_num_display
            
        pg.quit()
        print("SIMULATION ENDED.")

if __name__ == "__main__":
    Main()