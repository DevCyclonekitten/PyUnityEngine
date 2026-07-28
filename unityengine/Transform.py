from unityengine.Vector2 import Vector2

class Transform():
    def __init__(self):
        self.position = Vector2(0,0)
        self.rotation = Vector2(0,0)
        self.scale = Vector2(1,1)
    def Clone(self):
        n = Transform()
        n.position = self.position.Clone()
        n.rotation = self.rotation.Clone()
        n.scale = self.scale.Clone()
        return n