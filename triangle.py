#620097038
import sys
from math import cos,sqrt,radians
import random

#Checks if the sides within a list forms a triangle
def isTriangle(side):
  if (side[0] + side[1]) <= side[2] or (side[0] + side[2]) <= side[1] or (side[1] + side[2]) <= side[0]:
    return False
  return True

def equal(a,b):
  e = 1*10**(-2)
  # print(a-b)
  return abs(a-b) <= e

#function to check if Triangle is equilateral
def equi(tri,a):
  if ((tri[0] == tri[1] == tri[2]) and a == 60) or equal(tri[0], tri[1] and equal(tri[1], tri[2]) and a == 60):
    return True
  return False

#function to check if Triangle is isosceles 
def isos(tri):
  if (tri[0] == tri[1] != tri[2] or tri[1] == tri[2] != tri[0] or tri[0] == tri[2] != tri[1]):
    return True
  return False

#To determine the third side of an triangle and which type it is 
def determine_triangle(a, b, ang):
  if(a < 0 or b < 0 or ang < 0 or ang >= 180):
    return "Triangle is Invalid"

  c = sqrt(a**2 + b**2 - 2*a*b*cos(radians(ang)))
  c = round(c)
  # print(a, b, c)
  tri = [a, b, c]
  # print(tri)

  if not isTriangle(tri):
    return "Triangle is Invalid"
  if equi(tri, ang):
    return "Equilateral Triangle"
  elif isos(tri):
    return "Isosceles Triangle"
  else:
    return "Neither of the two"
        
if __name__ == "__main__":
  print(determine_triangle(32,12,36))
