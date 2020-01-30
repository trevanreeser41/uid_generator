from baseX import BaseXConverter
_conv = BaseXConverter("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_")

def convert(val):
    return _conv.convert(val)

def invert(bXval):
    return _conv.invert(bXval)
