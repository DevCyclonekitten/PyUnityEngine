from unityengine.Transform import *
from unityengine.Time import *
import copy,pygame
class GameObject():
    def __init__(self,scene=None): #Create your variables here
        #These variables are required
        self.usingUnityEngine = True
        self.enabled = True
        self.monobehaviours = {}
        self.monobehaviourname = "GameObject"
        self.transform = Transform()
        self.scene = scene
        if(scene!=None):
            scene.AddGameObject(self)
        self.destroyTime = -9999
    def Destroy(self,time=0):
        if(time==0):
            for item in self.scene.sceneGameObjects:
                if(item==self):
                    self.scene.sceneGameObjects.remove(item)
                    return
        else:
            self.destroyTime=time
    def AddComponent(self,component):
        name = component.monobehaviourname
        
        self.monobehaviours[name] = component
        component.gameObject = self
        return component
    def RemoveComponent(self,component):
        name = component.monobehaviourname
        #self.monobehaviours[name] = component
    def GetComponent(self,name):
        try:
            return self.monobehaviours[name]
        except:
            print(f"[Error] Could not get component {name} from object {self}")
    def Start(self): #Create your variables here
        pass
    def Update(self): #Runs every frame
        self.destroyTime-=Time.deltaTime
        if(self.destroyTime<0 and self.destroyTime>-9999):
            self.Destroy()
    def EarlyUpdate(self):
        pass
    def LateUpdate(self):
        pass
    def Instantiate(gameObject,position = None):
        new = GameObject()
        new.scene = gameObject.scene
        if(new.scene!=None):
            new.scene.AddGameObject(new)

        #clone transform
        if(position is None):
            position = gameObject.transform.position
        
        t = gameObject.transform.Clone()
        t.position = position.Clone() #neccesary, as its otherwise a reference, keeping transforms's the same
        new.transform = t.Clone()

        monos = {}
        #clone monobehaviours
        for key in gameObject.monobehaviours.keys():
            value = gameObject.monobehaviours[key]
            result = ""
            try:
                result = value.Clone()
                result.gameObject=new
                try:
                    result.transform = t
                except Exception as e2:
                    pass
                #print("new rigidbody pls")
            except Exception as e:
                print(f"[DEBUG] Could not run explicit cloning of monobehaviour "+value.monobehaviourname+f"\n - Err {e}")
                result = copy.copy(value)
                result.gameObject=new
                result.transform = t
            monos[key]=result
        new.monobehaviours=monos
        #print(new.transform.position.ToString())

        return new
            



