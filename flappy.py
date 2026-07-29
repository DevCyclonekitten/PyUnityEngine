#required namespaces
from unityengine import *
import time,math,random,pygame


# user defined namespaces
from BirdCharacter import BirdCharacter



# global objects
time = Time()
userinput = Input()

gameScene = Scene()
gameCamera = Camera.CreatePrefab(scene=gameScene)



bird = GameObject(scene=gameScene)
birdscript = BirdCharacter(gameObject=bird)
bird.AddComponent(birdscript)









pipeMaterial = Material(baseColour=(0,255,0))
birdMaterial = Material(baseColour=(255,255,0))
backgroundMaterial = Material(baseColour=(187,252,255))
groundMaterial = Material(baseColour=(162,255,146))
particleMaterial = Material(baseColour=(255,255,255))


background = SpriteRenderer.CreatePrefab(scene=gameScene,material=backgroundMaterial)
background.transform.scale = Vector2(8,6)

ground = SpriteRenderer.CreatePrefab(scene=gameScene,material=groundMaterial)
ground.transform.scale = Vector2(8,1)
ground.transform.position = Vector2(0,-2)

pipeTop = SpriteRenderer.CreatePrefab(scene=gameScene,material=pipeMaterial)
pipeTop.transform.position = Vector2(-500,0)
pipeTop.transform.scale = Vector2(0.5,5)
pipeTop.AddComponent(Rigidbody2D())

pipeBottom = SpriteRenderer.CreatePrefab(scene=gameScene,material=pipeMaterial)
pipeBottom.transform.position = Vector2(-500,0)
pipeBottom.transform.scale = Vector2(0.5,5)
pipeBottom.AddComponent(Rigidbody2D())


#Game Settings


pipeMovementSpeed = 2
pipeGapDistance = 1.5
pipeSpawnRate = 2
pipeSpawnTimer = 2
pipeHeightRange = 1.25




def Die():
    pass
def ClonePipe():
    global pipeTop
    yheight = random.randint(-int(pipeHeightRange*10),int(pipeHeightRange*10))/10



    top = GameObject.Instantiate(pipeTop,position=Vector2(5,2.5+yheight+pipeGapDistance/2))
    rb=top.GetComponent("Rigidbody2D")
    rb.movementsystem="Inate"
    rb.velocity = Vector2(-pipeMovementSpeed,0)

    btm = GameObject.Instantiate(pipeBottom,position=Vector2(5,-2.5+yheight-pipeGapDistance/2))
    rb=btm.GetComponent("Rigidbody2D")
    rb.movementsystem="Inate"
    rb.velocity = Vector2(-pipeMovementSpeed,0)

    top.Destroy(10)
    btm.Destroy(10)

timer = 0
while True:
    
    maps = userinput.GetDown()
    if(maps["up"]==True):
        birdscript.Jump()



    pipeSpawnTimer -= Time.deltaTime
    if(pipeSpawnTimer<=0):
        pipeSpawnTimer=pipeSpawnRate
        pipeSpawnRate-=0.05
        pipeGapDistance-=0.001
        if(pipeSpawnRate<0.4):
            pipeSpawnRate=0.4
        ClonePipe()
    

    
    gameScene.RunMonobehaviour()
    time.Tick()


    