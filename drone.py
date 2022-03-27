from ursina import *
import math

class Drone(Entity):
    def __init__(self):
        super().__init__(    
            model = 'assets/drone.obj',
            y = 0,
            color = color.red,
            texture = 'white_cube',
            x = 0,
            z = 0
            )

        self.upForce = 0.1
        self.alt = Text(text='Altitude: '+str(self.y), x=0, y=0.49)
        
    def update(self):
        self.alt.text = "Altitude: "+str(math.floor(self.y))+" Meters"
        if held_keys['w']:
            print("W Key is pressed")
            self.y += self.upForce
