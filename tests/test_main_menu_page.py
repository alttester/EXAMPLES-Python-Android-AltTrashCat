from .utils import AltTestCase
from pages.main_menu_page import MainMenuPage


class TestMainMenuPage(AltTestCase):

    def setUp(self):
        self.main_menu_page = MainMenuPage(self.altdriver)
        self.main_menu_page.load()

    def test_main_menu_page_loaded_correctly(self):
        assert self.main_menu_page.is_displayed()
