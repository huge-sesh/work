class Movement(object):
    def acceleration(self, time):
        if self.accel_time != 0: return self.max_speed / self.accel_time * time
        else: return self.max_speed

    def deceleration(self, time):
        if self.decel_time != 0: return self.max_speed / self.decel_time * time
        else: return self.max_speed

    def air_acceleration(self, time):
        if self.air_accel_time != 0: return self.max_speed / self.air_accel_time * time
        else: return self.max_speed

class Momentum(Movement):
    def __init__(self):
        super(Momentum, self).__init__()
        self.max_speed = 20.0
        self.accel_time = 0.002
        self.decel_time = 0.004
        self.air_accel_time = 0.02
        self.jump_force = 10.0
        self.speed_bonus = 5.0

class Instant(Movement):
    def __init__(self):
        super(Instant, self).__init__()
        self.max_speed = 20.0
        self.accel_time = 0
        self.decel_time = 0
        self.air_accel_time = 0
        self.jump_force = 10.0
        self.speed_bonus = 5.0
