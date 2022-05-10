from abc import ABCMeta, abstractmethod


class MilitaryObject(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def accept(self, spy):
        pass


class GeneralStaff(MilitaryObject):
    def __init__(self, name, generals, secretPaper):
        super().__init__(name)
        self.generals = generals
        self.secretPaper = secretPaper

    def __str__(self):
        return f"GeneralStaff: У генеральному штабі є {self.generals} геренералів та {self.secretPaper} секретних паперів."

    def accept(self, spy):
        spy.visitGeneralStaff(self)


class MilitaryBase(MilitaryObject):
    def __init__(self, name, officers, soldiers, jeeps, tanks):
        super().__init__(name)
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        return f"MilitaryBase: На військовій базі є {self.officers} офіцерів, {self.soldiers} солдатів, {self.jeeps} джипів та {self.tanks} танків."

    def accept(self, spy):
        spy.visitMilitaryBase(self)


class Spy(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Шпигун: {self.name}\n"

    @abstractmethod
    def visitGeneralStaff(self, generalStaff):
        pass

    @abstractmethod
    def visitMilitaryBase(self, militaryBase):
        pass

class SecretAgent(Spy):

    def __init__(self, name):
        super().__init__(name)
        self.information = ""

    def __str__(self):
        return super().__str__() + f"information = {self.information}\n"

    def visitGeneralStaff(self, generalStaff):
        self.information += f"{generalStaff.name}:\n" \
                            f"генералів: {generalStaff.generals}\n" \
                            f"секретних паперів: {generalStaff.secretPaper}\n"

    def visitMilitaryBase(self, militaryBase):
        self.information += f"{militaryBase.name}:\n" \
                            f"офіцерів: {militaryBase.officers}\n" \
                            f"солдатів: {militaryBase.soldiers}\n" \
                            f"джипів  : {militaryBase.jeeps}\n" \
                            f"танків  : {militaryBase.tanks}\n"

class Saboter(Spy):
    def __str__(self):
        return super().__str__() + "Усіх вбью, один лишуся!"

    def visitGeneralStaff(self, generalStaff):
        generalStaff.generals = 0
        generalStaff.secretPaper = 0

    def visitMilitaryBase(self, militaryBase):
        militaryBase.officers = 0
        militaryBase.soldiers = 0
        militaryBase.jeeps = 0
        militaryBase.tanks = 0


if __name__ == '__main__':
    generalStaff = GeneralStaff("Пентагон", 20, 100)
    print(generalStaff)

    militaryBase = MilitaryBase("Перл Харбор", 10, 1000, 300, 20)
    print(militaryBase)

    JamesBond = SecretAgent("James Bond")
    generalStaff.accept(JamesBond)
    print(JamesBond)

    militaryBase.accept(JamesBond)
    print(JamesBond)

    Rambo = Saboter("Rambo")
    print(Rambo)
    generalStaff.accept(Rambo)
    militaryBase.accept(Rambo)

    print(generalStaff)
    print(militaryBase)

    generalStaff.accept(JamesBond)
    print(JamesBond)