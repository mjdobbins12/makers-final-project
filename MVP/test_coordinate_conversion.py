import pytest
import coordinate_conversion

class TestConvert:

        def test_convert_coordinates(self):
            convert = coordinate_conversion.Convert()
            assert convert.coordinates('a1','a2') == [7, 0, 6, 0]
            assert convert.coordinates('a7','c5') == [1, 0, 3, 2]

        def test_convert_errors(self):
            convert = coordinate_conversion.Convert()
            assert convert.coordinates('xx','') == [0, 0, 7, 7]
            assert convert.coordinates('aaaaa','a99') == [0, 0, 7, 7]
            assert convert.coordinates('','') == [0, 0, 7, 7]
