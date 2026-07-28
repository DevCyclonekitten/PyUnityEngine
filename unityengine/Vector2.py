class Vector2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def ToString(self):
        return f"Vector2 ({round(self.x,5)},{round(self.y,5)})"
    def Scale(self,vector):
        self.x *= vector.x
        self.y *= vector.y
    def Add(self,vector):
        self.x +=vector.x
        self.y += vector.y
    def ReturnAdd(self,vector):
        v = Vector2(self.x+vector.x,self.y+vector.y)
        return v
    def ReturnSubtract(self,vector):
        v = Vector2(self.x-vector.x,self.y-vector.y)
        return v
    def ReturnMultiply(self,fact):
        v = Vector2(self.x*fact,self.y*fact)
        return v

    def Multiply(self,fact):
        self.x*=fact
        self.y*=fact
    def ReturnScaled(self,fact):
        v = Vector2(self.x*fact,self.y*fact)
        return v


def Clamp(inp, min,max):
    if(inp<min):
        return min
    if(inp>max):
        return max
    return inp