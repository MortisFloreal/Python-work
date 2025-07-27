class Car():
    '''Простая модель автомобиля'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'miles {self.odometer_reading}')
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('error')
    
    def increment_odometer(self,miles):
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print('error')

class Battery():

    def __init__(self, battery_size=75):
        self.battery_size = battery_size
  
    def describe_battery(self):
        print(f'{self.battery_size}-kwh battery')
    '''Выводит приблизительный хапас хода'''
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'{range} miles приблизительный запас хода')
    

class ElectricCar(Car):
    '''Представляет аспекты машин специфиеческие для эдектромобилей'''
    def __init__(self,make,model,year):
        '''Инициализирует атрибуты класса-родителя'''
        super().__init__(make,model,year)
        self.battery = Battery()

    def describe_battery(self):
        print(f'{self.battery_size}-kWh battery')


             
        