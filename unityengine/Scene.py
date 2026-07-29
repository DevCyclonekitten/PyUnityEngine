class Scene():
    sceneGameObjects = 5
    def __init__(self,camera = None):
        self.sceneGameObjects = []
        self.camera = camera
        self.frameCounter=0
        self.hasRanStart = False
    def ConnectCamera(self,camera):
        self.camera = camera
        self.AddGameObject(self.camera.gameObject)
        self.camera.scene=self
        #self.camera.
    def StartMonobehaviour(self):
        for gameObject in self.sceneGameObjects:
            for monobehaviour in gameObject.monobehaviours.keys():
                m = gameObject.monobehaviours[monobehaviour]
                if(m.usingUnityEngine):
                    m.scene=self
                    m.Start()
    def RunMonobehaviour(self):
        if(not self.hasRanStart):
            self.StartMonobehaviour()
        self.frameCounter+=1
        for gameObject in self.sceneGameObjects:
            for monobehaviour in gameObject.monobehaviours.keys():
                m = gameObject.monobehaviours[monobehaviour]
                if(m.usingUnityEngine):
                    m.EarlyUpdate()

        for gameObject in self.sceneGameObjects:
            gameObject.Update()
            for monobehaviour in gameObject.monobehaviours.keys():
                m = gameObject.monobehaviours[monobehaviour]
                if(m.usingUnityEngine):
                    m.Update()
                    print(str(m))

        for gameObject in self.sceneGameObjects:
            for monobehaviour in gameObject.monobehaviours.keys():
                m = gameObject.monobehaviours[monobehaviour]
                if(m.usingUnityEngine):
                    m.LateUpdate()
    def AddGameObject(self,gameobject):
        self.sceneGameObjects.append(gameobject)
