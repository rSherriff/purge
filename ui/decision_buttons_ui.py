from ui.ui import UI
from ui.ui import Button

from actions.actions import BarPersonAction, ArrestPersonAction, LeavePersonAction

class DecisionButtonsUI(UI):
    def __init__(self, section, x, y, tiles):
        super().__init__(section, x, y)
        self.elements = list()

        bd = [1, 1 ,29,5] #Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        one_button = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=BarPersonAction(self.section.engine), tiles=button_tiles )
        self.add_element(one_button)
 
        bd = [1, 7 ,29,5] #Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        one_button = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=ArrestPersonAction(self.section.engine), tiles=button_tiles )
        self.add_element(one_button)

        bd = [1, 13, 29,5] #Button Dimensions
        button_tiles = tiles[bd[0]:bd[0] + bd[2], bd[1]:bd[1] + bd[3]]
        one_button = Button(x=bd[0], y=bd[1], width=bd[2], height=bd[3], click_action=LeavePersonAction(self.section.engine), tiles=button_tiles )
        self.add_element(one_button)
