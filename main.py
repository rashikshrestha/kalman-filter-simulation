import numpy as np
from simulation import Simulation
from robot import Robot

sim =  Simulation((1024,768),'Kalman filter Simulation - Rashik Shrestha')
r = Robot()
r.define_static_matrices(0.1)
r.init_dynamic_matrices()

print(r.X)

while True:
    sim.handle_events()
    r.take_action(sim.button_state)
    r.check_boundary((1024,768))
    
    r.motion_model()
    r.sensor_model()
    r.apply_kalman()

    sim.update_screen(r.X,r.X_est,r.Z)

    print('Error = ' , r.X.flatten() - r.X_est.flatten() )