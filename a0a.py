# import tkinter as tk
# import math

# class PointMover(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Point Mover")
#         self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
#         self.canvas.pack()

#         # Initial positions for point A and point B
#         self.point_a = (50, 300)  # Fixed position for Point A
#         self.point_b = (300, 200)  # Initial position for Point B

#         # Draw points
#         self.canvas.create_oval(self.point_a[0] - 5, self.point_a[1] - 5,
#                                 self.point_a[0] + 5, self.point_a[1] + 5,
#                                 fill="red", tags="point_a")
#         self.point_b_id = self.canvas.create_oval(self.point_b[0] - 5, self.point_b[1] - 5,
#                                                   self.point_b[0] + 5, self.point_b[1] + 5,
#                                                   fill="blue", tags="point_b")

#         # Display value
#         # self.value_label = tk.Label(self, text=f"Point B Coordinates: ({self.point_b[0]}, {self.point_b[1]})")
#         aoa = math.atan((self.point_b[1]-self.point_a[1])/(self.point_b[0]-self.point_a[0])) * (180/math.pi)
#         # math.atan((p2[1]-p1[1])/(p2[0]-p1[0])) * (180/math.pi)
#         # print()

#         # print(self.point_b[1]-self.point_a[1])
#         # print(self.point_b[0]-self.point_a[0])
    
#         # print(self.point_a, self.point_b)
#         self.value_label = tk.Label(self, text=f"AOA: {aoa}")
#         self.value_label.pack()

#         # Bind mouse events to point B
#         self.canvas.tag_bind("point_b", "<ButtonPress-1>", self.on_click)
#         self.canvas.tag_bind("point_b", "<B1-Motion>", self.on_drag)

#     def on_click(self, event):
#         self._drag_data = {"x": event.x, "y": event.y}

#     def on_drag(self, event):
#         dx = event.x - self._drag_data["x"]
#         dy = event.y - self._drag_data["y"]

#         # Move point B
#         self.canvas.move(self.point_b_id, dx, dy)
#         self._drag_data = {"x": event.x, "y": event.y}

#         # Update point B's coordinates
#         self.point_b = (self.point_b[0] + dx, self.point_b[1] + dy)

#         # Update value based on point B's coordinates
#         self.value_label.config(text=f"Point B Coordinates: ({self.point_b[0]}, {self.point_b[1]})")
#         aoa = math.tan((self.point_b[0]-self.point_a[0])/(self.point_b[1]-self.point_a[1])) * (180/math.pi)
#         # aoa = math.atan(self.point_b[1]/self.point_b[0]) * (180/math.pi)
#         self.value_label.config(text=f"AOA: {aoa}")

# if __name__ == "__main__":
#     app = PointMover()
#     app.mainloop()
import matplotlib.pyplot as plt
import math

# Function to plot 2 points and a dotted line between them
def plot_points_with_line(x1, y1, x2, y2):
    plt.figure(figsize=(60, 60))
    plt.plot([x1, x2],[y1, y2], 'x')  # Plot points
    plt.plot([x1, x2], [y1, y2], 'r--')  # Plot dotted line between points
    # plt.xlabel('Sea Level')
    # plt.ylabel('Y-axis')
    angle = math.atan((y2-y1)/(x2-x1)) * (180/math.pi)
    angle = round(angle, 1)
    time = None
    plt.title(f'AoA: {angle}\u00B0\nDistance to plane: {y2}\nHeight of plane: {x2}\nTime to landing: {time}')
    plt.grid(True)
    plt.show()

# Example points
x1, y1 = 0,0
x2, y2 = 50,20

# Call the function with example points
plot_points_with_line(x1, y1, x2, y2)
