from ursina import *

class Menu(Entity):
    def __init__(self, drone):
        super().__init__(parent=camera.ui, ignore=self)
        
        drone.enabled = False
        self.main_menu = Entity(parent=self, enabled=True)
        self.map_menu = Entity(parent=self, enabled=False)
        self.options_menu = Entity(parent=self, enabled=False)

        def quitGame():
            application.quit()

        def playGame():
            self.main_menu.enabled = False
            self.map_menu.enabled = True
            drone.enabled = False

        def optionsMenu():
            self.main_menu.enabled = False
            self.options_menu.enabled = True

        def mainMenu():
            self.options_menu.enabled = False
            self.map_menu.enabled = False
            self.main_menu.enabled = True

        # Map Functions
        def TestMap():
            self.map_menu.enabled = False
            drone.enabled = True

        # Main Menu
        Text("Drone Simulator", y=0.4, parent=self.main_menu, scale=3, origin=(0,0))
        Button(text="Exit", y=-0.2, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=quitGame)
        Button(text="Play", y=0.2, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=playGame)
        Button(text="Options", y=0.0, parent=self.main_menu, scale_x=0.2, scale_y=0.1, on_click=optionsMenu)
        
        # Options Menu
        Text("Options", y=0.4, parent=self.options_menu, scale=3, origin=(0,0))
        Button(text="Back", y=-0.2, parent=self.options_menu, scale_x=0.2, scale_y=0.1, on_click=mainMenu)

        # Map Selection
        Text("Map Selection", y=0.4, parent=self.map_menu, scale=3, origin=(0,0))
        Button(text="Back", y=-0.2, parent=self.map_menu, scale_x=0.2, scale_y=0.1, on_click=mainMenu)
        # Maps
        Button(text="Test Map", y=0.1, parent=self.map_menu, scale_x=0.2, scale_y=0.2, on_click=TestMap)

