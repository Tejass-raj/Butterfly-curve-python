import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Figure setup
fig, ax = plt.subplots(figsize=(6, 10), facecolor='black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

#butterfly curve function
t = np.linspace(0, 12 * np.pi, 4000)
r = np.exp(np.cos(t)) - 2*np.cos(4*t) + np.sin(t/12)**5
x = np.sin(t) * r
y = np.cos(t) * r

#Scale to fit

x *= 70
y *= 70

line, = ax.plot([], [], lw=2, color='white',)
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)

#Animation function
def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

#Create animation
ani = FuncAnimation(fig, update, frames=len(t), interval=1, blit=True)

plt.show()