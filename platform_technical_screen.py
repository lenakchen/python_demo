

def sort(width, height, length, mass) -> str:
    """
    Sort the packages using the following criteria:

    - A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
    - A package is heavy when its mass is greater or equal to 20 kg.

    Dispatch the packages in the following stacks:
    - STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.
    - SPECIAL: packages that are either heavy or bulky can't be handled automatically.
    - REJECTED: packages that are **both** heavy and bulky are rejected.


    :param width: width of the package, unit in centimeters, must be > 0
    :param height: height of the package, unit in centimeters, must be > 0
    :param length: length of the package, unit in centimeters, must be > 0
    :param mass: weight of the package, unit in kilograms, must be > 0
    :return: name of the stack that package should go
    """
    assert width > 0, "Package width must be > 0"
    assert height > 0, "Package height must be > 0"
    assert length > 0, "Package length must be > 0"
    assert mass > 0, "Package mass must be > 0"
    bulky = 0
    heavy = 0
    volume = width * height * length
    if volume >= 1000000 or any([width>=150, height>=150, length>=150]):
        bulky = 1
    if mass >= 20:
        heavy = 1
    if bulky and heavy:
        return "REJECTED"
    elif bulky==0 and heavy==0:
        return "STANDARD"
    else:
        return "SPECIAL"


