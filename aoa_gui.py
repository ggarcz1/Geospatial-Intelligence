import tkinter as tk
import math

class PointMover(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Point Mover")
        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack()

        # Initial positions for point A and point B
        self.point_a = (50, 350)  # Fixed position for Point A
        self.point_b = (300, 300)  # Initial position for Point B

        # Draw points
        self.canvas.create_oval(self.point_a[0] - 5, self.point_a[1] - 5,
                                self.point_a[0] + 5, self.point_a[1] + 5,
                                fill="red", tags="point_a")
        self.point_b_id = self.canvas.create_oval(self.point_b[0] - 5, self.point_b[1] - 5,
                                                  self.point_b[0] + 5, self.point_b[1] + 5,
                                                  fill="blue", tags="point_b")

        # Display value
        # self.value_label = tk.Label(self, text=f"Point B Coordinates: ({self.point_b[0]}, {self.point_b[1]})")
        aoa = math.atan(self.point_b[0]/self.point_b[1])*(180/math.pi)
        self.value_label = tk.Label(self, text=f"AOA: {aoa}")

        self.value_label.pack()

        # Bind mouse events to point B
        self.canvas.tag_bind("point_b", "<ButtonPress-1>", self.on_click)
        self.canvas.tag_bind("point_b", "<B1-Motion>", self.on_drag)

    def on_click(self, event):
        self._drag_data = {"x": event.x, "y": event.y}

    def on_drag(self, event):
        dx = event.x - self._drag_data["x"]
        dy = event.y - self._drag_data["y"]

        # Move point B
        self.canvas.move(self.point_b_id, dx, dy)
        self._drag_data = {"x": event.x, "y": event.y}

        # Update point B's coordinates
        self.point_b = (self.point_b[0] + dx, self.point_b[1] + dy)

        # Update value based on point B's coordinates
        self.value_label.config(text=f"Point B Coordinates: ({self.point_b[0]}, {self.point_b[1]})")
        aoa = math.atan(self.point_b[0]/self.point_b[1])*(180/math.pi)
        self.value_label = tk.Label(self, text=f"AOA: {aoa}")

if __name__ == "__main__":
    app = PointMover()
    app.mainloop()
