from PIL import Image, ImageDraw
from PIL.ImageCms import DIRECTION_INPUT
from vec3 import Vec3#This is a class that was modified by Sean Groathouse
from math import  sqrt
import math
from numpy import record, square
import random
from compiler.pyassem import DONE
#to do for tuesday 1. fix random sphere, 2. move icolor down to main for loop
#This section contains Most of the variables for the program, such as the height and width of the image. 
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
sphere1 = Image.new('RGB', (width, height), 'white') #Creates a new blank image
sphere1.save('Project.jpg') #Saves the image

#A function that focuses on seeing if a point hits any of the spheres, and returns a sphere center, color, origin, direction, radius, noraml, pt, and mirror
def hitSphereList(origin, direction, sphereCenterList, sphereRadiList, mirrorList):
    for i in range(len(sphereCenterList)): 
        record = hitsphere(origin, direction, sphereCenterList[i], sphereRadiList[i], mirrorList[i])
        if record[0]:
            return True, sphereCenterList[i], colorList[i], origin, direction, sphereRadiList[i], record[2], record[1], record[3]
    return False, sphereCenterList[0], colorList[0], origin, direction, sphereRadiList[i], record[2], record[1], record[3]
#a funtion that focuses on seeing if a point hits a single sphere, and returns a true/false boolean, pt, normal, and mirror

def hitsphere(origin, direction, center, radius, mirrorList):
    oc = origin - center
    discriminant =  math.pow(direction.dot(oc), 2.0) - direction.dot(direction)*(oc.dot(oc) - radius * radius)
    if discriminant < 0:
        return False, oc, oc, mirrorList
    else:
        t = (-1.0 * direction.dot(origin - center) - math.sqrt(discriminant))/(direction.dot(direction))
        if t < 0.01:
            return False, oc, oc, mirrorList
        pt = origin + t * direction
        normal = pt - center
        normal2 = normal.normalize()
        return True, pt, normal2, mirrorList
#making random point in sphere
def sphereRandom():
    x = 2*random.random() -1
    y = 2*random.random() -1
    z = 2*random.random() -1
    while (((x*x) + (y*y) + (z*z)) > 1):
        x = 2*random.random() -1
        y = 2*random.random() -1
        z = 2*random.random() -1
    
    return Vec3(x, y, z)

    
def rayColor(rayorigin, raydirection, depth):
    #currentSphere is used to see if any of the spheres are hit and uses rayorigin, raydirection, the sphereCenterList, radiusList, and mirrorList as arguments
            currentSphere = hitSphereList(rayorigin, raydirection, sphereCenterList, radiusList, mirrorList)
            #currentSphere[0] = a boolean flag to see if any of the spheres have been hit
            #currentSphere[1] = a sphere center from the sphereCenterList
            #currentSphere[2] = a vec3 color from the color list to represent a sphere color
            #currentSphere[3] = the origin represented by a vec3 of (0.0, 0.0, 0.0)
            #currentSphere[4] = the ray direction
            #currentSphere[5] = the radius of the sphere from the sphereRadiList
            #currentSphere[6] = the normal calculated in the hitsphere function
            #currentSphere[7] = the hitpoint calculated in the hitsphere funtion
            #currentSphere[8] = a boolean flag to see if the sphere mirror is true or false from the mirror list
            #Checking to see if the currentSphere has been hit. If it has, we set the color of the sphere to a color in the colorList, and the shadow to 1.0.
            if depth > 5:
                color = Vec3(0.0, 0.0, 0.0)
            elif currentSphere[0]:
                color = currentSphere[2]
                shadow = 1.0
#                Here, we check to see if the hitSphereList funtion of the first sphere is true, and if it is, the shadow is set to 0.0, and it uses the normal 
#                from the hitSphere function, a vec3 objection that is green, 0.2 x the random function, and a center, radius, and mirror flag from their respective lists.           
                if hitSphereList(currentSphere[7], Vec3(0.0,1.0,0.0) + 0.2*sphereRandom(), sphereCenterList, radiusList, mirrorList)[0]:
                    shadow = 0.0 
#                We are checking if the mirror flag from currentSphere is true. If it is, we set color equal to the funtion rayColor and use the normal, hitpoint, and add 1 to the depth to simulate a mirror 
                if currentSphere[8]:
                    color = rayColor(currentSphere[7], currentSphere[6] + 0.2*sphereRandom(), depth + 1)
#                If the first two conditions are not satisfied, we set color equal to a Vec3 object and multiply the three integers in color by the
#                first normal in current sphere and by the shadow to get shadows on the spheres and on the ground.
                else:
                    color = currentSphere[6][1]*shadow*color
                    #This is where I am implementing the random Vec 3 and using The normal + sphere random, and wanted to know what other values to use for the Vec]
                    color += currentSphere[2]*rayColor(currentSphere[7], currentSphere[6] + sphereRandom(), depth+1)
#            If the current sphere has not been hit, we set color equal to the backgrounf color using 0.0, 0.2 multiplied by the ray direction, and 0.1
            else:
                color = Vec3(0.0, 0.5, 0.5*(1+raydirection[1]))
            #rayColor returns color, a vec3 object for later use in the main method.
            return color
        
#move icolor integer conversion to for loop
#Should I implement the equation r = d - 2(d*n)n in the hitsphere or hitshpherelist function, or in the main for loop? 
#Should I also use new variables for r, d, and n?

ns = 100
for i in range(width):
    for j in range(height):
        raycolor = Vec3(0,0,0)
        for s in range(ns):
            x = ((-1 + (2*(i/(width - 1.0)))))
            y = ((1 - (2*(j/(height - 1.0))))) 
            z = -1.0 
            vector = Vec3(x, y, z)
            draw = ImageDraw.Draw(sphere1, 'RGB')
            raycolor += rayColor(Vec3(0,0,0), vector, 0)
            #c = 1/ns
        raycolor *= (1.0/ns) 
        icolor = (int(raycolor[0] * 255), int(raycolor[1] * 255), int(raycolor[2] * 255))
        print icolor
        sphere1.putpixel((i,j) , icolor)
#computes one ray and determines what color it is, send several rays here
        
    
sphere1.save('Project.jpg')