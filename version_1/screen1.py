# draw elements onto screen, coordinate conversions

# included class(es): bkgnd
# included def(s): scalingC2P, scalingP2C

import pygame as pg
import pygame.gfxdraw
import numpy as np
from const1 import Constants as C


class bkgnd():
        
    def __init__(self):
        
        pg.init()
        self.screen = pg.display.set_mode((C.screen_x, C.screen_y)) # will be full screen if set to (0,0) -> in pixels
        
        # COLORS
        DKGREEN = C.DKGREEN
        BLACK = C.BLACK
        GRAY = C.GRAY
        YELLOW = C.YELLOW
        GOLD = C.GOLD
        KHAKI = C.KHAKI
        DKKHAKI = C.DKKHAKI
        WHITE = C.WHITE
        
        self.screen.fill(DKGREEN) # fill the screen with a color to wipe away anything from last frame


        # ROAD SURFACE rectangles
        pygame.gfxdraw.box(self.screen, C.hrect, GRAY)
        pygame.gfxdraw.box(self.screen, C.vrect, GRAY)
       

        # WHITE LANE LINES
        # Left
        pygame.gfxdraw.hline(self.screen, 0, C.rd_724, C.rd_217, WHITE) # top lane line
        pygame.gfxdraw.hline(self.screen, 0, C.rd_724, C.rd_514, WHITE) # bottom lane line
        
        # Right
        pygame.gfxdraw.hline(self.screen, C.rd_1219, C.screen_x, C.rd_217, WHITE) # top lane line
        pygame.gfxdraw.hline(self.screen, C.rd_1219, C.screen_x, C.rd_514, WHITE) # bottom lane line

        # Top
        pygame.gfxdraw.vline(self.screen, C.rd_823, 0, C.rd_118, WHITE) # left lane line
        pygame.gfxdraw.vline(self.screen, C.rd_1120, 0, C.rd_118, WHITE) # right lane line

        # Bottom
        pygame.gfxdraw.vline(self.screen, C.rd_823, C.rd_613, C.screen_y, WHITE) # left lane line
        pygame.gfxdraw.vline(self.screen, C.rd_1120, C.rd_613, C.screen_y, WHITE) # right lane line


        # Draw the DOUBLE YELLOW lane divide
        pygame.gfxdraw.box(self.screen, (0, C.rd_316, C.rd_724, C.yellow_spacing_x), YELLOW) # double yellow left
        pygame.gfxdraw.box(self.screen, (0, C.rd_415, C.rd_724, C.yellow_spacing_x), YELLOW)

        pygame.gfxdraw.box(self.screen, (C.rd_1219, C.rd_316, (C.screen_x - C.rd_1219), C.yellow_spacing_x), YELLOW) # double yellow right
        pygame.gfxdraw.box(self.screen, (C.rd_1219, C.rd_415, (C.screen_x - C.rd_1219), C.yellow_spacing_x), YELLOW)

        pygame.gfxdraw.box(self.screen, (C.rd_922, 0, C.yellow_spacing_y, C.rd_118), YELLOW) # double yellow top
        pygame.gfxdraw.box(self.screen, (C.rd_1021, 0, C.yellow_spacing_y, C.rd_118), YELLOW)

        pygame.gfxdraw.box(self.screen, (C.rd_922, C.rd_613, C.yellow_spacing_y, (C.screen_y - C.rd_613)), YELLOW) # double yellow bottom
        pygame.gfxdraw.box(self.screen, (C.rd_1021, C.rd_613, C.yellow_spacing_y, (C.screen_y - C.rd_613)), YELLOW)


        # BLACK STOP lines
        # Left
        pygame.gfxdraw.vline(self.screen, C.rd_724, C.rd_415 + C.yellow_width_x, C.rd_613, BLACK)
        # Right
        pygame.gfxdraw.vline(self.screen, C.rd_1219, C.rd_118, C.rd_316, BLACK)
        # Top
        pygame.gfxdraw.hline(self.screen, C.rd_724, C.rd_922, C.rd_118, BLACK)
        # Bottom
        pygame.gfxdraw.hline(self.screen, C.rd_1021 + C.yellow_width_y, C.rd_1219, C.rd_613, BLACK)


        pg.display.flip() # put work onto screen

"""
def scaling1(coordinates): # coordinates to pixel (reference code)

    x = C.coord_scale * (coordinates[0] - C.origin_c[0] + C.screen_x_c/2)
    y = C.coord_scale * (-coordinates[1] + C.origin_c[1] + C.screen_y_c/2)
    x = int((x - C.screen_x_c * C.coord_scale * 0.5) + C.screen_x_c * C.coord_scale * 0.5)
    y = int((y - C.screen_y_c * C.coord_scale * 0.5) + C.screen_y_c * C.coord_scale * 0.5)

    return np.array([x,y])
"""
    
def scalingP2C(coordinates): # this is pixel (x,y) to coordinate scale (x,y)

    x = round(coordinates[0] / C.scale_x)
    y = round(coordinates[1] / C.scale_y)

    return np.array([x,y])

def scalingC2P(coordinates): # this is coordinate (x,y) to pixel scale (x,y)

    x = round(coordinates[0] * C.scale_x)
    y = round(coordinates[1] * C.scale_y)

    return np.array([x,y])
