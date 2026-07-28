import pygame
class Input():
    def __init__(self):
        self.bindings = [["left",pygame.K_a,pygame.K_LEFT],["right",pygame.K_d,pygame.K_RIGHT],["up",pygame.K_w,pygame.K_UP],["down",pygame.K_s,pygame.K_DOWN]]
    def ClearBindings(self):
        self.bindings=[]
    def AddBinding(self,value,keys):
        listv = []
        listv.append(value)
        for item in keys:
            listv.append(item)
        self.bindings.append(listv)
    def GetPressed(self):
        keys = pygame.key.get_pressed()
        
        resultmap = {}
        for binding in self.bindings:
            root = binding[0]
            resultmap[root]=False
            for i in range(len(binding)-1):
                if(keys[binding[i+1]]):
                    resultmap[root]=True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                resultmap["exit"]=True
        return resultmap
    def GetDown(self):
        
        resultmap = {}

        for binding in self.bindings:
            root = binding[0]
            resultmap[root]=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                resultmap["exit"]=True
            elif event.type == pygame.KEYDOWN:
                for binding in self.bindings:
                    root = binding[0]
                    resultmap[root]=False
                    for i in range(len(binding)-1):
                        if(event.key ==binding[i+1]):
                            resultmap[root]=True
                if event.key == pygame.K_ESCAPE:
                    resultmap["exit"]=True
        return resultmap
