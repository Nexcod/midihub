from .base import FunctionalTest


class HomePageTest(FunctionalTest):
    def test_display_latest_midi_files(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Midihub', self.browser.title)
        self.assertIn(self.browser.find_element_by_tag_name('h1'), 'Piano MIDI files')
