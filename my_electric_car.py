from electric_car import ElectricCar, Car
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle = Car('vplkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())