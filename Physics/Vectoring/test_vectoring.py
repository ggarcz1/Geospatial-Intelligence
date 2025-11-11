import sys
from pathlib import Path
from threeVectoring import Vectoring
random_coords_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(random_coords_dir))
from random_coordinates import Random_Coordinates

# degrees = v.degrees_calculate(p1=p1, p2=p2, decimal=0)
# heading = v.get_nsew(degrees=degrees)

v = Vectoring()
rand = Random_Coordinates()
# get random coordinates for real world implications
points1 = rand.get_3d_whole_numbers()
points2 = rand.get_3d_whole_numbers()
print(points1)
print(points2)
p1 = [points1.x, points1.y, points1.z]
p2 = [points2.x, points2.y, points2.z]

# p1 = [0, 0, 0]
# p2 = [10, 5, 8]  # 3D point with Z
degrees, heading = v.plot_vector_to_target_3d(p1, p2)
print(f"Degrees: {degrees}\nHeading: {heading}")