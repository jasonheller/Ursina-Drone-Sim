from ursina import *
import math

class Drone(Entity):
    def __init__(self):
        super().__init__(    
            model = 'assets/drone.obj',
            y = 0,
            color = color.red,
            collider = 'cube',
            texture = 'white_cube',
            x = 0,
            z = 0
            )
        self.speed = 0
        
        self.fmode = "Race"
        self.acceleration = 0.25
        self.droneSpeed = .5
        self.droneForwardSpeed = 35
        self.autoHold = False

        self.alt = Text(text='Altitude: '+str(self.y), x=0, y=0.49)
        self.spe = Text(text='Speed: '+str(self.speed), x=0, y=0.46)
        self.md = Text(text='Mode: '+self.fmode, x=0, y=0.43)
        self.hold = Text(text='Autohold: '+str(self.autoHold), x=0, y=0.40)

    def update(self):
        
        self.alt.text = "Altitude: "+str(math.floor(self.y))+" Meters"
        self.spe.text = "Speed: "+str(self.speed)
        self.md.text = "Mode: "+self.fmode
        self.hold.text = "Autohold: "+str(self.autoHold)

        if self.fmode == "Race" and self.autoHold == False:
            self.speed = min(self.speed, self.droneSpeed)
            self.y += self.speed
            
        if held_keys['space']:
            self.autoHold = True
        if self.autoHold == True:
            self.y = self.y
            self.rotation_x = 0
            self.rotation_z = 0

        if held_keys['w']:
            self.speed += self.acceleration * time.dt 
            self.rotation_x = 8
            self.z += self.acceleration * self.droneForwardSpeed* time.dt
        else:
            self.speed -= self.acceleration * time.dt

        if held_keys['s']:
            self.autoHold = False
            self.rotation_x = -8
            self.z -= self.acceleration * self.droneForwardSpeed* time.dt


        #if held_keys['a']: 
        #    self.x -= self.acceleration * time.dt
        #    self.rotation_z = -4
        #if held_keys['d']:
        #    self.x += self.acceleration * time.dt
        #    self.rotation_z = 4

        # reset
        if self.y < 0:
            self.y = 1 
            self.speed = 0
            self.rotation_x = 0
            self.rotation_z = 0



