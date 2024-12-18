from graphic.rectangle import rectangle_area
from graphic.rectangle import rectangle_perimeter as r_perimeter

from graphic.circle import *

from graphic.threeDgraphics.cuboid import surface_area as s_area , volume as cubicvolume
from graphic.threeDgraphics.sphere import surface_area,volume

l=int(input("enter length of rectangle:"))
b=int(input("enter breadth of reactangle:"))
print("\t area of rectangle:",rectangle_area(l,b))
print("\t perimeter of rectangle:",r_perimeter(l,b))

r=int(input("\n enter radius of circle:"))
print("area of circle:",circle_a(r))
print("\t perimeter of circle:",circle_p(r))

cub_l=int(input("\nenter length of cuboid:"))
cub_b=int(input("enter breadth of cuboid:"))
cub_h=int(input("enter height of cuboid:"))
print("\t surface area of cube:",s_area(cub_l,cub_b,cub_h))
print("\t volume of cube:",cubicvolume(cub_l,cub_b,cub_h))

s_radius=int(input("enter radius os sphere:"))
print(f"\t surface area of cube:{surface_area(s_radius):.2f}")
print(f"\t volume of cube:{volume(s_radius):.2f}")
