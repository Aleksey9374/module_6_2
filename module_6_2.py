class Vehicle: # это любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner#(str) # владелец транспорта. (владелец может меняться)
        self.__model = __model#(str) # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power#(int)# мощность двигателя. (не можем менять самостоятельно)
        self.__color = __color#(str)# название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self): # возвращает строку: "Модель: <название модели транспорта>"
        return f'Модель: {self.__model}'

    def get_horsepower(self):  # возвращает строку: "Мощность двигателя: <мощность>"
        return f'Мощность двигателя:  {self.__engine_power}'

    def get_color(self):  # возвращает строку: "Цвет: <цвет транспорта>"
        return f'Цвет:  {self.__color}'

    def print_info(self):
        print(f'{Vehicle.get_model(self)}\n{Vehicle.get_horsepower(self)}'
              f'\n{Vehicle.get_color(self)}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle): # (седан) - наследник класса Vehicle
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()