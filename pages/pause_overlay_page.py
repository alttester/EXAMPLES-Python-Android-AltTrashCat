from pages.base_page import BasePage
# from pages.main_menu_page import MainMenuPage

class PauseOverlayPage(BasePage):
    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    @property
    def resume_button(self):
        return self.altdriver.find_element('Game/PauseMenu/Resume')

    @property
    def main_menu_button(self):
        return self.altdriver.find_element('Game/PauseMenu/Exit')

    @property
    def title(self):
        return self.altdriver.find_element('Game/PauseMenu/Text')

    def is_displayed(self):
        if resume_button and main_menu_button and title:
            return True