from unityengine import *
import random
class PipeSpawner():
    def __init__(self,scene=None,gameObject=None,rigidbody=None):
        self.scene=scene
        self.gameObject=gameObject

        self.usingUnityEngine = True
        self.enabled = True
        self.gameObject = gameObject
        self.monobehaviourname = "PipeSpawner"

        self.pipeSpeed=5
        self.pipeGapSize=2

        self.pipeSpawnRate = 0.07
        self.pipeSpawnTimer=2
        self.pipeHeightRange=3

        self.GenerateBasePrefabs()
    def Start(self):
        #self.GenerateBasePrefabs()
        pass
    def EarlyUpdate(self):
        pass
    def Update(self):
        self.pipeSpawnTimer-=Time.deltaTime;
        if(self.pipeSpawnTimer<0):
            self.pipeSpawnTimer=self.pipeSpawnRate
            self.SpawnPipes()
            #print("Spawningpipes")
    def LateUpdate(self):
        pass
    def GenerateBasePrefabs(self):
        #print("GeneratedBasePrefab")
        pipeMaterial=Material(baseColour=(255,0,255))
        
        pipeTop = SpriteRenderer.CreatePrefab(scene=self.gameObject.scene,material=pipeMaterial)
        pipeTop.GetComponent("SpriteRenderer").LoadTexture("sprites/pipe-green.png")
        pipeTop.transform.position = Vector2(-500,0)
        pipeTop.transform.scale = Vector2(0.7,-5)
        pipeTop.AddComponent(Rigidbody2D(gameObject=pipeTop))

        pipeBottom = SpriteRenderer.CreatePrefab(scene=self.gameObject.scene,material=pipeMaterial)
        pipeBottom.GetComponent("SpriteRenderer").LoadTexture("sprites/pipe-green.png")
        pipeBottom.transform.position = Vector2(-500,0)
        pipeBottom.transform.scale = Vector2(0.7,5)
        pipeBottom.AddComponent(Rigidbody2D())

        self.pipes = [pipeTop,pipeBottom]
    def SpawnPipes(self):
        if(self.pipes is not None):
            yheight = random.randint(-int(self.pipeHeightRange*100),int(self.pipeHeightRange*100))/100

            top = GameObject.Instantiate(self.pipes[0],position=Vector2(5,2.5+yheight+self.pipeGapSize/2))
            rb=top.GetComponent("Rigidbody2D")
            rb.movementsystem="Inate"
            rb.velocity = Vector2(-self.pipeSpeed,0)

            btm = GameObject.Instantiate(self.pipes[1],position=Vector2(5,-2.5+yheight-self.pipeGapSize/2))
            rb=btm.GetComponent("Rigidbody2D")
            rb.movementsystem="Inate"
            rb.velocity = Vector2(-self.pipeSpeed,0)

            top.Destroy(6)
            btm.Destroy(6)
    def CreatePrefab(scene=None):
        go = GameObject()
        go.scene=scene
        spawner = PipeSpawner(scene=scene,gameObject=go)
        go.AddComponent(spawner)
        scene.AddGameObject(go)
        

