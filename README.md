# Balance Simulation

A simple Python simulation demonstrating balance control. The simulation models a tilting object and applies a basic correction to keep it upright.

This project is beginner-friendly and shows how small feedback mechanisms can stabilize a system, similar to concepts used in robotics and control theory.

![output](https://github.com/AnthonyBraak/balance-control/blob/main/balance_demo.png)

## Features

Simulates tilt over time with random disturbances

Applies a simple proportional controller to maintain balance

Plots tilt angle and correction over time

Generates a graph that visualizes the system's behavior

## Requirements

Python 3.x

NumPy

Matplotlib

## Install dependencies with:

```pip install numpy matplotlib```

## Usage

### Clone the repository:

```
git clone https://github.com/AnthonyBraak/balance-control.git
cd balance-simulation
```

### Run the simulation:
```
python pid.py
```

A graph will appear showing tilt angles and corrections over time. A PNG image humanoid_balance_demo.png will also be saved.

### Example Output

Tilt Angle: Shows how the object wobbles over time

Correction Applied: Shows how the controller stabilizes the system
