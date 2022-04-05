from ursina import *
import json

class MapLoader(FileBrowser):
    def __init__(self):
        super().__init__(
            file_types=('.json'),
            enabled = False
            )

    def on_play(self):
        self.enabled = False

    def on_submit(self, paths):
        with open(paths[0], "r") as _file:
            map_data = json.load(_file)
            print(json.dumps(map_data, indent=4, sort_keys=True))
            
            # Show Map after Loading
            Panel(scale_x=0.6, scale_y=0.3, y=0.15)
            Text(text=map_data["map_desc"], y=0.1, x=-0.25)
            Text(text=map_data["map_name"], y=0.2, x=-0.25)
            Text(text=map_data["map_version"], y=0.13, x=-0.25)
            Button(text='Play', scale_x=0.15, scale_y=0.075, y=0.040, z=-0.1, on_click=self.on_play)

            # Map Loading
            Entity(model=map_data["path_to_map"], texture=map_data["path_to_texture"], scale=map_data["map_scale"], x=map_data["map_x"],y=map_data["map_y"],z=map_data["map_z"], double_sided=map_data["double_sided"])
            
