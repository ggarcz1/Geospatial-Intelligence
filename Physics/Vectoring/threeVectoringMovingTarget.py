import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import numpy as np
from scipy.interpolate import CubicSpline

class Radar2DSmooth:
    def __init__(self, source=[0,0], waypoints=None, loop=True, frame_delay=50):
        self.source = source
        self.waypoints = waypoints or [[10,5], [15,10], [5,15], [-5,10], [-10,0], [-5,-5], [5,-5]]
        self.loop = loop
        self.frame_delay = frame_delay  # ms between frames

        # Prepare smooth path using cubic spline
        self.smooth_path = self.create_smooth_path(self.waypoints, steps=400)
        self.path_index = 0
        self.target = self.smooth_path[self.path_index]

        # Tkinter GUI
        self.root = tk.Tk()
        self.root.title("2D Radar Screen - Smooth Target")
        self.root.geometry("800x650")

        # Labels
        self.degrees_label = ttk.Label(self.root, text="Degrees: ")
        self.degrees_label.grid(row=0, column=0, padx=5, pady=5)
        self.heading_label = ttk.Label(self.root, text="Heading: ")
        self.heading_label.grid(row=1, column=0, padx=5, pady=5)
        self.elevation_label = ttk.Label(self.root, text="Elevation: ")
        self.elevation_label.grid(row=2, column=0, padx=5, pady=5)
        self.target_label = ttk.Label(self.root, text=f"Target: {self.target}")
        self.target_label.grid(row=3, column=0, padx=5, pady=5)

        # Figure and canvas
        self.fig, self.ax = plt.subplots(figsize=(7,7))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=10, padx=10, pady=10)

        # Draw radar background once
        self.max_range = 25
        self.plot_radar_background()

        # Plot source once
        self.ax.scatter(*self.source, color='red', s=80, marker='^', label='Source')

        # Plot target marker and vector line (we'll update these)
        self.target_marker, = self.ax.plot(self.target[0], self.target[1], 'bo', markersize=8, label='Target')
        self.vector_line, = self.ax.plot([self.source[0], self.target[0]],
                                         [self.source[1], self.target[1]], 'g-', linewidth=2)

        # Legend
        self.ax.legend()
        self.canvas.draw()

        # Start animation
        self.root.after(self.frame_delay, self.animate)
        self.root.mainloop()

    def create_smooth_path(self, waypoints, steps=400):
        waypoints = np.array(waypoints)
        t_points = np.linspace(0, 1, len(waypoints))  # normalized waypoint positions

        # Cubic spline interpolation for X and Y
        cs_x = CubicSpline(t_points, waypoints[:,0], bc_type='periodic')
        cs_y = CubicSpline(t_points, waypoints[:,1], bc_type='periodic')

        t_smooth = np.linspace(0, 1, steps)
        smooth_path = np.array([[cs_x(t), cs_y(t)] for t in t_smooth])
        return smooth_path

    def plot_radar_background(self):
        # Draw radar circles and crosshairs
        for r in range(5, self.max_range+5, 5):
            circle = plt.Circle((self.source[0], self.source[1]), r, color='gray', fill=False, linestyle='dashed')
            self.ax.add_artist(circle)
        self.ax.axhline(self.source[1], color='gray', linestyle='dashed')
        self.ax.axvline(self.source[0], color='gray', linestyle='dashed')
        self.ax.set_xlim(-self.max_range, self.max_range)
        self.ax.set_ylim(-self.max_range, self.max_range)
        self.ax.set_aspect('equal')
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_title("2D Radar Screen - Smooth Target")

    def degrees_heading(self, src, tgt):
        dx = tgt[0] - src[0]
        dy = tgt[1] - src[1]
        angle = (math.degrees(math.atan2(dy, dx)) + 360) % 360
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
        index = round(angle / 45) % 8
        return angle, directions[index]

    def animate(self):
        # Move target along smooth path
        self.target = self.smooth_path[self.path_index]
        self.path_index += 1
        if self.path_index >= len(self.smooth_path):
            if self.loop:
                self.path_index = 0
            else:
                self.path_index = len(self.smooth_path) - 1

        # Update target marker and vector line
        self.target_marker.set_data(self.target[0], self.target[1])
        self.vector_line.set_data([self.source[0], self.target[0]], [self.source[1], self.target[1]])

        # Update labels
        deg, heading = self.degrees_heading(self.source, self.target)
        elevation = 10 * math.sin(math.radians(deg))  # simulated elevation
        self.degrees_label.config(text=f"Degrees: {deg:.1f}°")
        self.heading_label.config(text=f"Heading: {heading}")
        self.elevation_label.config(text=f"Elevation: {elevation:.1f}")
        self.target_label.config(text=f"Target: {[round(c,2) for c in self.target]}")

        # Redraw canvas
        self.canvas.draw()
        self.root.after(self.frame_delay, self.animate)


# --- Example usage ---
if __name__ == "__main__":
    waypoints = [[10,5], [15,10], [5,15], [-5,10], [-10,0], [-5,-5], [5,-5], [10,5]]  # first=last

    Radar2DSmooth(source=[0,0], waypoints=waypoints, loop=True, frame_delay=100)
