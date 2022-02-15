class Pet:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print("Моє ім'я - ", self.name)

    def voice(self):
        print("Я базовий клас, я нічого не можу говорити, я не знаю, хто я такий!")


class Cat(Pet):
    def voice(self):
        print("Miu-miu!")


class Dog(Pet):
    def voice(self):
        print("Bau-bau!")


class Parrot(Pet):
    def __init__(self, name, pawNumber):
        super().__init__(name)
        # Pet.__init__(self, name)
        self.pawNumber = pawNumber

    def voice(self):
        print(self.name, "хороший!")


if __name__ == "__main__":
    parrot = Parrot("Флінт", 2)
    parrot.showName()

    # myHomeZoo = [Cat("Кузя"),
    #              Dog("Шарік"),
    #              Parrot("Флінт"),
    #              Pet("Чебурашка")]
    #
    # for pet in myHomeZoo:
    #     pet.showName()
    #     pet.voice()


