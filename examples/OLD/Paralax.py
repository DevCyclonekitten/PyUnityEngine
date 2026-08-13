from unityengine import *
import random
class Paralax():
    def __init__(self,t1,t2,gameObject=None,scene=None):
        self.transform1=t1
        self.transform2=t2

        self.usingUnityEngine = True
        self.enabled = True
        self.monobehaviourname = "ParticleSystem"
        self.gameObject=gameObject
        self.scene=scene
        self.movementScale = -0.3
        self.time = 0

        self.width = 8
    def Update(self):
        self.time+=Time.deltaTime
        self.ApplyParalax()
        #print("paralax')")
    def Start(self):
        pass
    def LateUpdate(self):
        pass
    def EarlyUpdate(self):
        pass
    def ApplyParalax(self):
        pos = self.time * self.movementScale * self.width
        #print(pos)
        pos = (pos % self.width)
        self.transform1.transform.position = Vector2(pos,0)
        self.transform2.transform.position = Vector2(pos-self.width,0)
    
    def CreatePrefab(self,t1,t2):
        pass
