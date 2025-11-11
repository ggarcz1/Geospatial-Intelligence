import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

class Radar2D:
    def __init__(self, source=[0, 0], target=[10, 5]):
        self.source = source
        self.target = target
        self.t = 0  # time for animation

        # Tkinter GUI
        self.root = tk.Tk()
        self.root.title("2D Radar Screen")
        self.root.geometry("700x600")

        # Labels
        self.degrees_label = ttk.Label(self.root, text="Degrees: ")
        self.degrees_label.grid(row=0, column=0, padx=5, pady=5)
        self.heading_label = ttk.Label(self.root, text="Heading: ")
        self.heading_label.grid(row=1, column=0, padx=5, pady=5)
        self.elevation_label = ttk.Label(self.root, text="Elevation (simulated): ")
        self.elevation_label.grid(row=2, column=0, padx=5, pady=5)
        self.target_label = ttk.Label(self.root, text=f"Target: {self.target}")
        self.target_label.grid(row=3, column=0, padx=5, pady=5)

        # Figure and canvas
        self.fig, self.ax = plt.subplots(figsize=(5,5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=10, padx=10, pady=10)

        # Plot radar background
        self.plot_radar_background()
        self.update_plot()

        # Start animation
        self.root.after(50, self.animate)
        self.root.mainloop()

    def plot_radar_background(self):
        self.ax.clear()
        # Draw radar circles
        max_range = 20
        for r in range(5, max_range+5, 5):
            circle = plt.Circle((self.source[0], self.source[1]), r, color='gray', fill=False, linestyle='dashed')
            self.ax.add_artist(circle)

        # Draw cross lines
        self.ax.axhline(self.source[1], color='gray', linestyle='dashed')
        self.ax.axvline(self.source[0], color='gray', linestyle='dashed')

        # Axes settings
        self.ax.set_xlim(-max_range, max_range)
        self.ax.set_ylim(-max_range, max_range)
        self.ax.set_aspect('equal')
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_title("2D Radar Screen")

    def degrees_heading(self, src, tgt):
        dx = tgt[0] - src[0]
        dy = tgt[1] - src[1]
        angle = (math.degrees(math.atan2(dy, dx)) + 360) % 360
        # NSEW
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
        index = round(angle / 45) % 8
        return angle, directions[index]

    def update_plot(self):
        self.plot_radar_background()
        # Draw source
        self.ax.scatter(*self.source, color='red', s=80, marker='^', label='Source')
        # Draw target
        self.ax.scatter(*self.target, color='blue', s=60, label='Target')

        # Draw vector line
        self.ax.plot([self.source[0], self.target[0]],
                     [self.source[1], self.target[1]], color='green', linewidth=2)

        # Update degrees and heading
        deg, heading = self.degrees_heading(self.source, self.target)
        self.degrees_label.config(text=f"Degrees: {deg:.1f}°")
        self.heading_label.config(text=f"Heading: {heading}")
        # Simulated elevation (Z axis can be arbitrary)
        elevation = 10 * math.sin(math.radians(deg))  # just for demo
        self.elevation_label.config(text=f"Elevation: {elevation:.1f}")
        self.target_label.config(text=f"Target: {[round(c,2) for c in self.target]}")

        self.ax.legend()
        self.canvas.draw()

    def animate(self):
        # Move target in a circular pattern around source
        self.t += 0.05
        radius = 15
        self.target[0] = self.source[0] + radius * math.cos(self.t)
        self.target[1] = self.source[1] + radius * math.sin(self.t)
        self.update_plot()
        self.root.after(50, self.animate)  # call again after 50ms for smooth animation (~20fps)

# --- Example usage ---
if __name__ == "__main__":
    Radar2D()
