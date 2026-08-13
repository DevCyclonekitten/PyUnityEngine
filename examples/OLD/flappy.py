#required namespaces
from unityengine import *
import time,math,random,pygame
# user defined namespaces
from BirdCharacter import BirdCharacter
from PipeSpawner import PipeSpawner
from Paralax import Paralax
# Global objects
time = Time()
userinput = Input()

menuScene = Scene()
menuCamera = Camera.CreatePrefab(scene=menuScene)

gameScene = Scene()
gameCamera = Camera.CreatePrefab(scene=gameScene)

#Game Objects

bg1 = SpriteRenderer.CreatePrefab(scene=gameScene)
bg1.GetComponent("SpriteRenderer").LoadTexture("sprites/background-day.png")
bg1.transform.scale = Vector2(8,8)

bg2 = SpriteRenderer.CreatePrefab(scene=gameScene)
bg2.GetComponent("SpriteRenderer").LoadTexture("sprites/background-day.png")
bg2.transform.scale = Vector2(8,8)

p = GameObject(scene=gameScene)
paralax = Paralax(bg1,bg2,gameObject=p,scene=gameScene)
p.AddComponent(paralax)
paralax.movementScale=-0.2

bird = BirdCharacter.CreatePrefab(scene=gameScene)


birdscript = bird.GetComponent("BirdCharacter")
pipes = PipeSpawner.CreatePrefab(scene=gameScene)




# Menu
menubox = SpriteRenderer.CreatePrefab(scene=menuScene,material=Material((255,0,255)))
menubox.GetComponent("SpriteRenderer").LoadTexture("sprites/gameover.png")
menubox.transform.scale=Vector2(3,1.5)


currentScene = gameScene
otherScene = menuScene
while True:
    birdscript.input.GetDown()

    if(birdscript.input.storedmap["exit"] or birdscript.swapflag):
        cs = otherScene
        otherScene=currentScene
        currentScene=cs
        birdscript.swapflag=False
        birdscript.input.storedmap["exit"]=False

    currentScene.RunMonobehaviour()
    time.Tick()