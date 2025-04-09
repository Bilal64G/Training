import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return n
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(x, y), max_iter) for x in r1] for y in r2])

# Set up the plot
fig = plt.figure(figsize=(8, 8))
ax = plt.axes()
img = ax.imshow(np.zeros((800, 800)), extent=[-2, 1, -1.5, 1.5], cmap='hot')

def update(frame):
    zoom = 0.97 ** frame
    x_center, y_center = -0.75, 0.0
    range_x = 3.0 * zoom
    range_y = 3.0 * zoom

    xmin = x_center - range_x / 2
    xmax = x_center + range_x / 2
    ymin = y_center - range_y / 2
    ymax = y_center + range_y / 2

    Z = mandelbrot_set(xmin, xmax, ymin, ymax, 800, 800, 100)
    img.set_data(Z)
    img.set_extent([xmin, xmax, ymin, ymax])
    ax.set_title(f"Zoom Level: {frame}")
    return [img]

ani = animation.FuncAnimation(fig, update, frames=100, blit=True)
plt.show()
