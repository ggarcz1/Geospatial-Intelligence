import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

class Vectoring:
    def __init__(self):
        pass

    def degrees_calculate(self, p1: list, p2: list, decimal: int = 0) -> float:
        """Calculate 2D angle from p1 to p2 in XY-plane (0° = East)."""
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        angle_radians = math.atan2(dy, dx)
        angle_degrees = math.degrees(angle_radians)
        angle_degrees = (angle_degrees + 360) % 360
        return round(angle_degrees, decimal)

    def get_nsew(self, degrees: float) -> str:
        """Return NSEW heading for degrees."""
        degrees %= 360
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
        index = round(degrees / 45) % 8
        return directions[index]

    def elevation_angle(self, p1: list, p2: list, decimal: int = 2) -> float:
        """Calculate elevation angle (degrees above horizontal XY-plane)."""
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        dz = p2[2] - p1[2]
        horizontal_distance = math.sqrt(dx**2 + dy**2)
        angle_rad = math.atan2(dz, horizontal_distance)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg, decimal)

    def plot_vector_to_target_3d(self, p1: list, p2: list):
        """Launch a 3D GUI to plot vector from p1 to p2 with elevation."""
        class VectorGUI3D(tk.Tk):
            def __init__(self, v_obj, p1, p2):
                super().__init__()
                self.title("3D Vector Chart with Elevation and Coordinates")
                self.geometry("950x600")
                self.v_obj = v_obj
                self.p1 = p1
                self.p2 = p2

                # Labels for coordinates
                self.source_label = ttk.Label(self, text=f"Source (P1): {p1}")
                self.source_label.grid(row=0, column=0, padx=5, pady=5)
                self.target_label = ttk.Label(self, text=f"Target (P2): {p2}")
                self.target_label.grid(row=1, column=0, padx=5, pady=5)

                # Labels for degrees, heading, elevation
                self.degrees_label = ttk.Label(self, text="Degrees (XY-plane): ")
                self.degrees_label.grid(row=2, column=0, padx=5, pady=5)
                self.heading_label = ttk.Label(self, text="Heading (XY-plane): ")
                self.heading_label.grid(row=3, column=0, padx=5, pady=5)
                self.elevation_label = ttk.Label(self, text="Elevation (relative to horizon): ")
                self.elevation_label.grid(row=4, column=0, padx=5, pady=5)

                # 3D Figure
                self.fig = plt.figure(figsize=(7,5))
                self.ax = self.fig.add_subplot(111, projection='3d')
                self.canvas = FigureCanvasTkAgg(self.fig, master=self)
                self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=10, padx=10, pady=10)

                self.plot_vector()

            def plot_vector(self):
                self.ax.clear()
                # Plot points
                self.ax.scatter(*self.p1, color='red', s=50, label='P1')
                self.ax.scatter(*self.p2, color='blue', s=50, label='P2')

                # Draw vector
                self.ax.plot([self.p1[0], self.p2[0]],
                             [self.p1[1], self.p2[1]],
                             [self.p1[2], self.p2[2]],
                             color='green', linewidth=2, label='Vector')

                # Labels
                self.ax.text(*self.p1, f"P1\n{self.p1}", color='red')
                self.ax.text(*self.p2, f"P2\n{self.p2}", color='blue')

                # Axes labels
                self.ax.set_xlabel("X")
                self.ax.set_ylabel("Y")
                self.ax.set_zlabel("Z")
                self.ax.set_title("3D Vector Plot with Elevation and Coordinates")
                self.ax.legend()
                self.ax.grid(True)
                self.ax.view_init(elev=25, azim=-60)

                # Degrees, heading, elevation
                degrees = self.v_obj.degrees_calculate(self.p1, self.p2, decimal=0)
                heading = self.v_obj.get_nsew(degrees)
                elevation = self.v_obj.elevation_angle(self.p1, self.p2, decimal=2)

                self.degrees_label.config(text=f"Degrees (XY-plane): {degrees}°")
                self.heading_label.config(text=f"Heading (XY-plane): {heading}")
                self.elevation_label.config(text=f"Elevation: {elevation}°")

                self.canvas.draw()

        app = VectorGUI3D(self, p1, p2)
        app.mainloop()

        deg = self.degrees_calculate(p1, p2, decimal=0)
        head = self.get_nsew(deg)
        elev = self.elevation_angle(p1, p2, decimal=2)
        return deg, head, elev


