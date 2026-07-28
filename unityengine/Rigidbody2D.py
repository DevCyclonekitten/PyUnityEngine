from unityengine.Vector2 import *
from unityengine.Time import *
class Rigidbody2D():
    def __init__(self,gameObject=None): #Create your variables here
        #These variables are required
        self.usingUnityEngine = True
        self.enabled = True
        self.gameObject = gameObject
        self.monobehaviourname = "Rigidbody2D"
        self.started = False
        
        #Velocity Settings
        self.movementsystem = "Dynamic"
        self.velocity = Vector2(0,0)
        self.angularVelocity = 0

        self.mass = 1
        self.gravity = -9.81
        self.linearDrag = 0.1
        self.angularDrag = 0
        self.linearDragClipping = 0.1
        #These are optional
    
    def Start(self): #Grab Hook to transform
        if(self.gameObject!=None):
            self.transform = self.gameObject.transform

    def Update(self): #Runs every frame
        


        if(self.movementsystem=="Dynamic"):
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
    def Clone(self):
        #print("[INFO] Cloning Rigidbody2D is not fully implemented")
        rb = Rigidbody2D()
        rb.movementsystem = self.movementsystem
        rb.velocity = self.velocity.Clone() #bru, omg, not cloning this made them connect. screw you references
        rb.angularVelocity = self.angularVelocity

        rb.mass = self.mass
        rb.gravity = self.gravity
        rb.linearDrag = self.linearDrag
        rb.angularDrag = self.angularDrag
        rb.linearDragClipping = self.linearDragClipping
        return rb