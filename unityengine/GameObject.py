from unityengine.Transform import *
class GameObject():
    def __init__(self): #Create your variables here
        #These variables are required
        self.usingUnityEngine = True
        self.enabled = True
        self.monobehaviours = {}
        self.monobehaviourname = "GameObject"
        self.transform = Transform()
    def AddComponent(self,component):
        name = component.monobehaviourname
        
        self.monobehaviours[name] = component
        component.gameObject = self
    def RemoveComponent(self,component):
        name = component.monobehaviourname
        #self.monobehaviours[name] = component
    def GetComponent(self,name):
        return self.monobehaviours[name]
    def Start(self): #Create your variables here
        pass
    def Update(self): #Runs every frame
        pass
    def EarlyUpdate(self):
        pass
    def LateUpdate(self):
        pass



