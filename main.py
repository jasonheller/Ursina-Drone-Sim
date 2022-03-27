from ursina import *
from drone import Drone
window.borderless = False
window.show_ursina_splash = True
app = Ursina(title='Ursina Drone Sim')
window.exit_button.enabled = False
Sky()

EditorCamera()
drone = Drone()

def update():
    pass

app.run()