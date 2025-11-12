import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
time = np.linspace(0, 10, 200)  # 10 seconds, 200 steps
tilt = np.zeros_like(time)       # tilt angle in radians
correction = np.zeros_like(time) # correction applied

np.random.seed(0)  # for reproducible randomness

# Simulate balance
for i in range(1, len(time)):
    # Random disturbance to simulate uneven walking
    disturbance = np.random.normal(0, 0.05)
    
    # Simple proportional controller: try to reduce tilt
    correction[i] = -0.5 * tilt[i-1]
    
    # Update tilt: previous tilt + disturbance + correction
    tilt[i] = tilt[i-1] + disturbance + correction[i]

# Plot results
plt.figure(figsize=(8,5))
plt.plot(time, tilt, label='Tilt Angle')
plt.plot(time, correction, label='Correction Applied', linestyle='--')
plt.title("Balance Simulation")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.legend()
plt.grid(True)
plt.savefig("balance_demo.png")
plt.show()