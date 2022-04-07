from ursina import *
from drone import Drone
from menu import Menu

window.borderless = False
window.show_ursina_splash = True
app = Ursina(title='Ursina Drone Sim')
window.exit_button.enabled = False
Sky()

drone = Drone()
menu = Menu(drone=drone)

def update():
    pass

app.run()