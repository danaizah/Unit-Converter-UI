CONVERSIONS = {
        ("km", "miles"): lambda x: x * 0.621371,
        ("miles", "km"): lambda x: x * 1.60934,
        ("kg", "lbs"):   lambda x: x * 2.20462,
        ("lbs", "kg"):   lambda x: x * 0.453592,
        ("c", "f"):      lambda x: (x * 9/5) + 32,
        ("f", "c"):      lambda x: (x - 32) * 5/9,
    }


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a numeric value from one unit to another.

    Args:
        value (float): The numeric value to convert.
        from_unit (str): The source unit.
        to_unit (str): The target unit.

    Raises:
        ValueError: If the units are unsupported or incompatible.

    Returns:
        float: The converted value.
    """
    
    if from_unit == to_unit:
        return value
    key = (from_unit.lower(), to_unit.lower())
    if key not in CONVERSIONS:
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
    return round(CONVERSIONS[key](value), 4)