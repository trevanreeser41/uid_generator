from baseX import BaseXConverter
_conv = BaseXConverter("01")

def convert(val):
    return _conv.convert(val)

def invert(bXval):
    return _conv.invert(bXval)
