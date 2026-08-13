from unityengine.Vector2 import Vector2
from unityengine.GameObject import GameObject
from unityengine.Material import Material
import os,pygame


class SpriteRenderer():
    def __init__(self,gameObject=None,camera = None,material=Material(),texturepath=""):
        self.usingUnityEngine = True
        self.enabled = True
        self.gameObject = gameObject
        self.monobehaviourname = "SpriteRenderer"
        self.camera = camera
        self.scene = None
        self.Start()

        self.material = material
        self.texturepath = texturepath
        self.texture = None
        self.texturerect=None
        self.LoadTexture(self.texturepath)


    def LoadTexture(self,texturepath):
        self.texturepath=texturepath
        if(self.texturepath!=""):
            path = os.path.join("Assets",self.texturepath)
            self.texture=[path,pygame.image.load(path).convert_alpha()]
            #self.texturerect = self.texture.get_rect()
            #self.texturerect.topleft = (100,100)
    def GetCamera(camera):
        self.camera = camera
    def Start(self):
        if(self.scene!=None):
            self.camera = self.scene.camera
        if(self.gameObject!=None):
            self.gameObject.scene = self.scene
    def Update(self):
        if(self.camera!=None):
            #print("Cam is valid")
            if(self.texture==None):
                self.camera.RenderRect(self.gameObject.transform,self.material)
            else:
                self.camera.Blit(self.gameObject.transform,self.material,self.texture)
        else:
            if(self.scene!=None):
                #print("Scene is not none")
                self.camera = self.scene.camera
            else:
                print("Scene and cam is none")
    def EarlyUpdate(self):
        pass
    def LateUpdate(self):
        pass
    def CreatePrefab(scene=None,material=Material()):
        go = GameObject()
        spr = SpriteRenderer(material=material)
        spr.scene=scene
        go.AddComponent(spr)


        scene.AddGameObject(go)

        return go
    def Clone(self):
        spr = SpriteRenderer()
        spr.camera = self.camera
        spr.material = self.material
        if(self.texturepath!=None):
            spr.texturepath=self.texturepath
            spr.texture=self.texture
        return spr
