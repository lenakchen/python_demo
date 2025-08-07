

def sort(width, height, length, mass) -> str:
    """
    :param width: width of the package, unit in centimeters
    :param height: height of the package, unit in centimeters
    :param length: length of the package, unit in centimeters
    :param mass: weight of the package, unit in kilograms
    :return: name of the stack that package should go
    """
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


