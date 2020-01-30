from baseX import BaseXConverter
_conv = BaseXConverter("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")

def convert(val):
    return _conv.convert(val)

def invert(bXval):
    return _conv.invert(bXval)
