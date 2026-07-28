from unityengine.Vector2 import Vector2
from unityengine.GameObject import GameObject
from unityengine.Material import Material
class SpriteRenderer():
    def __init__(self,gameObject=None,camera = None,material=Material()):
        self.usingUnityEngine = True
        self.enabled = True
        self.gameObject = gameObject
        self.monobehaviourname = "SpriteRenderer"
        self.camera = camera
        self.scene = None
        self.Start()
        self.material = material

    def GetCamera(camera):
        self.camera = camera
    def Start(self):
        if(self.scene!=None):
            self.camera = self.scene.camera
    def Update(self):
        if(self.camera!=None):
            self.camera.RenderRect(self.gameObject.transform.position,self.material,100*self.gameObject.transform.scale.x,100**self.gameObject.transform.scale.y)
        else:
            if(self.scene!=None):
                self.camera = self.scene.camera
    def EarlyUpdate(self):
        pass
    def LateUpdate(self):
        pass
    def CreatePrefab(scene=None,material=Material()):
        go = GameObject()
        spr = SpriteRenderer(material=material)
        spr.scene=scene
        scene.AddGameObject(go)

        go.AddComponent(spr)
        return go