import pytest 
from converter.converter_calculations import convert

# Basic conversions
def test_km_to_miles():
    assert convert(1, "km", "miles") == 0.6214

def test_miles_to_km():
    assert convert(1, "miles", "km") == 1.6093

def test_kg_to_lbs():
    assert convert(1, "kg", "lbs") == 2.2046

def test_c_to_f():
    assert convert(0, "c", "f") == 32.0


    # Edge cases
def test_same_unit_returns_value():
    assert convert(100, "km", "km") == 100

def test_zero_value():
    assert convert(0, "km", "miles") == 0.0


    # Errors
def test_unsupported_conversion_raises_error():
    with pytest.raises(ValueError):
        convert(1, "km", "lbs")