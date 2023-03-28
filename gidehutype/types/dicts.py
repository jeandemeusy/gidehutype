from ..checkings import Typed, Sized
from . import export

@export
class Dict(Typed):
    expected_type = dict

@export
class SizedDict(Dict, Sized):
    pass