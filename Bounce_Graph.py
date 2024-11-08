import matplotlib.pyplot as plt

# Constants
GRAVITY = 9.81      # m/s^2
BOUNCE_FACTOR = 0.7 # Fraction of energy retained after a bounce
TIME_STEP = 0.01    # Time step for simulation in seconds

# Initial conditions
height = 10.0       # meters
velocity = 0.0      # m/s

# Simulation arrays
earth_times = [0.0]
earth_heights = [height]

# Simulation loop
for i in range(1000):
#while height > 0.0:
    # Compute acceleration (due to gravity)
    acceleration = -GRAVITY
    
    # Update velocity and height using Euler's method
    velocity += acceleration * TIME_STEP
    height += velocity * TIME_STEP
    
    # If the ball hits the ground, bounce it
    if height < 0.0:
        height = -height * BOUNCE_FACTOR
        velocity = -velocity * BOUNCE_FACTOR
    
    # Record time and height in simulation arrays
    earth_times.append(earth_times[-1] + TIME_STEP)
    earth_heights.append(height)

#=================================

GRAVITY = 1.62      # m/s^2
BOUNCE_FACTOR = 0.7 # Fraction of energy retained after a bounce
TIME_STEP = 0.01    # Time step for simulation in seconds

# Initial conditions
height = 10.0       # meters
velocity = 0.0      # m/s

# Simulation arrays
moon_times = [0.0]
moon_heights = [height]

# Simulation loop
for i in range(1000):
#while height > 0.0:
    # Compute acceleration (due to gravity)
    acceleration = -GRAVITY
    
    # Update velocity and height using Euler's method
    velocity += acceleration * TIME_STEP
    height += velocity * TIME_STEP
    
    # If the ball hits the ground, bounce it
    if height < 0.0:
        height = -height * BOUNCE_FACTOR
        velocity = -velocity * BOUNCE_FACTOR
    
    # Record time and height in simulation arrays
    moon_times.append(moon_times[-1] + TIME_STEP)
    moon_heights.append(height)

#=================================

GRAVITY = 3.71      # m/s^2
BOUNCE_FACTOR = 0.7 # Fraction of energy retained after a bounce
TIME_STEP = 0.01    # Time step for simulation in seconds

# Initial conditions
height = 10.0       # meters
velocity = 0.0      # m/s

# Simulation arrays
mars_times = [0.0]
mars_heights = [height]

# Simulation loop
for i in range(1000):
#while height > 0.0:
    # Compute acceleration (due to gravity)
    acceleration = -GRAVITY
    
    # Update velocity and height using Euler's method
    velocity += acceleration * TIME_STEP
    height += velocity * TIME_STEP
    
    # If the ball hits the ground, bounce it
    if height < 0.0:
        height = -height * BOUNCE_FACTOR
        velocity = -velocity * BOUNCE_FACTOR
    
    # Record time and height in simulation arrays
    mars_times.append(mars_times[-1] + TIME_STEP)
    mars_heights.append(height)


# Plot the simulation results
plt.plot(moon_times, moon_heights, label="Moon", color = "grey")
plt.plot(mars_times, mars_heights, label="Mars", color = "red")
plt.plot(earth_times, earth_heights, label="Earth", color = "blue")
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.legend(loc="upper right")
plt.show()

