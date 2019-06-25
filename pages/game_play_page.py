from pages.base_page import BasePage
from pages.pause_overlay_page import PauseOverlayPage

class GamePlayPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    @property
    def pause_button(self):
        return self.altdriver.find_element('Game/WholeUI/pauseButton')
    
    @property
    def character(self):
        return self.altdriver.find_element('PlayerPivot')

    
    def is_displayed(self):
        if self.pause_button and self.character:
            return True

    def press_pause(self):
        self.pause_button.tap()
        return PauseOverlayPage(self.altdriver)