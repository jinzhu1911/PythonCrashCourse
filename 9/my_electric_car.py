# 在一个模块中存储多个类
# from electric_car import ElectricCar
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


# 从一个模块中导入多个类
# from electric_car import Car, ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


# 导入整个模块
import electric_car

my_beetle = electric_car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'beetle', 2016)
print(my_tesla.get_descriptive_name())