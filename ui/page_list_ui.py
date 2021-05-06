from ui.ui import UI
from ui.ui import Button

from actions.actions import ChangePageAction

class PageListUI(UI):
    def __init__(self, section, x, y, tiles):
        super().__init__(section, x, y)
        self.elements = list()

        bd = [0, 0 ,10,4] #Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        one_button = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=ChangePageAction(self.section.engine, "PageOne"), tiles=button_tiles )
        self.add_element(one_button)

        bd = [11, 0 ,10,4] #Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        one_button = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=ChangePageAction(self.section.engine, "PageTwo"), tiles=button_tiles )
        self.add_element(one_button)

        bd = [22, 0 ,10,4] #Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        one_button = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=ChangePageAction(self.section.engine, "PageThree"), tiles=button_tiles )
        self.add_element(one_button)

        bd = [33, 0 ,10,4] #Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        one_button = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=ChangePageAction(self.section.engine, "PageFour"), tiles=button_tiles )
        self.add_element(one_button)
