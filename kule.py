from vpython import *
from math import sqrt
import random

class Kula(sphere):
    def __init__(self):
        pos=vector(random.randrange(-11,11),1.25,random.randrange(-6,6))
        velocity=vector(random.randrange(1,7),0,random.randrange(1,7))
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
def colision(k1,k2):
    if sqrt(((k1.pos.x - k2.pos.x)**2) + ((k1.pos.z - k2.pos.x) ** 2)) <= 2.:
        print("zmiana")
        ramie = vector(k2.pos.x - k1.pos.x,0,k2.pos.z - k1.pos.z)
        x = round(sqrt(((k1.velocity.x **2)+(k1.velocity.z **2))*((ramie.x **2)+(ramie.z **2))),3)
        print(x)
        cos1 = (k1.velocity.x * ramie.x) + (k1.velocity.z * ramie.z)/x
        l_vel = round(sqrt((k1.velocity.x **2) + (k1.velocity.z **2)),3)
        l_vk = l_vel * cos1
        l_ram = round(sqrt((ramie.x **2) + (ramie.z **2)),3)
        stos = l_vk/l_ram
        new_vec_skl = vector(ramie.x*stos,0,ramie.z*stos)
        new_k2_vel = k2.velocity + new_vec_skl
        #########
        ramie = vector(k1.pos.x - k2.pos.x,0,k1.pos.z - k2.pos.z)
        x = round(sqrt(((k2.velocity.x **2)+(k2.velocity.z **2))*((ramie.x **2)+(ramie.z **2))),3)
        print(x)
        cos2 = (k2.velocity.x * ramie.x) + (k2.velocity.z * ramie.z)/x
        l_vel = round(sqrt((k2.velocity.x **2) + (k2.velocity.z **2)),3)
        l_vk = l_vel * cos2
        l_ram = round(sqrt((ramie.x **2) + (ramie.z **2)),3)
        stos = l_vk/l_ram 
        new_vec_skl = vector(ramie.x*stos,0,ramie.z*stos) 
        new_k1_vel = k1.velocity + new_vec_skl
        k1.velocity = new_k1_vel
        k2.velocity = new_k2_vel
        print(k1.velocity, k2.velocity)
  
floor = box (pos=vector(0,0,0), length=22.8, height=0.5, width=12.9, color=color.green)
scene.camera.pos = vector(0,0,20)
scene.center = vector(0,0,0)
list_ball = [Kula(),Kula()]
list_ball[0].pos = vector(6,1.15,0.5)
list_ball[1].pos = vector(-6,1.25,-0.5)
list_ball[0].velocity = vector(-1,0,0)
list_ball[1].velocity = vector(1,0,0)

list_ball[0].color = color.red # = Kula()
list_ball[1].color = color.blue # = Kula()
#list_ball[2] = Kula()
#list_ball[2] = Kula()
banda1 = box(pos=vector(0,0.75,6.95),length=22.8,height=1,width=1,color=color.red)
banda2 = box(pos=vector(11.9,0.75,0),length=1,height=1,width=14.9,color=color.red)
banda3 = box(pos=vector(0,0.75,-6.95),length=22.8,height=1,width=1,color=color.red)
banda4 = box(pos=vector(-11.9,0.75,0),length=1,height=1,width=14.9,color=color.red)

#ball = sphere (pos=vector(0,1.5,0), radius=1, color=color.blue)
#ball.velocity = vector(3,0,2)
#ball1 = sphere (pos=vector(1,1.5,1), radius=1, color=color.yellow)
#ball1.velocity = vector(5,0,1)

while 1:
    rate (50)
    list_ball[0].chpos()
    list_ball[1].chpos()
    #list_ball[2].chpos()
    #k3.chpos()
    x = 0
    y = 1
    while x < len(list_ball):
        while y < len(list_ball):
            colision(list_ball[x],list_ball[y])
            y+=1
        x+=1
