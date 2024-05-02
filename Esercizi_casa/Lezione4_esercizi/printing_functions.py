# 8-15. Printing Models

def make_car(manufacturer: str, model: str, color: str = None, tow_package: bool = None) -> dict[str, str | bool]:
    car: dict[str, str | bool] = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    if color:
        car['color'] = color
    if tow_package is not None:
        car['tow_package'] = tow_package
    return car
