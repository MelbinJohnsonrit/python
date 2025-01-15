from graphic.circle import*
from graphic.rectangle import area as r_area, perimeter as r_perimeter
from graphic.dgraphic.cuboid import area as c_area,perimeter as c_perimeter
from graphic.dgraphic.sphere import  area as s_area,perimeter as s_perimeter

r=4
print("circle area",area(r))
print("circle perimeter",perimeter(r))

l=2
b=3
print("rectangle area",r_area(l,b))
print("rectangle perimeter",r_perimeter(l,b))

l,w,h=2,3,4
print("cuboid area",c_area(l,w,h))
print("cuboid perimeter",c_perimeter(l,w,h))

r=4
print("sphere area",s_area(r))
print("sphere perimeter",s_perimeter(r))

