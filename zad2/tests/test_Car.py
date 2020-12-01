import unittest
from unittest.mock import *
from src.sample.Car import Car

class TestForCar(unittest.TestCase):

    def setUp(self):
        self.tmp = Car()

    def test_get_engine_temp(self):
        self.tmp.get_engine_temperature = Mock()
        self.tmp.get_engine_temperature.return_value = 100
        self.assertEqual(self.tmp.get_engine_temperature(), 100)

    @patch.object(Car, 'drive_to_destination')
    def test_drive_to_destination(self, mock_method):
        destination = 'Włocławek'
        mock_method.return_value = 'Drive to ' + destination
        result = self.tmp.drive_to_destination(destination)
        self.assertEqual(result, 'Drive to Włocławek')

    @patch.object(Car, 'needs_fuel')
    def test_needs_fuel(self, mock_method):
        mock_method.return_value = True
        result = self.tmp.needs_fuel()
        self.assertEqual(result, True)