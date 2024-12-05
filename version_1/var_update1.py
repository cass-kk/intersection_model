# store, update, and append global variables for use later in plots, etc.

class Variable_Data():

    def __init__(self):

        # will append the next value with each iteration in main.py file
        # will show past and current values with the current being the end of the np.array()
        self.car1position = [] # current position in x,y coordinates
        self.car1velocity = [] # current velocity in vx, vy
        self.car1acceleration = [] # current acceleration in ax, ay
        self.car1theta = [] # should be constant for now, can be used later for turning scenario

        self.car1futureTraj = [] # save future positions here

        self.car2position = [] # current position in x,y coordinates
        self.car2velocity = [] # current velocity in vx, vy
        self.car2acceleration = [] # current acceleration in ax, ay
        self.car2theta = [] # should be constant for now, can be used later for turning scenario

        self.car2futureTraj = [] # save future positions here


# believe the append functions below were used to literally display the future trajectory on the screen
    def car1_append(self, positions, vel, accel, theta, futureSteps):
        
        self.car1position = positions # fix to append to the end of this variable set?
        self.car1velocity = vel
        self.car1acceleration = accel
        self.car1theta = theta
        self.car1futureTraj = futureSteps

    def car2_append(self, positions, vel, accel, theta, futureSteps):
        
        self.car2position = positions # fix to append to the end of this variable set?
        self.car2velocity = vel
        self.car2acceleration = accel
        self.car2theta = theta
        self.car2futureTraj = futureSteps