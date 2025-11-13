## 📄 File: `cli_gui.py`

Description: 
- provides distance, degrees, direction, and quadrant of a target at `[X, Y]`

### 🔹Functions

- `calculate_endpoint(angle_degrees, distance)`
- `get_nsew(degrees)`
- `degrees_calculate(p1, p2)`
- `rise_run(p1, p2)`
- `distance(p1, p2)`
- `quadrant(point)`

---

## 📄 File: `main.py`

Description: 
- takes 2 points of `[X, Y, Z]` and calculates distance between them (simply just a file that imports classes)


---

## 📄 File: `random_coordinates.py`

Description: 
- creates random 2D or 3D coordinates for use in calculations
- error in import of `from coords import Coords`

### 🏷️Classes

- 🏷️**Class:** `Random_Coordinates`
  - ⚙️ Methods:
    - `get_2d_whole_numbers(self)`
    - `get_2d(self)`
    - `get_3d(self)`
    - `get_3d_whole_numbers(self)`
    - `get_3d_whole_numbers_range(self, x_low, x_hig, y_low, y_high, z_low, z_high)`


---

## 📄 File: `Coordinates\3d_space.py`

Description: 
- will provide a 3D GUI chart of target, origin, direction

### 🔹Functions

- `degrees_calculate(p1, p2)`
- `get_nsew(degrees)`
- `plot_arrow(ax, x, y, z, color)`
- `get_heading_points(heading_degrees)`

---

## 📄 File: `Coordinates\coordinate_tests.py`

Description: 
- tests for the Coordinates and Distance Classes (the latter has an import error)

### 🏷️Classes

- 🏷️**Class:** `TestCoordinateComputations`
  - ⚙️ Methods:
    - `test_dimension_1(self)`
    - `test_dimension_2(self)`
    - `test_dimension_3(self)`
    - `test_dimension_4(self)`
    - `test_dimension_5(self)`
    - `test_range_checks_1(self)`
    - `test_range_checks_2(self)`
    - `test_range_checks_3(self)`
    - `test_range_checks_4(self)`
    - `test_range_checks_5(self)`
    - `test_range_checks_6(self)`
    - `test_haversine_dist_two_points_1(self)`
    - `test_haversine_dist_two_points_2(self)`
    - `test_haversine_dist_3_points(self)`
    - `test_haversine_dist_1_point(self)`
    - `test_haversine_dist_0_point(self)`
    - `test_distance_2d_3_equals_0(self)`
    - `test_distance_2d_4_greater_0(self)`
    - `test_rise_over_run_2d_1(self)`
    - `test_rise_over_run_2d_2(self)`


---

## 📄 File: `Coordinates\coords.py`

Description: 
- class for Coordinates objects

### 🏷️Classes

- 🏷️**Class:** `Coords`
  - ⚙️ Methods:
    - `__init__(self, x, y, z, dimension)`
    - `__str__(self)`
    - `values(self)`
    - `rounded_values(self)`
    - `test_params(point)`


---

## 📄 File: `Physics\distances.py`

Description: 
- takes in `Coords` objects, calculates various distance dimension values
- imports `coords` and `units`, the former has an error 

### 🏷️Classes

- 🏷️**Class:** `Distances`
  - ⚙️ Methods:
    - `rise_run(coord1, coord2, coord3)`
    - `rise(coord1, coord2, coord3)`
    - `run(coord1, coord2, coord3)`
    - `distance_2d(coord1, coord2)`
    - `haversine_distance(coord1, coord2)`
    - `euclidean_distance(coord1, coord2)`


---

## 📄 File: `Physics\gps.py`

Description: 
- intended to be a class that interacts with a GPS, displays realtime data

### 🏷️Classes

- 🏷️**Class:** `GPS`
  - ⚙️ Methods:
    - `__init__(self, name, x, y, z, dimension)`
    - `__str__(self)`
    - `values(self)`


---

## 📄 File: `Physics\gui_test.py`

Description: 
- a 2D cartesian coordinates plane showing distance and direction to a target from an origin represented as `(0, 0)`

### 🔹Functions

- `plot_xy_plane(x_list, y_list, arrow_x, arrow_y)`
- `plot_point(x, y, direction_x, direction_y)`
- `calculate_endpoint(angle_degrees, distance)`
- `get_nsew(degrees)`
- `degrees_calculate(p1, p2)`
- `rise_run(p1, p2)`
- `distance(p1, p2)`
- `quadrant(point)`

---

## 📄 File: `Physics\physics_methods.py`

Description: 
- static methods for calculating various Movements related to an object 

### 🏷️Classes

- 🏷️**Class:** `Movement`
  - ⚙️ Methods:
    - `time_to_x(distance, speed, unit_speed, unit_time)`
    - `distance(value1, value2)`
    - `speed(distance, timeInitial, timeFinal)`
    - `velocity(posInitial, posFinal, timeInitial, timeFinal)`
    - `acceleration(velocityInitial, velocityFinal, timeInitial, timeFinal)`
    - `get_heading_points(heading_degrees)`


---

