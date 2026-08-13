from unityengine import *
import random
import math
class Card():
    def __init__(self,scene=None,gameObject=None,rigidbody=None):
        self.scene=scene
        self.gameObject=gameObject

        self.usingUnityEngine = True
        self.enabled = True
        self.gameObject = gameObject
        self.monobehaviourname = "Card"

        self.targetState = 1
        self.isShown = False
        self.isShownValue = -1

        self.textureBacking = None
        self.textureFront = None
        self.sprite = None

        self.time = 0
        self.sizeX = 3
        self.sizeY = 4


    def GetSpeed(self):
        return (1)* Time.deltaTime
    def Start(self):
        self.angle=0
        self.gameObject.transform.scale.y = self.sizeY
    def EarlyUpdate(self):
        pass
    def LateUpdate(self):
        pass
    def SetState(self,state):
        self.targetState=state
        print(f"Set State: {state}")
    def UpdateSprite(self):
        if(self.targetState==1):
            self.sprite.LoadTexture(self.textureBacking)
        else:
            self.sprite.LoadTexture(self.textureFront)
    def Update(self):
        

        if(self.targetState==1):
            self.time+=Time.deltaTime
            if(self.time>3.141):
                self.time=3.141
        else:
            self.time-=Time.deltaTime
            if(self.time<0):
                self.time=0
        self.angle = math.cos(self.time)
        self.gameObject.transform.scale.x = abs(self.angle)*3#.self.sizeX * self.isShownValue  
        
        if(self.angle>0):
             self.sprite.LoadTexture(self.textureBacking)
        else:
            self.sprite.LoadTexture(self.textureFront)
    def CreatePrefab(scene=None):
        go = SpriteRenderer.CreatePrefab(scene=scene,material = Material((255,255,0)))
        
        card = Card()

        go.AddComponent(card)
        card.textureFront = "sprites/background-day.png"
        card.textureBacking = "sprites/background-night.png"

        card.sprite = go.GetComponent("SpriteRenderer")
        card.sprite.LoadTexture(card.textureFront)

        go.scene=scene

        return go