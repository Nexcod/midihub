from .base import FunctionalTest


class HomePageTest(FunctionalTest):
    def test_display_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('MidiHub', self.browser.title)
        self.assertIn(self.browser.find_element_by_tag_name('h1').text, 'MidiHub')
