from sections.section import Section

import numpy as np
import xp_loader
import gzip
import tile_types
import os.path
from application_path import get_app_path
from ui.general_ui import GeneralUI

menu_panel_xp_file = get_app_path() + '/images/menuPanel'


class GeneralSection(Section):
    def __init__(self, engine, x, y, width, height):
        super().__init__(engine, x, y, width, height)
        self.ui = GeneralUI(self, x, y)
