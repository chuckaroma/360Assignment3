from PIL import Image, ImageDraw
from PIL.ImageCms import DIRECTION_INPUT
from vec3 import Vec3#This is a class that was modified by Sean Groathouse
from math import  sqrt
import math

width = 612
height = 612
radius1 = 1
radius2 = 1 # The radi of each sphere
radius3 = 1
radius4 = 98.5
radius5 = 1
radius6 = 1
radius7 = 1
radius8 = 1
radius9 = 1
radius10 = 1
radius11 = 1
radius12 = 1
radius13 = 1
radius14 = 1
radius15 = 1
radius16 = 1
radius17 = 1
radius18 = 1
radius19 = 1
radius20 = 1
origin = Vec3(0, 0, 0) # The origin 
center1 = Vec3(0, -0.5, -3)
center2 = Vec3(2, -0.5, -4)
center3 = Vec3(-2, -0.5, -3)
center4 = Vec3(0, -100, 0)
center5 = Vec3(0, 2.5, -5)
center6 = Vec3(-1.2, 0.5, -3.5)
center7 = Vec3(1, 0.5, -4)
center8 = Vec3(0, -0.5, 2)
center9 = Vec3(2, 1.5, -3.5)
center10 = Vec3(-2, 1.5, -3.5)
center11 = Vec3(-1.5, 2.5, -5)
center12 = Vec3(1.5, 2.5, -5)
center13 = Vec3(-3.5, 3, -4.5)
center14 = Vec3(-3.5, 1, -4.5)
center15 = Vec3(3.5, 1, -4.5)
center16 = Vec3(3.5, 3, -4.5)
center17 = Vec3(0, 3.5, -5)
center18 = Vec3(3.5, 0.0 ,-3.5)
center19 = Vec3(-1.5, 3, -4.5)
center20 = Vec3(1.5, 3, -4.5)
color1 = Vec3(1.0, 0.5, 0.5) #Medium Red
color2 = Vec3(0.5, 1.0, 0.5) #Medium Green
color3 = Vec3(0.5, 0.5, 1.0) # Meduim BlueThe colors for each circle
color4 = Vec3(1.0, 1.0, 1.0) #White
color5 = Vec3(1.0, 0.5, 0.0) #Orange
color6 = Vec3(1.0, 1.0, 0.0) #Yellow
color7 = Vec3(1.0, 0.0, 1.0) #purple
color8 = Vec3(1.0, 0.5, 0.5) #Medium Red
color9 = Vec3(0.0, 1.0, 1.0) #Aqua
color10 = Vec3(0.7, 0.6, 0.0) #Gold
color11 = Vec3(0.7, 0.7, 0.7) #Silver
color12 = Vec3(1.0, 0.4, 0.6) #Pink
color13 = Vec3(0.0, 0.0, 1.0) #Pure Blue
color14 = Vec3(0.4, 1.0, 0.4) #Light Green
color15 = Vec3(1.0, 0.0, 0.0) #Pure Red
color16 = Vec3(1.0, 1.0, 0.2) #light yellow
color17 = Vec3(0.0, 1.0, 0.0) #pure green
color18 = Vec3(0.5, 0.0, 1.0) # violet
color19 = Vec3(1.0, 0.6, 0.6)
color20 = Vec3(0.2, 0.2, 0.2)
mirror1 = True
mirror2 = False
mirror3 = False
mirror4 = False
mirror5 = False
mirror6 = False
mirror7 = False
mirror8 = False
mirror9 = False
mirror10 = False
mirror11 = False
mirror12 = False
mirror13 = False
mirror14 = False
mirror15 = False
mirror16 = False
mirror17 = False
mirror18 = False
mirror19 = False
mirror20 = False
mirrorList = [mirror1, mirror2, mirror3, mirror4, mirror5, mirror6, mirror7, mirror8, mirror9, mirror10, mirror11, mirror12, mirror13, mirror14, mirror15, mirror16, mirror17, mirror18, mirror19, mirror20]
sphereCenterList = [center1, center2, center3, center4, center5, center6, center7, center8, center9, center10, center11, center12, center13, center14, center15, center16, center17, center18, center19, center20] #Radi, centers, mirrors and colors are stored in lists
radiusList = [radius1, radius2, radius3, radius4, radius5, radius6, radius7, radius8, radius9, radius10, radius11, radius12, radius13, radius14, radius15, radius16, radius17, radius18, radius19, radius20]
colorList = [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12, color13, color14, color15, color16, color17, color18, color19, color20]
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