import numpy as np

class Robot:

    def __init__(self):
        pass

    def define_static_matrices(self,Ts):
        #State transition matrix
        self.A = np.array([[1,  0,  Ts,  0  ],
                           [0,  1,  0,    Ts],
                           [0,  0,  1,    0  ],
                           [0,  0,  0,    1  ]])

        #Control update matrix
        self.B = np.array([[(Ts*Ts)/2,   0         ],
                           [0,           (Ts*Ts)/2 ],
                           [Ts,          0         ],
                           [0,           Ts        ]])

        #Measurement update matrix
        self.H = np.array([[1,  0,  1,  0],
                           [0,  1,  0,  1],
                           [0,  0,  0,  0],
                           [0,  0,  0,  0]])

        #Action Uncertainity matrix   
        self.Q = np.array([[1,  0,  0,  0],
                           [0,  1,  0,  0],
                           [0,  0,  1,  0],
                           [0,  0,  0,  1]])

        #Sensor noise matrix
        self.R = np.array([[0.1,  0,  0,  0],
                           [0,  0.1,  0,  0],
                           [0,  0,  0.1,  0],
                           [0,  0,  0,  0.1]])

    def init_dynamic_matrices(self):
        self.X = np.array([[50],[50],[0],[0]])  # State matrix(mean)
        self.P = np.zeros((4,4))  # Covariance matrix
        self.U = np.zeros((2,1))  # Action matrix
        self.Z = np.zeros((4,1))  # Measurement matrix

        self.X_est = np.array([[50],[50],[0],[0]]) # State matrix estimation(mean)

    def motion_model(self):
        self.X = self.A @ self.X + self.B @ self.U + np.random.normal(0,0.1,4).reshape(4,1)

    def sensor_model(self):
        self.Z = self.H @ self.X + np.random.normal(0,7,4).reshape(4,1)

    def apply_kalman(self):

        self.X_est = self.A @ self.X + self.B @ self.U

        self.P = self.A @ self.P @ self.A.T + self.Q

        self.K   = self.P @ self.H.T @ np.linalg.inv(self.H @ self.P @ self.H.T + self.R)

        self.X_est = self.X_est + self.K @ (self.Z - self.H @ self.X)

        self.P = (np.eye(4,4) - self.K @ self.H) @ self.P


    def take_action(self, button_state):
        if button_state[0] == True:
            self.U = [[0],[-1]]

        elif button_state[1] == True:
            self.U = [[0],[1]]

        elif button_state[2] == True:
            self.U = [[-1],[0]]

        elif button_state[3] == True:
            self.U = [[1],[0]]

        else:
            self.U = [[0],[0]]

    def check_boundary(self, b):
        if self.X[0,0] < 0  or self.X[0,0] > b[0]:
            self.X[2,0] = -self.X[2,0]

        if self.X[1,0] < 0  or self.X[1,0] > b[1]:
            self.X[3,0] = -self.X[3,0]
        
        
