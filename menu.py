from ursina import *

class Menu(Entity):
    def __init__(self, drone, loader):
        super().__init__(parent=camera.ui, ignore=self)
        
        drone.enabled = False
        self.main_menu = Entity(parent=self, enabled=True)
        self.map_menu = Entity(parent=self, enabled=False)
        self.options_menu = Entity(parent=self, enabled=False)

        def switchMenu(menu1, menu2):
            menu1.enabled = False
            menu2.enabled = True

        # Map Functions
        def LoadCustomMap():
            loader.enabled = True
            drone.enabled = False
        
        # Testing Only!
        def UnstableBuild():
            drone.enabled = True
            self.map_menu.enabled = False

        # Main Menu
        Text("Drone Simulator", y=0.4, parent=self.main_menu, scale=3, origin=(0,0))
        Button(text="Exit", y=-0.2, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: application.quit())
        Button(text="Play", y=0.2, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: switchMenu(self.main_menu, self.map_menu))
        Button(text="Options", y=0.0, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: switchMenu(self.main_menu, self.options_menu))
        
        # Options Menu
        Text("Options", y=0.4, parent=self.options_menu, scale=3, origin=(0,0))
        Button(text="Back", y=-0.2, parent=self.options_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: switchMenu(self.options_menu, self.main_menu))

        # Map Selection
        Text("Map Selection", y=0.4, parent=self.map_menu, scale=3, origin=(0,0))
        Button(text="Back", y=-0.2, parent=self.map_menu, scale_x=0.2, scale_y=0.1, on_click=lambda: switchMenu(self.map_menu, self.main_menu))
        # Maps
        Button(text="Load custom map", y=-0.2, x=0.6, parent=self.map_menu, scale_x=0.22, scale_y=0.1, on_click=LoadCustomMap)
        Button(text="Play unstable", y=-0.2, x=-0.6, parent=self.map_menu, scale_x=0.22, scale_y=0.1, on_click=UnstableBuild)

        