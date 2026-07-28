from unityengine import *
import time,math,random,pygame


#Scene Setup
scene = Scene()
time = Time()
camera = Camera.CreatePrefab(scene = scene)



Red = Material(baseColour = (255,128,128))
Blue = Material(baseColour=(128,128,255))
Green = Material(baseColour=(128,255,128))

square = SpriteRenderer.CreatePrefab(scene=scene,material=Red)
movingsquare = SpriteRenderer.CreatePrefab(scene=scene,material=Blue)
circlesquare = SpriteRenderer.CreatePrefab(scene=scene,material=Green)

square.transform.scale=Vector2(0.2,0.2)
movingsquare.transform.scale=Vector2(1,1)
circlesquare.transform.scale=Vector2(0.5,0.5)


#moving data
xpos = 0
ypos = 0
xdir = 1
ydir = 1
degrees=0
ddir = 1


while True:
    #update position
    camera.transform.position = Vector2(xpos,0)
    movingsquare.transform.position = Vector2(2,ypos)
    circlesquare.transform.position = Vector2(2*math.cos(degrees),2*math.sin(degrees))


    scene.RunMonobehaviour()


    #update directions
    xpos+=0.02*xdir
    ypos+=0.01*ydir
    if(abs(xpos)>2):
        xdir *=-1
        xpos+=0.1*xdir
    if(abs(ypos)>5): 
        ydir *=-1
        ypos+=0.1*ydir

    degrees+=ddir * 3.14159/180

    if(random.randint(1,100)==67):
        ddir*=-1

    time.Tick()


