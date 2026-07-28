from unityengine import *
import time,math,random,pygame

time = Time()
userinput = Input()

gameScene = Scene()
gameCamera = Camera.CreatePrefab(scene=gameScene)

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

bird = SpriteRenderer.CreatePrefab(scene=gameScene,material=birdMaterial)
birdrb = bird.AddComponent(Rigidbody2D())
bird.transform.scale = Vector2(0.35,0.35)
bird.transform.position = Vector2(-2,0)

#Game Settings
birdJumpVelocity = 3
birdGravityScale = 0.75
birdDeathHeight = -1.5

pipeMovementSpeed = 2
pipeGapDistance = 1.5
pipeSpawnRate = 2
pipeSpawnTimer = 2
pipeHeightRange = 1.25


birdrb.gravity *=birdGravityScale



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
particles = []
while True:
    
    maps = userinput.GetDown()
    if(maps["up"]==True):
        birdrb.velocity = Vector2(0,birdJumpVelocity)
        for i in range(20):
            go = GameObject.Instantiate(bird,position = bird.transform.position.Clone())
            rb = go.GetComponent("Rigidbody2D")
            rb.AddForce(Vector2(random.randint(-30,-10)/10,random.randint(-30,10)/10))
            go.transform.scale.Scale(Vector2(0.3,0.3))
            spr = go.GetComponent("SpriteRenderer")
            spr.material = particleMaterial

            go.Destroy(0.2+random.randint(3,10)/20)
            particles.append(go)
    for p in particles:
        if(p is None):
            particles.remove(p)
        else:
            p.transform.scale.Scale(Vector2(0.95,0.95))


    pipeSpawnTimer -= Time.deltaTime
    if(pipeSpawnTimer<=0):
        pipeSpawnTimer=pipeSpawnRate
        pipeSpawnRate-=0.05
        pipeGapDistance-=0.001
        if(pipeSpawnRate<0.4):
            pipeSpawnRate=0.4
        ClonePipe()
    
    
    if(bird.transform.position.y<birdDeathHeight):
        bird.transform.position.y = 0
        birdrb.velocity = Vector2(0,0)
    
    gameScene.RunMonobehaviour()
    time.Tick()


    