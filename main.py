from unityengine import *
from Card import *
import random

scene = Scene()
time = Time()
camera = Camera.CreatePrefab(scene = scene)



card = Card.CreatePrefab(scene=scene)
cs = card.GetComponent("Card")
counter = 1
state = 1
while True:
    counter+=1
    if(counter>250):
        counter=0
        state+=1
        if(state>2):
            state=1
        cs.SetState(state)



    scene.RunMonobehaviour()
    time.Tick()