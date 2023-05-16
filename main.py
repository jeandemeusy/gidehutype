from gidehutype import PositiveFloat, PositiveInteger, RegexString, SizedFloatList
from gidehutype.structure import Structure


class Stock(Structure):
    name = RegexString(pattern="[A-Z]+$")
    shares = PositiveInteger()
    price = PositiveFloat()
    foo = SizedFloatList(maxlen=2)


if __name__ == '__main__':
    try:
        s = Stock("appl", -2, 10., [1., 2., 3.])
    except TypeError as e:
        print("!TypeError!", e)
    except ValueError as e:
        print("!ValueError!", e)
    else:
        print(f"{s.name=}")
        print(f"{s.shares=}")
        print(f"{s.price=}")
        print(f"{s.foo=}")


        
