"""
Very simply PID implementation
"""

class PID:

    def __init__(self, P=.1, I=0.0, D=10.0, Derivator=0, Integrator=0, Integrator_max=500, Integrator_min=-500):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.Derivator = Derivator
        self.Integrator = Integrator
        self.Integrator_max = Integrator_max
        self.Integrator_min = Integrator_min
        self.set_point = 0.0

    def update(self, current_value):
        error = self.set_point - current_value

        self.P_value = self.Kp * error
        self.D_value = self.Kd * ( error - self.Derivator)
        self.Derivator = error

        self.Integrator = self.Integrator + error

        if self.Integrator > self.Integrator_max:
            self.Integrator = self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = self.Integrator_min

        self.I_value = self.Integrator * self.Ki

        PID = self.P_value + self.I_value + self.D_value

        return PID
