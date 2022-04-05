from ursina import *
from drone import Drone
from menu import Menu
from maploader import MapLoader

window.borderless = False
window.show_ursina_splash = True
app = Ursina(title='Ursina Drone Sim')
window.exit_button.enabled = False
Sky()

drone = Drone()
maploader = MapLoader()
menu = Menu(drone=drone, loader=maploader)
EditorCamera()

def update():
    pass

app.run()