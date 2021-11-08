from vpython import *
import random

class Kula(sphere):
    def __init__(self):
        pos=vector(random.randrange(-11,11),1.25,random.randrange(-6,6))
        velocity=vector(random.randrange(0,7),0,random.randrange(0,7))
        color=vector(random.randrange(0,10),random.randrange(0,10),random.randrange(0,10))
        super().__init__(pos=pos,radius=1,color=color,velocity=velocity)
    def chpos(self,):
        dt = 0.01 
        self.pos = self.pos + self.velocity*dt
        if self.pos.x >= 9.9 or self.pos.x <= -9.9:
            self.velocity.x = self.velocity.x * -1
        if self.pos.z >= 5.45 or self.pos.z <= -5.45:
            self.velocity.z = self.velocity.z * -1
        self.pos = self.pos + self.velocity*dt
#x = sphere(pos=vector(0,0,0),radius=1) 
floor = box (pos=vector(0,0,0), length=22.8, height=0.5, width=12.9, color=color.green)
k1 = Kula()
k2 = Kula()
k3 = Kula()
banda1 = box(pos=vector(0,0.75,6.95),length=22.8,height=1,width=1,color=color.red)
banda2 = box(pos=vector(11.9,0.75,0),length=1,height=1,width=14.9,color=color.red)
banda3 = box(pos=vector(0,0.75,-6.95),length=22.8,height=1,width=1,color=color.red)
banda4 = box(pos=vector(-11.9,0.75,0),length=1,height=1,width=14.9,color=color.red)

#ball = sphere (pos=vector(0,1.5,0), radius=1, color=color.blue)
#ball.velocity = vector(3,0,2)
#ball1 = sphere (pos=vector(1,1.5,1), radius=1, color=color.yellow)
#ball1.velocity = vector(5,0,1)

while 1:
    rate (200)
    k1.chpos()
    k2.chpos()
    k3.chpos()
