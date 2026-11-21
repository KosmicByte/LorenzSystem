import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# Define Lorenz System Equations and Parameters

def lorenz(t, state, sigma=10, rho=28, beta=8/3,):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x*(rho-z) - y
    dz_dt = x*y - beta*z
    return dx_dt, dy_dt, dz_dt

# Set Initial Conditions and Time Span - Simulation Parameters

# Define the time range over which we want to simulate the system.
# t_span = (start_time, end_time), so we simulate from t = 0 to t = 40.
t_span = (0, 40)


# Create an array of time points where the solution will be evaluated.
# np.linspace(start, end, num_points) generates 5000 evenly spaced points between 0 and 40.
# This gives us a smooth and high-resolution simulation.
t_eval = np.linspace(*t_span, 5000)

# Initial condition
initial_state = [8.0, 8.0, 8.0]


'''Methods to solve the ODE system.
One is without RK45 method and the other is with it.'''

#METHOD 1 - WITHOUT RK 45

# Solve the ODE system
sol = solve_ivp(lorenz, t_span, initial_state, t_eval=t_eval)


# Results
x, y, z = sol.y


# Plotting the Lorenz Attractor

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, lw=0.7, color='red')
ax.set_title('Lorenz Attractor – Static 3D View')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

# Animating the Lorenz Attractor

