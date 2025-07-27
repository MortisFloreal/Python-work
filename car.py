class Car():
    '''Модель автомобиля'''

    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 35

    def get_descriptive_name(self):
        '''Форматированное описание'''
        bio = f'year {self.year} model {self.model} make {self.make}'
        return bio.title()
    
    def read_odometer(self):
        '''Выводит пробег машины в милях'''
        print(f'Пробег у {self.model} = {self.odometer_reading}')

    def updaate_odometer(self, mileage):
        '''Устанавливает заданное значение на одометре при попытке скрутить
        одометер посылает куда по дальше'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('пшел нах, пробег он собрался скрутить')
    
    def increment_odometer(self,miles):
        '''Увеличивает показания одометра
        с заданным приращением'''

        if miles >= self.odometer_reading:
          self.odometer_reading += miles
        else:
            print('Значение одометра отрицательное')


'''Экземпляр и методs'''
car = Car('audi', 'a4', 2019)  
print(car.get_descriptive_name())

car.updaate_odometer(36)
car.read_odometer()

car.increment_odometer(200)
car.read_odometer()