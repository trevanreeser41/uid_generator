#!/usr/bin/env python3

class BaseXConverter(object):
    '''
    Converts positive, base-10 numbers to base-X numbers using a custom alphabet.
    The base is given by the length of the alphabet specified in the constructor.
    The first character in the alphabet has a value of zero,
    the second character a value of one, and so forth.

    Examples:
        Base2:  BaseXConverter('01')
        Base2:  BaseXConverter('<>')     # custom alphabet: < is a zero value and > is a one value
        Base4:  BaseXConverter('0123')
        Base20: BaseXConverter('0123456789abcdefghij')

    See the unit tests at the bottom of the file for many examples.
    '''

    def __init__(self, alphabet):
        '''
        The base is taken from the number of characters in the alphabet.
        '''
        self.alphabet = list(alphabet)
        self.base = len(alphabet)
        self.alphabet_index = {}

    def convert(self, val):
        '''
        Converts value from base 10 to base X.
        The return value is a baseX integer, wrapped as a string.
        '''
        if val == 0:
            return self.alphabet[0]
        arr = []
        self.base = len(self.alphabet)
        while val:
            val, rem = divmod(val, self.base)
            arr.append(self.alphabet[rem])
        arr.reverse()
        return ''.join(arr)
        
    def invert(self, bXval):
        '''
        Converts a value from base X to base 10.
        The bXval should be a baseX integer, wrapped as a string.
        Raises a ValueError if bXval contains any chars not in the alphabet.
        '''
        strlen = len(bXval)
        num = 0
        idx = 0
        for char in bXval:
            power = (strlen - (idx + 1))
            num += self.alphabet.index(char) * (self.base ** power)
            idx += 1
        return num
