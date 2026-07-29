from unityengine import *
class BirdCharacter():
    
    def __init__(self,gameObject = None):
        self.usingUnityEngine = True
        self.enabled = True
        self.scene = None
        self.gameObject = gameObject
        self.monobehaviourname="BirdCharacter"


        self.birdJumpVelocity = 3
        self.birdGravityScale = 0.75
        self.birdDeathHeight = -1.5

        if(gameObject==None):
            print("[ERROR] BirdCharacter requires gameobject defined already")
            exit()

        self.scene = self.gameObject.scene
        self.rb = self.gameObject.AddComponent(Rigidbody2D())
        self.sprite = self.gameObject.AddComponent(SpriteRenderer())
        self.sprite.scene = self.scene
        self.scene.AddGameObject(self.gameObject)
        #self.Start()
        
    def Start(self): #Create your variables here
        self.rb.gravity *= self.birdGravityScale
        self.sprite.material = Material((255,0,255))


        self.gameObject.transform.scale = Vector2(1,1)
        self.gameObject.transform.position = Vector2(2,0)

    def Jump(self):
        self.rb.velocity = Vector2(0,self.birdJumpVelocity)
    def Update(self): #Runs every frame
        if(self.gameObject.transform.position.y<self.birdDeathHeight):
            self.gameObject.transform.position.y = 0
            self.rb.velocity = Vector2(0,0)
        print(self.rb.velocity.ToString())
        print(self.gameObject.transform.position.ToString())
        self.gameObject.transform.position = Vector2(0,0)
    def LateUpdate(self):
        pass
    def EarlyUpdate(self):
        pass

        