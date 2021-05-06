from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine


class Action:
    def __init__(self, engine) -> None:
        super().__init__()
        self.engine = engine

    def perform(self) -> None:
        """Perform this action with the objects needed to determine its scope.

        `engine` is the scope this action is being performed in.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()


class EscapeAction(Action):
    def perform(self) -> None:
        raise SystemExit()

class CloseMenu(Action):
    def perform(self) -> None:
        self.engine.close_menu()

class OpenMenu(Action):
    def perform(self) -> None:
        self.engine.open_menu()

class ShowTooltip(Action):
    def __init__(self, engine, tooltip_key: str) -> None:
        super().__init__(engine)
        self.tooltip_key = tooltip_key

    def perform(self):
        self.engine.show_tooltip(self.tooltip_key)

class HideTooltip(Action):
    def __init__(self, engine, tooltip_key: str) -> None:
        super().__init__(engine)
        self.tooltip_key = tooltip_key

    def perform(self):
        self.engine.hide_tooltip(self.tooltip_key)

class ChangePageAction(Action):
    def __init__(self, engine, new_page : str) -> None:
        super().__init__(engine)
        self.new_page = new_page

    def perform(self):
        self.engine.switch_page(self.new_page)

class SetupPersonStartAction(Action):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def perform(self):
        self.engine.game_sections["DecisionButtons"].disable_UI()

class SetupPersonEndAction(Action):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def perform(self):
        self.engine.game_sections["DecisionButtons"].enable_UI()

class BarPersonAction(Action):
    def perform(self):
        self.engine.barPerson()

class ArrestPersonAction(Action):
    def perform(self):
        self.engine.arrestPerson()

class LeavePersonAction(Action):
    def perform(self):
        self.engine.leavePerson()

class UpdatePoliticalPowerAction(Action):
    def __init__(self, engine, delta_power) -> None:
        super().__init__(engine)
        self.delta_power = delta_power

    def perform(self):
        self.engine.update_political_power(self.delta_power)

