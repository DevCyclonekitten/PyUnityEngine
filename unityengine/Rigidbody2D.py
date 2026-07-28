from unityengine.Vector2 import *
from unityengine.Time import *
class Rigidbody2D():
    def __init__(self,gameObject=None): #Create your variables here
        #These variables are required
        self.usingUnityEngine = True
        self.enabled = True
        self.gameObject = gameObject
        self.monobehaviourname = "Rigidbody2D"
        
        
        #These are optional
        self.Start()
    
    def Start(self): #Create your variables here
        self.transform = self.gameObject.transform
        self.velocity = Vector2(0,0)
        self.angularVelocity = 0

        self.mass = 1
        self.gravity = -9.81
        self.linearDrag = 0.1
        self.angularDrag = 0

        self.linearDragClipping = 0.1
    def Update(self): #Runs every frame
        self.velocity.Multiply(1-(self.linearDrag*Time.deltaTime))

    
        self.velocity.Add(Vector2(0,self.gravity*Time.deltaTime))
        self.transform.position.Add(self.velocity.ReturnScaled(Time.deltaTime))
                
        #print("Velocity: "+self.velocity.ToString() +" - Position: "+self.transform.position.ToString())
    
        # have to add drag, something based on v^2 and mass
    
    
    def AddForce(self,forceVector):
        self.velocity.Add(forceVector.ReturnMultiply(1/(self.mass * self.mass)))
    def EarlyUpdate(self):
        pass
    def LateUpdate(self):
        pass