import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Vectoring:
    def __init__(self):
        return
    
    def degrees_calculate(self, p1: list, p2: list, decimal: int = 0) -> float:
        """Calculate 2D angle from p1 to p2 in XY-plane (0° = East)."""
        if decimal < 0:
            return -1
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        angle_radians = math.atan2(dy, dx)
        angle_degrees = math.degrees(angle_radians)
        angle_degrees = (angle_degrees + 360) % 360
        return round(angle_degrees, decimal)
    
    def get_nsew(self, degrees: float) -> str:
        degrees %= 360
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
        index = round(degrees / 45) % 8
        return directions[index]

    def get_heading_points(self, heading_degrees):
        # Convert compass heading from degrees to radians
        theta = math.radians(90)  # Polar angle (θ) is 90 degrees
        phi = math.radians(90 - heading_degrees)  # Azimuthal angle (φ) is 90 degrees - compass heading

        # Define radius
        r = 1  # Assuming unit radius for simplicity

        # Calculate Cartesian coordinates using spherical to Cartesian conversion
        x_coordinate = r * math.sin(theta) * math.cos(phi)
        y_coordinate = r * math.sin(theta) * math.sin(phi)
        z_coordinate = r * math.cos(theta)
        return [x_coordinate, y_coordinate, z_coordinate]

    # TODO:
    def plot_vector_to_target(self, p1: list, p2: list) -> float:
        """Launch a simple 2D GUI to plot vector from p1 to p2."""
        class VectorGUI(tk.Tk):
            def __init__(self, v_obj, p1, p2):
                super().__init__()
                self.title("2D Vector Chart")
                self.geometry("700x500")
                self.v_obj = v_obj
                self.p1 = p1
                self.p2 = p2

                # Labels for degrees & heading
                self.degrees_label = ttk.Label(self, text="Degrees: ")
                self.degrees_label.grid(row=0, column=0, padx=5, pady=5)
                self.heading_label = ttk.Label(self, text="Heading: ")
                self.heading_label.grid(row=1, column=0, padx=5, pady=5)

                # Plot figure
                self.fig, self.ax = plt.subplots(figsize=(5,4))
                self.canvas = FigureCanvasTkAgg(self.fig, master=self)
                self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=10, padx=10, pady=10)

                self.plot_vector()

            def plot_vector(self):
                self.ax.clear()
                self.ax.plot([self.p1[0], self.p2[0]], [self.p1[1], self.p2[1]],
                             marker='o', color='blue')
                self.ax.annotate("P1", self.p1, textcoords="offset points", xytext=(-10,10))
                self.ax.annotate("P2", self.p2, textcoords="offset points", xytext=(-10,10))
                self.ax.set_xlabel("X")
                self.ax.set_ylabel("Y")
                self.ax.set_title("2D Vector Chart")
                self.ax.grid(True)
                self.ax.axis('equal')

                # Calculate and display degrees & heading
                degrees = self.v_obj.degrees_calculate(self.p1, self.p2, decimal=0)
                heading = self.v_obj.get_nsew(degrees)
                self.degrees_label.config(text=f"Degrees: {degrees}°")
                self.heading_label.config(text=f"Heading: {heading}")

                self.canvas.draw()

        # Launch GUI
        app = VectorGUI(self, p1, p2)
        app.mainloop()
        # Return degrees and heading for programmatic use
        deg = self.degrees_calculate(p1, p2, decimal=0)
        head = self.get_nsew(deg)
        return deg, head