## 📄 File: `Physics\physics_tests.py`

Description: 
- testing of Classes within `Physics\`

### 🏷️Classes

- 🏷️**Class:** `TestCoordinateComputations`
  - ⚙️ Methods:
    - `test_speed_1(self)`
    - `test_speed_2(self)`
    - `test_speed_3(self)`
    - `test_speed_4(self)`
    - `test_speed_5(self)`
    - `test_speed_6(self)`
    - `test_velocity_1(self)`
    - `test_velocity_2(self)`
    - `test_velocity_3(self)`
    - `test_velocity_4(self)`
    - `test_velocity_5(self)`
    - `test_acceleration_1(self)`
    - `test_acceleration_2(self)`
    - `test_acceleration_3(self)`
    - `test_acceleration_4(self)`
    - `test_acceleration_5(self)`
    - `test_time_1(self)`
    - `test_time_2(self)`
    - `test_time_3(self)`
    - `test_time_4(self)`
    - `test_time_5(self)`
    - `test_time_6(self)`
    - `test_time_7(self)`
    - `test_units_1(self)`
    - `test_units_2(self)`
    - `test_units_3(self)`


---

## 📄 File: `Physics\position.py`

Description: 
- assignment of values for position, speed, acceleration, and bearing

### 🏷️Classes

- 🏷️**Class:** `Position`
  - ⚙️ Methods:
    - `__init__(self, timeI, time, speedI, speedF, accelX, accelY, accelZ, bearingI, bearingF)`
    - `__str__(self)`
    - `values(self)`


---

## 📄 File: `Physics\triangulate.py`

Description: 
- triangulation and fetching of a given city's coordinates through Google API
- API key needed 

### 🏷️Classes

- 🏷️**Class:** `Triangulate`
  - ⚙️ Methods:
    - `find_center_coordinates(self, coord1, coord2, coord3)`
    - `get_city_coordinates(self, city, api_key)`


---

## 📄 File: `Physics\triangulate_test.py`

Description: 
- testing of `Triangulation` class


---

## 📄 File: `Physics\units.py`

Description: TODO

### 🏷️Classes

- 🏷️**Class:** `Units`
  - ⚙️ Methods:
    - `__init__(self, measure_distance, measure_time)`
    - `__str__(self)`
    - `display(self)`


---

## 📄 File: `Physics\Vectoring\test_vectoring.py`

Description: TODO


---

## 📄 File: `Physics\Vectoring\threeVectoring.py`

Description: TODO

### 🏷️Classes

- 🏷️**Class:** `Vectoring`
  - ⚙️ Methods:
    - `__init__(self)`
    - `degrees_calculate(self, p1, p2, decimal)`
    - `get_nsew(self, degrees)`
    - `elevation_angle(self, p1, p2, decimal)`
    - `plot_vector_to_target_3d(self, p1, p2)`


---

## 📄 File: `Physics\Vectoring\threeVectoringMovingTarget.py`

Description: TODO

### 🏷️Classes

- 🏷️**Class:** `Radar2DSmooth`
  - ⚙️ Methods:
    - `__init__(self, source, waypoints, loop, frame_delay)`
    - `create_smooth_path(self, waypoints, steps)`
    - `plot_radar_background(self)`
    - `degrees_heading(self, src, tgt)`
    - `animate(self)`


---

## 📄 File: `Physics\Vectoring\threeVectoringMovingTargetCircle.py`

Description: TODO

### 🏷️Classes

- 🏷️**Class:** `Radar2D`
  - ⚙️ Methods:
    - `__init__(self, source, target)`
    - `plot_radar_background(self)`
    - `degrees_heading(self, src, tgt)`
    - `update_plot(self)`
    - `animate(self)`


---

## 📄 File: `Physics\Vectoring\twoVectoring.py`

Description: TODO

### 🏷️Classes

- 🏷️**Class:** `Vectoring`
  - ⚙️ Methods:
    - `__init__(self)`
    - `degrees_calculate(self, p1, p2, decimal)`
    - `get_nsew(self, degrees)`
    - `get_heading_points(self, heading_degrees)`
    - `plot_vector_to_target(self, p1, p2)`


---

## 📄 File: `review and recycle\Aoa\a0a.py`

Description: TODO

### 🔹Functions

- `plot_points_with_line(x1, y1, x2, y2)`

---

## 📄 File: `review and recycle\Aoa\aoa_gui.py`

Description: TODO

### 🏷️Classes

- 🏷️**Class:** `PointMover`
  - ⚙️ Methods:
    - `__init__(self)`
    - `on_click(self, event)`
    - `on_drag(self, event)`


---

## 📄 File: `review and recycle\Aoa\aoa_test.py`

Description: TODO

### 🔹Functions

- `get_plane_coordinates()`

---

## 📄 File: `review and recycle\automation\auto_make_tests.py`

Description: TODO

### 🔹Functions

- `get_thing(angle_degrees)`
- `get_nsew(degrees)`

---

## 📄 File: `review and recycle\automation\auto_open_maps.py`

Description: TODO


---

