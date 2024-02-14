from class_type import Polygon, Triangle

obj_poligon = Polygon()
obj_triangle = Triangle()

print(type(obj_triangle) == Triangle)
print(type(obj_triangle) == Polygon)

print(isinstance(obj_poligon, Polygon))
print(isinstance(obj_triangle, Polygon))