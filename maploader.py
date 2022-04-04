from ursina import *
from menu import Menu
import json

class MapLoader(FileBrowser):
    def __init__(self):
        super().__init__(
            file_types=('.json'),
            enabled = False
            )

    def on_submit(self, paths):
        with open(paths[0], "r") as _file:
            map_data = json.load(_file)
            print(json.dumps(map_data, indent=4, sort_keys=True))
            
            # Show Map after Loading
            Button(text=map_data["map_name"], scale_x=0.6, scale_y=0.3, y=0.15)
            Text(text=map_data["map_desc"], y=0.1, x=-0.25)
            Text(text=map_data["map_version"], y=0.13, x=-0.25)
