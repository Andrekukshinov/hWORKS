from numpy import void


class IPhone:

    def __init__(self, id, surname, name,
                 secondName, address, ccNumber,
                 debit, credit, inCountryTimeCallings, internationalTimeCallings):
        self.__id__ = id
        self.__surname__ = surname
        self.__name__ = name
        self.__secondName__ = secondName
        self.__address__ = address
        self.__ccNumber__ = ccNumber
        self.__debit__ = debit
        self.__credit__ = credit
        self.__inCountryTimeCallings__ = inCountryTimeCallings
        self.__internationalTimeCallings__ = internationalTimeCallings

    def getId(self) -> int:
        return self.__id__

    def setId(self, id):
        self.__id__ = id

    def getSurname(self) -> str:
        return self.__surname__

    def setSurname(self, surname):
        self.__surname__ = surname

    def getName(self) -> str:
        return self.__name__

    def setName(self, name):
        self.__name__ = name

    def getSecondName(self) -> str:
        return self.__secondName__

    def setSecondName(self, secondName):
        self.__secondName__ = secondName

    def getAddress(self) -> str:
        return self.__address__

    def setAddress(self, address):
        self.__address__ = address

    def getCcNumber(self) -> str:
        return self.__ccNumber__

    def setCcNumber(self, ccNumber):
        self.__ccNumber__ = ccNumber

    def getDebit(self) -> float:
        return self.__debit__

    def setDebit(self, debit):
        self.__debit__ = debit

    def getCredit(self) -> float:
        return self.__credit__

    def setCredit(self, credit):
        self.__credit__ = credit

    def getInCountryCalligsTime(self) -> float:
        return self.__inCountryTimeCallings__

    def setInCountryCalligsTime(self, inCountryTimeCallings):
        self.__inCountryTimeCallings__ = inCountryTimeCallings

    def getInternationalCallingsTime(self) -> float:
        return self.__internationalTimeCallings__

    def setInternationalCallingsTime(self, internationalTimeCallings):
        self.__internationalTimeCallings__ = internationalTimeCallings

    def __eq__(self, other) -> bool:
        return self.__id__ == other.__id__ \
               and self.__name__ == other.__name__ \
               and self.__surname__ == other.__surname__ \
               and self.__secondName__ == other.__secondName__ \
               and self.__address__ == other.__address \
               and self.__ccNumber__ == other.__ccNumber__ \
               and self.__debit__ == other.__debit__ \
               and self.__credit__ == other.__credit__ \
               and self.__inCountryTimeCallings__ == other.__inCountryTimeCallings__ \
               and self.__internationalTimeCallings__ == other.__internationalTimeCallings__

    def __ne__(self, other) -> bool:
        return not (__eq__(other))

    def __str__(self) -> str:
        return ("id " + str(self.__id__) + " surname " + str(self.__surname__) +
                " name " + str(self.__name__) + " secondName " + str(self.__secondName__) +
                " address " + str(self.__address__) + " ccNumber " + str(self.__ccNumber__) +
                " debit " + str(self.__debit__) + " credit " + str(self.__credit__) +
                " inCountryTimeCallings " + str(self.__inCountryTimeCallings__)
                + " internationalTimeCallings " + str(self.__internationalTimeCallings__)
                )


class NoSuchSubscriberException(Exception):
    pass


class PhoneOperator:

    def __init__(self, subs):
        self.__subscribers__ = subs

    def getSubscribers(self):
        return self.__subscribers__

    def addSubscriber(self, subscriber):
        self.__subscribers__.append(subscriber)

    # todo remove sub

    def getSubscriberBalance(self, subscriber) -> float:
        result = -1
        try:
            result = self.__subscribers__.index(subscriber)
        except ValueError:
            raise NoSuchSubscriberException("No such subscriber available, try again")
        print(subscriber)
        return subscriber.getDebit() - subscriber.getCredit()

    def getAllSubscribersInCountryCallTimeAbove(self, time) -> list:
        result = []
        for sub in self.__subscribers__:
            callings_time = sub.getInCountryCalligsTime()
            if callings_time > time:
                result.append(sub)
        return result

    def getAllSubscribersWithInternationalCalls(self) -> list:
        result = []
        for sub in self.__subscribers__:
            callings_time = sub.getInternationalCallingsTime()
            if callings_time > 0:
                result.append(sub)
        return result


def run() -> None:
    sub1 = IPhone(1, "Harrington", "Billy", "Boss", "Nico nico doga", "12234245235213", 300, 48, 3000, 56)
    sub2 = IPhone(2, "Darkholme", "Van", "Of", "Nico nico doga", "1223424543235213", 300, 148, 30, 5)
    sub3 = IPhone(3, "Sins", "Johny", "The", "Brothers", "89234245235213", 300, 48, 3000, 0)
    sub4 = IPhone(4, "Johny", "Rambo", "Gym", "Let's celebrate", "12234245235213", 20, 300, 0, 0)
    sub5 = IPhone(5, "Carry", "Don", "Carlione", "Italy", "666", 666, 666, 3000, 56)
    sub6 = IPhone(6, "Milos", "Ricardo", "Flex", "Nico nico doga", "12234245235213", 300, 48, 300, 560)
    sub7 = IPhone(7, "Carl", "John", "Boss", "Nico nico doga", "12234245235213", 3009, 48, 300, 56)

    subs = [sub1, sub7, sub6, sub5, sub4, sub3, sub2]

    phoneOperator = PhoneOperator(subs)

    print(str(phoneOperator.getSubscriberBalance(sub4)))

    print("\n")

    international_calls = phoneOperator.getAllSubscribersWithInternationalCalls()

    for sub in international_calls:
        print(str(sub) + " ")

    print("\n")

    country_call_time_above = phoneOperator.getAllSubscribersInCountryCallTimeAbove(300)
    for sub in country_call_time_above:
        print(str(sub) + " ")


run()
