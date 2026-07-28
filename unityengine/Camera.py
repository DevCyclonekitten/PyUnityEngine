from unityengine.Vector2 import Vector2
from unityengine.GameObject import GameObject
import pygame
class Camera():
    def __init__(self,gameObject=None):
        self.usingUnityEngine = True
        self.enabled = True
        self.monobehaviourname = "Camera"
        self.gameObject = gameObject
        self.backgroundcolour = (255,255,255)
        self.SCREEN_WIDTH=800
        self.SCREEN_HEIGHT=480
        self.scene=None
        pygame.init()
        pygame.display.set_caption("Titler")
        self.window = pygame.display.set_mode((800, 480))
        self.Start()
    def Start(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS",20)
        pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.


    def EarlyUpdate(self):
        self.window.fill(self.backgroundcolour)
    def Update(self):
        pass
    def LateUpdate(self):
        text_surface = self.font.render("Frame "+str(self.scene.frameCounter)+ "  Time: "+str(round(self.scene.frameCounter/60,2)), False, (0, 0, 0))
        self.window.blit(text_surface,(0,0))
        pygame.display.update()
    def PositionToPixel(self,position):
        return position.ReturnScaled(100)
    def PixelToPosition(self,pixel):
        return pixel.ReturnScaled(100)
    def PixelToLength(self,length):
        return length/100
    def RenderRect(self,transform, material):
        #screen position
        width = transform.scale.x*100
        height = transform.scale.y*100
        center = self.PositionToPixel(transform.position.ReturnSubtract(self.gameObject.transform.position)).ReturnAdd(Vector2(self.SCREEN_WIDTH/2,self.SCREEN_HEIGHT/2))
        center = center.ReturnSubtract(Vector2(width/2,-height/2))
        #center = self.PositionToPixel(center)
        pygame.draw.rect(self.window,material.baseColour,(center.x,self.SCREEN_HEIGHT-center.y,width,height))
        #print((center.x,center.y))
    def CreatePrefab(scene=None):
        go = GameObject()
        cam = Camera(gameObject=go)
        go.AddComponent(cam)
        if(scene!=None):
            scene.ConnectCamera(cam)
        return go