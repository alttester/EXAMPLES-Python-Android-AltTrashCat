import os
import sys

sys.path.append(os.path.dirname(__file__))

from pages.base_page import BasePage
from pages.game_play_page import GamePlayPage

class MainMenuPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Main')

    @property
    def store_button(self):
        return self.altdriver.find_element('StoreButton')
    
    @property
    def leader_board_button(self):
        return self.altdriver.find_element('OpenLeaderboard')

    @property
    def settings_button(self):
        return self.altdriver.find_element('SettingButton')

    @property
    def mission_button(self):
        return self.altdriver.find_element('MissionButton')

    @property
    def run_button(self):
        return self.altdriver.find_element('UICamera/Loadout/StartButton')

    @property
    def character_name(self):
        return self.altdriver.find_element('CharName')

    @property
    def theme_name(self):
        return self.altdriver.find_element('ThemeName')

    def is_displayed(self):
        if self.store_button and self.leader_board_button and self.settings_button \
            and self.mission_button and self.run_button and self.character_name and self.theme_name:
            return True

    def press_run(self):
        self.run_button.tap()
        return GamePlayPage(self.altdriver)
