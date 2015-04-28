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
width = 256
height = 256
radius1 = 1
radius2 = 1 # The radi of each sphere
radius3 = 1
radius4 = 98.5
origin = Vec3(0, 0, 0) # The origin 
center1 = Vec3(0, 0, -3)
center2 = Vec3(2, 0, -4)
center3 = Vec3(-2, 0, -3) # The centers of each sphere
center4 = Vec3(0, -100, 0)
color1 = Vec3(1.0, 0.5, 0.5)
color2 = Vec3(0.5, 1.0, 0.5)
color3 = Vec3(0.5, 0.5, 1.0) # The colors for each circle
color4 = Vec3(1.0, 1.0, 1.0)
mirror1 = False
mirror2 = False
mirror3 = True
mirror4 = False
mirrorList = [mirror1, mirror2, mirror3, mirror4]
sphereCenterList = [center1, center2, center3, center4] #Radi, centers, mirrors and colors are stored in lists
radiusList = [radius1, radius2, radius3, radius4]
colorList = [color1, color2, color3, color4]
sphere1 = Image.new('RGB', (width, height), 'white') #Creates a new blank image
sphere1.save('mirror.jpg') #Saves the image

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
                color = Vec3(0.0, 0.2*(1+raydirection[1]), 0.1)
            #rayColor returns color, a vec3 object for later use in the main method.
            return color
        
#move icolor integer conversion to for loop
#Should I implement the equation r = d - 2(d*n)n in the hitsphere or hitshpherelist function, or in the main for loop? 
#Should I also use new variables for r, d, and n?

ns = 1000
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
        #When 1 is divided by 10, do I want 0.1 or a whole number?
        icolor = (int(raycolor[0] * 255), int(raycolor[1] * 255), int(raycolor[2] * 255))
        #print icolor
        sphere1.putpixel((i,j) , icolor)
#computes one ray and determines what color it is, send several rays here
        
    
sphere1.save('Mirror.jpg')