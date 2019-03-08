from django.test import TestCase

from midi.models import Midi


class MidiModelTest(TestCase):
    def test_string_representation(self):
        midi = Midi(title='foo')
        self.assertEqual(str(midi), 'foo')
