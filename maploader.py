from ursina import *

class MapLoader(FileBrowser):
    def __init__(self):
        super().__init__(
            file_types=('.json'),
            enabled = False
            )