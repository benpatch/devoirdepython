__author__ = 'tchilabalo'

from numbers import Number
from numpy import*

def parallelogram_area(length,width):
    """
    calculating the area of a parallelogram
    @length and width must have the same units
    @return: the area(unit^2 from length)
    """
    return length*width
print("parallelogram area is",parallelogram_area(5,9))

def circle_perimeter(diameter):
    """
    calculating the perimeter of a circle
    @param diameter:
    @return: the perimeter(same unit as diameter)
    """
    return diameter*pi
print("circle perimeter is",circle_perimeter(15))

def cube_volume(side):
    """
    calculating the volume of a cube
    @param side:
    @return: the volume(unit^3 from side)
    """
    return side**3
print("volume of a cube is",cube_volume(5))

def area_disc(radius):
    """
    calculating the area of a disc
    @param radius:
    @return: the area(unit^2 from radius)
    """
    return radius*radius*pi
print("area of a disc is",area_disc(8))


def cylinder_volume(radius,length):
    """
    calculating cylinder volume
    @radius and length must have the same units
    @return:the volume(unit^3 from radius)
    """
    return radius*radius*pi*length
print("a cylinder volume is",cylinder_volume(2,5))

def area_square(side):
    """
    calculating the area of a square
    @param side:
    @return: the area(unit^2 from side)
    """
    return side*side
print("area of a square is",area_square(5))

def sphere_volume(radius):
    """
    calculating sphere volume
    @return:the volume(unit^3 from radius)
    """
    return 4*radius*radius*radius*pi/3
print("a sphere volume is",sphere_volume(1))

def pyramid_volume(base_surface,heigth):
    """
    calculating pyramid volume
    @base surface unit is unit^2 from heigth
    @return:the volume(unit^3 from heigth)
    """
    return base_surface*heigth/3
print("a pyramid volume is",pyramid_volume(15,5))

def cone_area(radius):
    """
    calculating cone area
    @return:the area(unit^2 from radius)
    """
    return 2*pi*radius*radius
print("a cone area is",cone_area(2))

def rectangle_perimeter(width,length):
    """
    calculating rectangle perimeter
    @width and length must have the same units
    @return:the perimeter(same unit as width)
    """
    return 2*(width*length)
print("a cylinder volume is",rectangle_perimeter(2,5))



