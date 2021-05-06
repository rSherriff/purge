from sections.section import Section

import numpy as np
import xp_loader
import gzip
import tile_types
import os.path
from actions.actions import SetupPersonStartAction, SetupPersonEndAction
from application_path import get_app_path
from threading import Timer

xp_filepath = get_app_path() + '/images/character_portrait.xp'


class CharacterPortrait(Section):
    def __init__(self, engine, x, y, width, height):
        super().__init__(engine, x, y, width, height)

        xp_file = gzip.open(xp_filepath)
        raw_data = xp_file.read()
        xp_file.close()

        xp_data = xp_loader.load_xp_string(raw_data)

        self.tiles = np.full((self.width, self.height),
                             fill_value=tile_types.blank, order="F")

        for h in range(0, self.height):
            for w in range(0, self.width):
                self.tiles[w, h]['graphic'] = xp_data['layer_data'][0]['cells'][w][h]

        #self.ui = MenuUI(self, x, y, self.animated_tiles[0]["graphic"])
        self.selected_tiles = 0


    def start_setup_person(self, person):
        SetupPersonStartAction(self.engine).perform()

        #do setup
        
        person.print()
        Timer(2, self.end_setup_person).start()

    def end_setup_person(self):
        SetupPersonEndAction(self.engine).perform()