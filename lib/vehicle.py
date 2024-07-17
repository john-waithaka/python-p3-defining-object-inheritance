# class Vehicle:
#     pass


class Vehicle:

    def __init__(self, wheel_size=22, wheel_number=18):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"

my_vehicle = Vehicle()


print(my_vehicle.wheel_size)       # Output: 22
print(my_vehicle.wheel_number)     # Output: 18

# Calling methods
print(my_vehicle.go())             # Output: vrrrrrrrooom!
print(my_vehicle.fill_up_tank()) 