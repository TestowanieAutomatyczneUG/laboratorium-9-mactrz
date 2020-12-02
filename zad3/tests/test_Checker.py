import unittest
from unittest.mock import *
from  src.sample.Checker import Checker

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.tmp = Checker()

    def test_remainder_not_played(self):
        file = 'test.mp3'
        self.tmp.tmp.getTime = Mock(name='getTime')
        self.tmp.tmp.getTime.return_value = 16
        self.tmp.tmp.resetWav = Mock(name='resetWav')
        self.tmp.tmp.playWavFile = Mock()
        self.tmp.tmp.resetWav.return_value = False
        result = self.tmp.remainder(file)
        self.assertEqual(result, False)

    def test_remainder_played(self):
        file = 'test.mp3'
        self.tmp.tmp.getTime = Mock(name= "getTime")
        self.tmp.tmp.playWavFile = Mock(name="playWavFile")
        self.tmp.tmp.wavWasPlayed = Mock(name="wavWasPlayed")

        self.tmp.tmp.getTime.return_value = 18
        self.tmp.tmp.wavWasPlayed.return_value = True
        self.tmp.tmp.playWavFile.return_value = self.tmp.tmp.wavWasPlayed()

        result = self.tmp.remainder(file)
        self.assertEqual(result, True)