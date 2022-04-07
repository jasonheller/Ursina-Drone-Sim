from ursina import *
from ursina import FileBrowser
import json

class Menu(Entity):
    def __init__(self, drone):
        super().__init__(parent=camera.ui, ignore=self)
        
        ec = EditorCamera(enabled=False)
        fb = FileBrowser(file_types='.json', enabled=False)
        drone.enabled = False
        self.main_menu = Entity(parent=self, enabled=True)
        self.map_menu = Entity(parent=self, enabled=False)
        self.options_menu = Entity(parent=self, enabled=False)
        self.background = Sprite('shore')

        def switch(menu1, menu2):
            menu1.enabled = False
            menu2.enabled = True

        # Map Functions
        def LoadCustomMap():
            fb.enabled = True
            drone.enabled = False
        
        # Testing Only!
        def UnstableBuild():
            drone.enabled = True
            self.map_menu.enabled = False

        def on_submit(paths):
            with open(paths[0], "r") as _file:
                map_data = json.load(_file)
                print(json.dumps(map_data, indent=4, sort_keys=True))

                def play():
                    drone.enabled = True
                    fb.enabled = False
                    self.background.enabled = False
                    self.map_menu.enabled = False
                    ec.enabled = True
                    _map1.enabled = False; _map2.enabled = False
                    _map2.enabled = False; _map3.enabled = False
                    _map4.enabled = False; _map5.enabled = False
                    _mapX.enabled = False; _map.enabled = True

                def newMap():
                    drone.enabled = False
                    fb.enabled = False
                    ec.enabled = False
                    _map.enabled = False
                    self.map_menu.enabled = True
                    self.background.enabled = True
                    _map1.enabled = False; _map2.enabled = False
                    _map2.enabled = False; _map3.enabled = False
                    _map4.enabled = False; _map5.enabled = False
                    _mapX.enabled = False;

                _map1 = Panel(scale_x=0.6, scale_y=0.3, y=0.15)
                _map2 = Text(text=map_data["map_desc"], y=0.1, x=-0.25)
                _map3 = Text(text=map_data["map_name"], y=0.2, x=-0.25)
                _map4 = Text(text=map_data["map_version"], y=0.13, x=-0.25)
                _map5 = Button(text='Play', scale_x=0.15, scale_y=0.075, y=0.040, z=-0.1, on_click=play)
                _mapX = Button(text='X', scale_x=0.1, scale_y=0.1, model='circle', x=0.25, y=0.25, on_click=newMap)

                _map = Entity(model=map_data["path_to_map"], texture=map_data["path_to_texture"], scale=map_data["map_scale"], x=map_data["map_x"],y=map_data["map_y"],z=map_data["map_z"], double_sided=map_data["double_sided"])

        fb.on_submit = on_submit

        # Main Menu
        Text("Drone Simulator", y=0.4, parent=self.main_menu, scale=3, origin=(0,0))
        Button(text="Exit", y=-0.2, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: application.quit())
        Button(text="Play", y=0.2, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: switch(self.main_menu, self.map_menu))
        Button(text="Options", y=0.0, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: switch(self.main_menu, self.options_menu))
        
        # Options Menu
        Text("Options", y=0.4, parent=self.options_menu, scale=3, origin=(0,0))
        Button(text="Back", y=-0.2, parent=self.options_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: switch(self.options_menu, self.main_menu))

        # Map Selection
        Text("Map Selection", y=0.4, parent=self.map_menu, scale=3, origin=(0,0))
        Button(text="Back", y=-0.2, parent=self.map_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: switch(self.map_menu, self.main_menu))
        # Maps
        Button(text="Load custom map", y=-0.2, x=0.6, parent=self.map_menu, scale_x=0.22, scale_y=0.1, on_click=LoadCustomMap)
        Button(text="Play unstable", y=-0.2, x=-0.6, parent=self.map_menu, scale_x=0.22, scale_y=0.1, on_click=UnstableBuild)

        