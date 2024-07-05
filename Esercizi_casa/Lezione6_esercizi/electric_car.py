# 9-9. Battery Upgrade

class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

class ElectricCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.battery = Battery()

    def get_range(self):
        if self.battery.battery_size == 70:
            range_miles = 240
        elif self.battery.battery_size == 85:
            range_miles = 270
        else:
            range_miles = 200  # Default value for other battery sizes
        return range_miles

my_electric_car = ElectricCar("Tesla", "Model S")
print(f"Initial Range: {my_electric_car.get_range()} miles")

my_electric_car.battery.upgrade_battery()
print(f"Updated Range: {my_electric_car.get_range()} miles")