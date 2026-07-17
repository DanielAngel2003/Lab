import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lorentz_oscillator(t, y, gamma, omega0):
    x, v = y
    # Equations: dx/dt = v, dv/dt = -gamma*v - omega0^2*x
    return [v, -gamma*v - (omega0**2)*x]

# Parameters
gamma = 0.5
omega0 = 2.0
t_span = (0, 50)
y0 = [1.0, 0.0]  # Initial displacement and velocity

sol = solve_ivp(lorentz_oscillator, t_span, y0, args=(gamma, omega0), t_eval=np.linspace(0, 50, 1000))

plt.plot(sol.t, sol.y[0])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.show()