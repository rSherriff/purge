from __future__ import annotations

import time
from enum import Enum, auto
from threading import Timer
from typing import TYPE_CHECKING

import numpy as np
import tcod
from playsound import playsound
from tcod.console import Console

import tile_types
from effects.melt_effect import MeltWipeEffect, MeltWipeEffectType
from input_handlers import EventHandler, MainGameEventHandler

from people.person_manager import PersonManager

from sections.general import GeneralSection
from sections.menu import Menu
from sections.page_list import PageList
from sections.page_one import PageOne
from sections.page_two import PageTwo
from sections.page_three import PageThree
from sections.page_four import PageFour
from sections.decision_buttons import DecisionButtons
from sections.pundits import Pundits
from sections.character_portrait import CharacterPortrait
from sections.seating import Seating
from sections.swingometer import Swingometer

from utils.delta_time import DeltaTime

from actions.actions import UpdatePoliticalPowerAction

from application_path import get_app_path


class GameState(Enum):
    MENU = auto()
    IN_GAME = auto()
    COMPLETE = auto()


class Engine:
    def __init__(self, teminal_width: int, terminal_height: int):

        self.screen_width = teminal_width
        self.screen_height = terminal_height
        self.delta_time = DeltaTime()

        self.event_handler: EventHandler = MainGameEventHandler(self)
        self.mouse_location = (0, 0)

        self.setup_effects()
        self.setup_sections()
        self.setup_game()
        self.state = GameState.IN_GAME

        self.start_game()

    def render(self, root_console: Console) -> None:
        """ Renders the game to console """
        for section_key, section_value in self.get_active_sections():
            if section_key not in self.disabled_sections:
                section_value.render(root_console)

        if self.state == GameState.IN_GAME:
            for tooltip in self.tooltips.values():
                tooltip.render(root_console)

        if self.full_screen_effect.in_effect == True:
            self.full_screen_effect.render(root_console)
        else:
            self.full_screen_effect.set_tiles(root_console.tiles_rgb)

    def update(self):
        """ Engine update tick """
        for _, section in self.get_active_sections():
            section.update()

        self.delta_time.update_delta_time()

    def handle_events(self, context: tcod.context.Context):
        self.event_handler.handle_events(
            context, discard_events=self.full_screen_effect.in_effect)

    def setup_effects(self): 
        self.full_screen_effect = MeltWipeEffect(self, 0, 0, 64, 35, MeltWipeEffectType.RANDOM, 100)

    def setup_sections(self):
        self.menu_sections = {}
        self.menu_sections["Menu"] = Menu(self, 0, 0, 64, 35)

        self.game_sections = {}
        self.game_sections["General"] = GeneralSection(self, 0, 0, self.screen_width, self.screen_height)
        self.game_sections["PageList"] = PageList(self, 3, 3, 43, 4)
        self.game_sections["PageOne"] = PageOne(self, 3, 7, 43, 53)
        self.game_sections["PageTwo"] = PageTwo(self, 3, 7, 43, 53)
        self.game_sections["PageThree"] = PageThree(self, 3, 7, 43, 53)
        self.game_sections["PageFour"] = PageFour(self, 3, 7, 43, 53)
        self.game_sections["DecisionButtons"] = DecisionButtons(self, 49, 49, 31, 18)
        self.game_sections["CharacterPortrait"] = CharacterPortrait(self, 49, 21, 31, 26)
        self.game_sections["Seating"] = Seating(self, 49, 3, 31, 16)
        self.game_sections["Pundits"] = Pundits(self, 83, 27, 32, 34)
        self.game_sections["Swingometer"] = Swingometer(self, 83, 3, 32, 22)

        self.completion_sections = {}

        self.disabled_sections = ["PageTwo", "PageThree", "PageFour"]

    def get_active_sections(self):
        if self.state == GameState.MENU:
            return self.menu_sections.items()
        elif self.state == GameState.IN_GAME:
            return self.game_sections.items()
        elif self.state == GameState.COMPLETE:
            return self.completion_sections.items()

    def setup_game(self):
        self.person_manager = PersonManager()
        self.political_power = 0
        self.tooltips = {}
        self.completion_criteria = {}

    def close_menu(self):
        self.state = GameState.IN_GAME
        self.full_screen_effect.start()

    def open_menu(self):
        self.state = GameState.MENU
        self.full_screen_effect.start()

    def start_game(self):
        self.nextPerson()

    def complete_game(self):
        self.state = GameState.COMPLETE
        self.full_screen_effect.start()

    def show_tooltip(self, key):
        self.tooltips[key].invisible = False

    def hide_tooltip(self, key):
        self.tooltips[key].invisible = True

    def get_delta_time(self):
        return self.delta_time.get_delta_time()

    def switch_page(self, new_page : str):
        if new_page in self.disabled_sections:
            self.disabled_sections.remove(new_page)

        if (new_page != "PageOne") and ("PageOne" not in self.disabled_sections):
            self.disabled_sections.append("PageOne")

        if (new_page != "PageTwo") and ("PageTwo" not in self.disabled_sections):
            self.disabled_sections.append("PageTwo")

        if (new_page != "PageThree") and ("PageThree" not in self.disabled_sections):
            self.disabled_sections.append("PageThree")

        if (new_page != "PageFour") and ("PageFour" not in self.disabled_sections):
            self.disabled_sections.append("PageFour")

    def nextPerson(self):
        self.game_sections["CharacterPortrait"].start_setup_person(self.person_manager.get_next_person())

    def barPerson(self):
        UpdatePoliticalPowerAction(self, self.person_manager.currentPerson.politicalPower).perform()
        self.nextPerson()

    def arrestPerson(self):
        UpdatePoliticalPowerAction(self, self.person_manager.currentPerson.politicalPower * 2).perform()
        self.nextPerson()

    def leavePerson(self):
        UpdatePoliticalPowerAction(self, -self.person_manager.currentPerson.politicalPower).perform()
        self.nextPerson()

    def update_political_power(self, delta_power):
        self.political_power += delta_power
        print(self.political_power)


