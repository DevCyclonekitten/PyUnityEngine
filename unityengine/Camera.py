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
        self.compressedtextures={}
        pygame.init()
        pygame.display.set_caption("Titler")
        self.window = pygame.display.set_mode((800, 480), pygame.DOUBLEBUF, vsync=1)
        self.Start()
    def Start(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS",20)


    def EarlyUpdate(self):
        self.window.fill(self.backgroundcolour)
    def Update(self):
        pass
    def WriteText(self,text,line):
        text_surface = self.font.render(text, False, (0, 0, 0))
        self.window.blit(text_surface,(0,line*30-30))
    def LateUpdate(self):

        
        self.WriteText(f"Frame {self.scene.frameCounter} Time {round(self.scene.frameCounter/60,2)}",1)
        self.WriteText(f"GameObjects {len(self.scene.sceneGameObjects)}",2)
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
    def Blit(self,transform,material,tex):
        
        
        #screen position
        width = transform.scale.x*100
        height = transform.scale.y*100

        if(transform.position.x+width/2 <=0 or transform.position.x-width/2 >self.SCREEN_WIDTH):
            return
        #if(transform.position.y+height/2<=0):
            #return
        blittex = None
        shortname = tex[0]+f"-{width}/{height}"
        if shortname in self.compressedtextures:
            blittex = self.compressedtextures[shortname]
        else:
            blittex = pygame.transform.scale(tex[1], (abs(width), abs(height)))
            blittex = pygame.transform.flip(blittex, width < 0, height < 0)
            self.compressedtextures[shortname]=blittex


        #check if it exists
        center = self.PositionToPixel(transform.position.ReturnSubtract(self.gameObject.transform.position)).ReturnAdd(Vector2(self.SCREEN_WIDTH/2,self.SCREEN_HEIGHT/2))
        center = center.ReturnSubtract(Vector2(abs(width)/2,-abs(height)/2))
        #center = self.PositionToPixel(center)
        #print((center.x,center.y))



        self.window.blit(blittex,(center.x,self.SCREEN_HEIGHT-center.y))

    def CreatePrefab(scene=None):
        go = GameObject()
        cam = Camera(gameObject=go)
        go.AddComponent(cam)
        if(scene!=None):
            scene.ConnectCamera(cam)
        return go