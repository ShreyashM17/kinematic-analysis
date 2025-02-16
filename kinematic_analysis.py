from math import cos, sin, acos, asin, sqrt, pow, radians, degrees


class Kinematic_analysis:
    def __init__(self, length, radius):
        self.length = length
        self.radius = radius
        self.oblique_ratio = self.length / self.radius
        self.phi = 0
        self.theta = 0

    # Conversion from theta to phi and viceversa in radians
    def theta_to_phi(self, theta):
        self.theta = radians(theta)
        self.phi = asin(sin(self.theta)/self.oblique_ratio)
        return degrees(self.phi)

    def phi_to_theta(self, phi):
        self.phi = radians(phi)
        self.theta = asin(sin(phi) * self.oblique_ratio)
        return self.theta

    def get_value_theta_radians(self):
        return self.theta

    def get_value_phi_radians(self):
        return self.phi

    def get_value_theta_in_degree(self):
        return degrees(self.theta)

    def get_value_phi_in_degree(self):
        return degrees(self.phi)


class Slider(Kinematic_analysis):
    def __init__(self, length, radius, omega=0):
        super().__init__(length, radius)
        self.omega = 2*3.142*omega/60
        self.distance = 0
        self.vel = 0
        self.acc = 0

    def distance_travelled_by_slider(self, theta):
        theta = radians(theta)
        n = self.oblique_ratio
        self.distance = self.radius * (1 - cos(theta) + n - (sqrt(pow(n, 2) - pow(sin(theta), 2))))
        return self.distance

    def velocity(self, theta):
        theta = radians(theta)
        self.vel = self.omega * self.radius * (sin(theta) + (sin(2 * theta) / (2 * self.oblique_ratio)))
        return self.vel

    def acceleration(self, theta):
        theta = radians(theta)
        self.acc = self.omega * self.omega * self.radius * (cos(theta) + (cos(2 * theta) / self.oblique_ratio))
        return self.acc


class Connecting_rod(Kinematic_analysis):
    def __init__(self, length, radius, omega=0):
        super().__init__(length, radius)
        self.omega = 2*3.142*omega/60
        self.radial_vel = 0
        self.radial_acc = 0

    def angular_displacement(self, theta):
        angular_dis = self.theta_to_phi(theta)
        return angular_dis

    def radial_velocity(self, theta):
        theta = radians(theta)
        n = self.oblique_ratio
        self.radial_vel = (self.omega*cos(theta))/(sqrt(pow(n, 2)-pow(sin(theta), 2)))
        return self.radial_vel

    def radial_acceleration(self, theta):
        n = self.oblique_ratio
        theta = radians(theta)
        self.radial_acc = -(pow(self.omega, 2)*sin(theta))/n
        return self.radial_acc
