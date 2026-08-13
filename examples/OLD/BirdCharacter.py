from unityengine import *
from ParticleSystem import *

class BirdCharacter():
    def __init__(self,gameObject=None,rigidbody=None):
        self.usingUnityEngine = True
        self.enabled = True
        self.gameObject = gameObject
        self.monobehaviourname = "BirdCharacter"
        self.rb=rigidbody
        self.jumpParticle=None

        self.birdJumpVelocity=3
        self.birdDeathHeight=-6
        self.swapflag=True
        self.input = Input()
    def Jump(self):
        self.rb.velocity = Vector2(0,self.birdJumpVelocity)
        if(self.jumpParticle!=None):
            self.jumpParticle.Play()
    def Start(self):
        pass
    def Die(self):
        pass
    def Update(self): #Runs every frame
        if(self.gameObject.transform.position.y<self.birdDeathHeight):
            self.gameObject.transform.position.y = 0
            self.rb.velocity = Vector2(0,0)
            self.swapflag=True
        #inputmap = self.input.GetDown()
        if(self.input.storedmap["up"]):
            self.Jump()
    def EarlyUpdate(self):
        pass
    def LateUpdate(self):
        pass

        
    def CreatePrefab(scene=None):



        
        
        go = SpriteRenderer.CreatePrefab(scene=scene,material = Material((255,255,0)))
        ps=ParticleSystem(scene=scene,gameObject=go,material=Material(baseColour=(255,255,0)))
        go.GetComponent("SpriteRenderer").LoadTexture("sprites/yellowbird-upflap.png")
        go.transform.position = Vector2(-2,0)
        go.transform.scale = Vector2(0.4,0.4)
        
        rb = go.AddComponent(Rigidbody2D())
        bird = go.AddComponent(BirdCharacter(gameObject=go,rigidbody=rb))
       
        go.AddComponent(ps)
        bird.jumpParticle = ps
        return go
