from PIL import Image, ImageDraw
from PIL.ImageCms import DIRECTION_INPUT
from vec3 import Vec3#This is a class that was modified by Sean Groathouse
from math import  sqrt
import math

width = 256
height = 256
radius1 = 1
radius2 = 1
radius3 = 1
radius4 = 98.5
radius5 = 1
radius6 = 1
radius7 = 1
origin = Vec3(0, 0, 0)
center1 = Vec3(0, -0.5, -3)
center2 = Vec3(2, -0.5, -4)
center3 = Vec3(-2, -0.5, -3)
center4 = Vec3(0, -100, 0)
center5 = Vec3(0, 2.5, -4)
center6 = Vec3(-1, 0.7, -3)
center7 = Vec3(1, 0.7, -4)
color1 = Vec3(1.0, 0.5, 0.5)
color2 = Vec3(0.5, 1.0, 0.5)
color3 = Vec3(0.5, 0.5, 1.0)
color4 = Vec3(1.0, 1.0, 1.0)
color5 = Vec3(1.0, 0.5, 0.0)
color6 = Vec3(1.0, 1.0, 0.5)
color7 = Vec3(1.0, 0.0, 1.0)
mirror1 = True
mirror2 = False
mirror3 = False
mirror4 = False
mirror5 = False
mirror6 = False
mirror7 = False
mirrorList = [mirror1, mirror2, mirror3, mirror4, mirror5, mirror6, mirror7]
sphereCenterList = [center1, center2, center3, center4, center5, center6, center7]
radiusList = [radius1, radius2, radius3, radius4, radius5, radius6, radius7]
colorList = [color1, color2, color3, color4, color5, color6, color7]
sphere1 = Image.new('RGB', (width, height), 'white')
sphere1.save('6spheres.jpg')

def hitSphereList(origin, direction, sphereCenterList, sphereRadiList):
    for i in range(len(sphereCenterList)): 
        record = hitsphere(origin, direction, sphereCenterList[i], sphereRadiList[i])
        if record[0]:
            return True, sphereCenterList[i], colorList[i], origin, direction, sphereRadiList[i], record[2], record[1]
    return False, sphereCenterList[0], colorList[0], origin, direction, sphereRadiList[i], record[2], record[1]

def hitsphere(origin, direction, center, radius):
    oc = origin - center
    discriminant =  math.pow(direction.dot(oc), 2.0) - direction.dot(direction)*(oc.dot(oc) - radius * radius)
    if discriminant < 0.0001:
        return False, oc, oc
    else:
        t = (-1.0 * direction.dot(origin - center) - math.sqrt(discriminant))/(direction.dot(direction))
        if t < 0:
            return False, oc, oc
    
        pt = origin + t * direction
        normal = pt - center
        normal2 = normal.normalize()
        return True, pt, normal2

for i in range(width):
    for j in range(height):
        x = ((-1 + (2*(i/(width - 1.0)))))
        y = ((1 - (2*(j/(height - 1.0))))) 
        z = -1.0 
        vector = Vec3(x, y, z)
        draw = ImageDraw.Draw(sphere1, 'RGB')
        currentSphere = hitSphereList(origin, vector, sphereCenterList, radiusList)
        if currentSphere[0]:
            color = currentSphere[2]
            shadow = 1.0
            if hitSphereList(currentSphere[7], Vec3(0.0,1.0,0.0), sphereCenterList, radiusList)[0]:
                shadow = 0.0
            if mirror1:
                icolor = (int(color[0] * currentSphere[6][1]* shadow * 255), int(color[1] * shadow *currentSphere[6][1]*255), int(color[2] * shadow * currentSphere[6][1]*255)) 
        else:
            color = (0, 0.5*(1+vector[1]), 0.5)
            icolor = (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
            print color
        sphere1.putpixel((i,j) , icolor)
       
        
    
sphere1.save('6spheres.jpg')