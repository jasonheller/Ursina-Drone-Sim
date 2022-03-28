from ursina import *
from drone import Drone
window.borderless = False
window.show_ursina_splash = True
app = Ursina(title='Ursina Drone Sim')
window.exit_button.enabled = False
Sky()

drone = Drone()
EditorCamera()

# World
ground = Entity(model='plane', texture='brick', collider='plane', color=color.green, scale_x=100, scale_z=100, x=0, y=0, z=0)
obstacle1 = Entity(model='cube', texture='brick', color=color.orange, scale_x=1, scale_y=5, x=0, y=1, z=12)
obstacle2 = Entity(model='cube', texture='brick', color=color.orange, scale_x=5, scale_y=4, x=-5, y=1, z=-26)
obstacle3 = Entity(model='cube', texture='brick', color=color.orange, scale_x=5, scale_y=4, x=3, y=1, z=14)

def update():
    pass

app.run()