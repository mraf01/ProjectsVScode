# 8-15. Printing Models

from printing_functions import make_car

car: dict[str, str | bool] = make_car('subaru', 'outback', color='blue', tow_package=True)
print(f"Car: {car}")
