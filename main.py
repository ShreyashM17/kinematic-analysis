import kinematic_analysis
import matplotlib.pyplot as plt

Crank_Radius = float(input("Enter the crank radius(m): "))
Connecting_rod_Length = float(input("Enter the connecting rod length(m): "))
Speed_of_Crank = float(input("Enter the Speed of crank(rpm): "))
velocity_of_piston = []
acceleration_of_piston = []
velocity_of_connecting_rod = []
acceleration_of_connecting_rod = []
crank_angle = []
Slider_analysis = kinematic_analysis.Slider(Connecting_rod_Length, Crank_Radius, Speed_of_Crank)
Connecting_rod = kinematic_analysis.Connecting_rod(Connecting_rod_Length, Crank_Radius, Speed_of_Crank)

for angle in range(0, 361, 30):
    Slider_displacement = Slider_analysis.distance_travelled_by_slider(angle)
    Slider_velocity = Slider_analysis.velocity(angle)
    Slider_acceleration = Slider_analysis.acceleration(angle)
    Connecting_rod_angular_displacement = Connecting_rod.angular_displacement(angle)
    Connecting_rod_angular_velocity = Connecting_rod.radial_velocity(angle)
    Connecting_rod_angular_acceleration = Connecting_rod.radial_acceleration(angle)
    velocity_of_piston.append(Slider_velocity)
    acceleration_of_piston.append(Slider_acceleration)
    velocity_of_connecting_rod.append(Connecting_rod_angular_velocity)
    acceleration_of_connecting_rod.append(Connecting_rod_angular_acceleration)
    crank_angle.append(angle)
    print(f"\n\n## For angle = {angle} ##\n --Slider\n Displacement= {Slider_displacement}\n Velocity = {Slider_velocity}\n "
          f"Acceleration = {Slider_acceleration} \n\n --Connecting Rod \n "
          f"Angular_displacement = {Connecting_rod_angular_displacement} \n "
          f"Angular Velocity = {Connecting_rod_angular_velocity} \n"
          f"Angular Acceleration = {Connecting_rod_angular_acceleration} \n\n")

plt.plot(crank_angle, velocity_of_piston)
plt.xlabel("Crank Angle")
plt.ylabel("Velocity of piston")
plt.title("Approx. velocity of Piston v/s Crank angle (θ)")
plt.show()
plt.plot(crank_angle, acceleration_of_piston)
plt.xlabel("Crank Angle")
plt.ylabel("Acceleration of piston")
plt.title("Approx. acceleration of Piston v/s Crank angle (θ)")
plt.show()
plt.plot(crank_angle, velocity_of_connecting_rod)
plt.xlabel("Crank Angle")
plt.ylabel("Velocity of connecting rod")
plt.title("Approx. velocity of connecting v/s Crank angle (θ)")
plt.show()
plt.plot(crank_angle, acceleration_of_connecting_rod)
plt.xlabel("Crank Angle")
plt.ylabel("Acceleration of connecting rod")
plt.title("Approx. acceleration of connecting rod v/s Crank angle (θ)")
plt.show()