from const import Constants as C

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class dyn:
    
    def __init__(self, vehicle):

        self.P_CAR = vehicle
    
    # pass through 1 or s for use across two files
    # if/else within function file
    # if third parameter is 1 then use it the way AV.py does
    # if third parameter is not 1 then use it the way loss_func.py does

    
    def dyn_future(self):
        x0 = self.P_CAR.positions[0][0]
        y0 = self.P_CAR.positions[0][1]
        vx0 = self.P_CAR.vel[0][0]
        vy0 = self.P_CAR.vel[0][1]
        u0 = self.P_CAR.accel
        accel_x = u0[0][0]
        accel_y = u0[0][1]
        S_0 = [x0, y0, vx0, vy0]
        t = np.linspace(0, 1, 100)

        def ode_eqn(t, S): # dSdt side of ODE equation
            
            x, vx, y, vy = S

            x_dot = vx # velocity in the x direction
            #vx_dot = (2/t^2)*(x - vx0 - vx0*t) # acceleration in the x direction
            vx_dot = accel_x

            y_dot = vy # velocity in the y direction
            #vy_dot = (2/t^2)*(y - vy0 - vy0*t) # acceleration in the y direction
            vy_dot = accel_y

            return np.array[x_dot, vx_dot, y_dot, vy_dot]


        sol = solve_ivp(ode_eqn, t_span=(0, max(t)), y0=S_0, method='RK45')

        return sol.y # hopefully includes first time steps for position, velocity, and acceleration
        """
        t_step_evaluation = sol.t
        y_evaluation = sol.y # not the y-direction but vector y where y_dot = Ay
        """
    
    # NEED TO RETURN PREDICT_RESULT_TRAJ   
    # STORE PREDICT_RESULT_VELOCITY -> GRAPH?
    # NEED TO CHANGE VALUES BASED ON WHICH MODEL IS PREDICTING WHO

"""

# https://www.youtube.com/watch?v=vNoFdtcPFdk


    def rk45_solve(self, fun, t_span, y0, t_bound):

        sol = solve_ivp(fun, t_span, y0, method='RK45')

        return sol

"""