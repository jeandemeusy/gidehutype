from gidehutype import PositiveFloat, PositiveInteger, RegexString, SizedBoolSet
from gidehutype.structure import Structure


class Stock(Structure):
    name = RegexString(pattern="[A-Z]+$")
    shares = PositiveInteger()
    price = PositiveFloat()
    sizedBool = SizedBoolSet("grault", maxlen=3)


if __name__ == '__main__':
    s = Stock('APPL', 12, 10., {True, False, True})

    s.name = "GOOGL"
    print(s.sizedBool)