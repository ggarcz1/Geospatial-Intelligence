import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

# Lists to store X and Y coordinates of points
x_coords = []
y_coords = []


def plot_xy_plane(x_list, y_list, arrow_x, arrow_y):
    fig = Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color('gray')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.grid(True, which='both')
    ax.plot(x_list, y_list, marker='o', markersize=10, color='red')
    ax.annotate('', xy=(arrow_x, arrow_y), xytext=(0, 0),
                arrowprops=dict(facecolor='blue', shrink=0.05, width=1, headwidth=8))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# def plot_point():
def plot_point(x: float, y: float, direction_x: float, direction_y: float):
    # x = float(entry_x.get())
    # y = float(entry_y.get())
    # direction_x = float(entry_direction_x.get())
    # direction_y = float(entry_direction_y.get())
    x_coords.append(x)
    y_coords.append(y)
    # plot_xy_plane(x, y, direction_x, direction_y)
    x_coords.append(-55)
    y_coords.append(33)
    plot_xy_plane(x, y, direction_x, direction_y)


# calculate the endpoint based on angle and distance given
def calculate_endpoint(angle_degrees: float, distance):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate endpoint coordinates
    end_point_x = 0 + distance * math.cos(angle_radians)
    end_point_y = 0 + distance * math.sin(angle_radians)

    return [end_point_x, end_point_y]


def degrees_calculate(p1: list, p2: list) -> float:
    return rise_run(p1, p2) * 360


# to calculate the distance of a vector, aka to a "target", point or object
def rise_run(p1: list, p2: list) -> float:
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def distance(p1: list, p2: list) -> float:
    return math.sqrt(
        math.pow(p1[0] - p2[0], 2) +
        math.pow(p1[1] - p2[1], 2))


def quadrant(point):
    # I
    # x+ y+
    if point[0] > 0 and point[1] > 0:
        return 1
    # II
    # x- y+
    elif point[0] < 0 and point[1] > 0:
        return 2
    # III
    # x- y-
    elif point[0] < 0 and point[1] < 0:
        return 3
    # IV
    # x+ y-
    else:
        return 4


root = tk.Tk()
root.title("XY Plane GUI")

# # inputs on the gui
# label_x = tk.Label(root, text="X Coordinate:")
# label_x.pack()
# entry_x = tk.Entry(root)
# entry_x.pack()
#
# label_y = tk.Label(root, text="Y Coordinate:")
# label_y.pack()
# entry_y = tk.Entry(root)
# entry_y.pack()
#
# label_direction_x = tk.Label(root, text="Direction X Coordinate:")
# label_direction_x.pack()
# entry_direction_x = tk.Entry(root)
# entry_direction_x.pack()
#
# label_direction_y = tk.Label(root, text="Direction Y Coordinate:")
# label_direction_y.pack()
# entry_direction_y = tk.Entry(root)
# entry_direction_y.pack()

# plot_button = tk.Button(root, text="Plot Point", command=plot_point)
# plot_button.pack()

# declare direction
vector_degrees = 40

if type(vector_degrees) is not float and \
        type(vector_degrees) is not int \
        or vector_degrees < 0 \
        or vector_degrees > 360:
    print(f'Error. {vector_degrees} is invalid.')

# revisit what this does exactly
# point = calculate_endpoint(vector_degrees, distance([0, 0], target))

origin = [0, 0]
target = [-85, -33]

plot_point(0, 0, target[0], target[1])
dist = distance([0, 0], target)

distance_button = tk.Button(root,
                            text=f"Distance: {round(dist, 2)} miles")
distance_button.pack()

degrees = tk.Button(root,
                    text=f"Degrees: {round(degrees_calculate(origin, target), 2)}\u00b0")
degrees.pack()

quad = tk.Button(root,
                 text=f"Quadrant: {quadrant(target)}")
quad.pack()

# # input for destination point/vehicle
# x_dest = 54
# y_dest = -33
# # plot_point(x_dest, y_dest, point[0], point[1])
root.mainloop()
