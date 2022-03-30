from ursina import *
import math
from ursina.shaders import lit_with_shadows_shader
from ursina.camera import Camera

class Drone(Entity):
    def __init__(self):
        super().__init__(    
            model = 'assets/newdrone.obj',
            y = 0,
            color = color.gray,
            collider = 'cube',
            texture = 'white_cube',
            x = 0,
            z = 0
            )
        self.speed = 0
        
        self.fmode = ["Race", "Assisted", "Cinematic"]
        self.acceleration = 0.25
        self.droneSpeed = .5
        self.droneForwardSpeed = 35
        self.index = 0

        self.alt = Text(text='Altitude: '+str(self.y), x=0, y=0.49)
        self.spe = Text(text='Speed: '+str(self.speed), x=0, y=0.46)
        self.md = Text(text='Mode: '+str(self.fmode[self.index]), x=0, y=0.43)

    def reset(self):
        self.y = 1 
        self.speed = 0
        self.rotation_x = 0
        self.rotation_z = 0

    def update(self):

        self.alt.text = "Altitude: "+str(math.floor(self.y))+" Meters"
        self.spe.text = "Speed: "+str(self.speed)
        self.md.text = "Mode: "+str(self.fmode[self.index])

        # Modes
        # Race
        if self.index == 0:
            self.speed = min(self.speed, self.droneSpeed)
            self.y += self.speed
        # Assisted
        elif self.index == 1:
            self.speed = min(self.speed, self.droneSpeed)
            self.y += self.speed
        # Cine
        elif self.index == 2:
            self.y = self.y
            self.rotation_x = 0
            self.rotation_z = 0
        
        # go up
        if held_keys['space']:
            self.y += self.speed
            self.rotation_x = 0
            self.rotation_z = 0
        
        # flight_mode
        if held_keys['x']:
            self.index += 1
        if self.index >= len(self.fmode):
            self.index = 0
        
        # flight controls
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

        if self.y < 0:
            self.reset()
        
        #if held_keys['a']: 
        #    self.x -= self.acceleration * self.droneForwardSpeed * time.dt
        #    self.rotation_z = -8

        #if held_keys['a']: 
        #    self.x += self.acceleration * self.droneForwardSpeed * time.dt
        #    self.rotation_z = 8       

        # reset

