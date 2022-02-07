class Engine:
    def __init__(self, power: int, torque : int, volume : float) -> None:
        self.power = power # потужність
        self.torque = torque # крутний момент
        self.volume = volume # об'єм двигуна

class Driver:
    def __init__(self, name: str, licence: bool):
        self.name = name  # ім'я водія
        self.licence = licence # наявність водійського посвідчення

    def driveCool(self):
        if self.licence == True:
            print("Вжжжжжжж!")
        else:
            print("Я не маю посвідчення, щоб робити Вжжжжжжж!")

class Car:
    def __init__(self):
        self.engine = Engine(150, 200, 2)

    def go(self, driver : Driver):
            driver.driveCool()

driver = Driver("Петренко", False)
car = Car()
car.go(driver)









