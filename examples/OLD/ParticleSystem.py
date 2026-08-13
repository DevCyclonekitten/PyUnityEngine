from unityengine import *
import random
class ParticleSystem():
    def __init__(self,scene=None,gameObject=None,material=None):
        self.usingUnityEngine = True
        self.enabled = True
        self.gameObject = gameObject
        self.monobehaviourname = "ParticleSystem"
        self.scene=scene
        self.camera=None

        self.material = material
        self.duration=1
        self.destroyTime = 0.5

        self.particleSize = 0.2
        self.particleSizeMultPerFrame=0.95
        self.particlecount = 10
        self.particles = []
    def Play(self):
        for i in range(self.particlecount):
            p = Particle(system=self)
            p.material = self.material
            p.transform.position = self.gameObject.transform.position.Clone()
            p.transform.scale.Scale(Vector2(self.particleSize,self.particleSize))
            p.destroyTime=self.destroyTime
            p.velocity = Vector2(random.randint(-50,0)/10,random.randint(-30,10)/10)
            self.particles.append(p)
    def Start(self):
        if(self.camera==None):
            if(self.scene!=None):
                self.camera=self.scene.camera
    def ApplyParticleUpdate(self,p):
        p.transform.scale.Multiply(self.particleSizeMultPerFrame)
    def Update(self):
        if(self.camera==None):
            return
        for p in self.particles:
            self.ApplyParticleUpdate(p)
            p.Update()
           
        #print("Particlelength: "+str(len(self.particles)))
    def EarlyUpdate(self):
        pass
    def LateUpdate(self):
        pass
    def Destroy(self,particle):
        self.particles.remove(particle)
    def CreatePrefab(scene=None):
        pass

class Particle():
    def __init__(self,system=None,material=None,camera=None):
        self.system = system
        self.transform = Transform()
        self.velocity = Vector2(0,0)
        self.destroyTime = -9999
        self.material = material
    def Destroy(self):
        self.system.Destroy(self)
    def Update(self):
        self.destroyTime-=Time.deltaTime
        if(self.destroyTime<0 and self.destroyTime>-9999):
            self.Destroy()

        self.transform.position.Add(self.velocity.ReturnScaled(Time.deltaTime))
        self.system.camera.RenderRect(self.transform,self.material)
 