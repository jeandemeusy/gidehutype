from collections import OrderedDict
from inspect import Parameter, Signature
from typing import List

from .descriptor import Descriptor


def make_signature(names: List[str]):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)

class NoDuplicateOrderedDict(OrderedDict):
    def __setitem__(self, key: str, value):
        if key in self:
            raise NameError(f"'{key}' already defined")

        super().__setitem__(key, value)

class StructureMeta(type):
    @classmethod
    def __prepare__(cls, _, __):
        return NoDuplicateOrderedDict()
        
    def __new__(cls, clsname: str, bases, clsdict: dict):
        fields = [key for key, value in clsdict.items() if isinstance(value, Descriptor)]

        for name in fields:
            clsdict[name].name = name
        
        clsobj = super().__new__(cls, clsname, bases, dict(clsdict))

        setattr(clsobj, '__signature__', make_signature(fields))

        return clsobj 


class Structure(object, metaclass=StructureMeta):
    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)

        for name, value in bound.arguments.items():
            setattr(self, name, value)

    def __repr__(self):
        names = list(self.__dict__.keys())
        types = [type(value).__name__ for value in self.__dict__.values()]
        values = list(self.__dict__.values())

        params = [f"{k}:{t}={v}" for k, t, v in zip(names, types, values)]
        
        return f"{type(self).__name__}({', '.join(params)})"