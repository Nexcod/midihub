from django.test import TestCase

from app.models import Midi


class MidiModelTest(TestCase):
    def test_string_representation(self):
        midi = Midi(title='foo')
        self.assertEqual(str(midi), 'foo')
