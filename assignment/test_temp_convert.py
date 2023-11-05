import temp_convert
import unittest


class TestSys(unittest.TestCase):
    def test_temp_convert(self):
        # Test Celsius to Fahrenheit conversion
        assert temp_convert.temp_converty(1, 0) == 32.0
        assert temp_convert.temp_converty(1, 25) == 77.0
        assert temp_convert.temp_converty(1, -40) == -40.0

        # Test Fahrenheit to Celsius conversion
        assert temp_convert.temp_converty(2, 32) == 0.0
        assert temp_convert.temp_converty(2, 77) == 25.0
        assert temp_convert.temp_converty(2, -40) == -40.0


if __name__ == '__main__':
    unittest.main()
