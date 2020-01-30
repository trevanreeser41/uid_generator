#!/usr/bin/env python3

import base2, base16, base58, time

##############################################################################################################################################################################
#  A uid class based on time, counter, and shard id.                                                                                                                         #
#                                                                                                                                                                            #
# |                | Time Component                 | Counter Component                         | Space Component                                                            |
# |----------------|--------------------------------|-------------------------------------------|----------------------------------------------------------------------------|
# | Number of Bits | 42 bits                        | 13 bits                                   | 8 bits                                                                     |
# | Description    | Milliseconds since Jan, 1970   | Counter (allows more than one UID per ms) | Shard ID (assigned explicitly to a server, process, or database)           |
# | Maximum Value  | 4,398,046,511,104 (May, 2109)  | 8,192 per ms                              | 256 unique locations                                                       |

# space = mac address || shard id || IP address
# time = milliseconds
# counter = 1-64000 developed per millisecond per computer
# guaranteed to never conflict with anyone on another system

# range is 0-255
SHARD_ID = 1

# sizes
MILLIS_BITS = 42
COUNTER_BITS = 13
SHARD_BITS = 8

# the masks
MILLIS_MASK = 21
COUNTER_MASK = 8
SHARD_MASK = 0

LAST_MILLIS = 0
COUNTER = 0

def generate(base=10):
    '''Generates a uid with the given base'''
    global LAST_MILLIS
    global COUNTER

    # get the millisecond, waiting if needed if we've hit the max counter
    # reset the counter if we are in a new millisecond

    if LAST_MILLIS != int(round(time.time() * 1000)):
        LAST_MILLIS = int(round(time.time() * 1000))
        COUNTER = 0

    while LAST_MILLIS == int(round(time.time() * 1000)):
        #INCREMENT COUNTER
        COUNTER = COUNTER + 1
        if COUNTER>8192:
            #DO NOTHING AS THE WAIT
            print('Duplicate')

    # pack it up and convert base
    uid = pack(LAST_MILLIS, COUNTER, SHARD_ID)
    
    # print("b2 conversion:" + str(base2.convert(uid)))
    # print("b16 conversion:" + str(base16.convert(uid)))
    # print("b58 conversion:" + str(base58.convert(uid)))

    # print("b2 inversion:" + str(base2.invert(base2.convert(uid))))
    # print("b16 inversion:" + str(base16.invert(base16.convert(uid))))
    # print("b58 inversion:" + str(base58.invert(base58.convert(uid))))
    print("uid:" + str(uid))
    
    return uid


def pack(millis, counter, shard):
    '''Combines the three items into a single uid number'''
    millis_shifted = millis<<21
    counter_shifted = counter<<8
    uid = (millis_shifted | counter_shifted | shard)
    return uid


def unpack(uid):
    '''Separates the uid into its three parts'''
    millis = uid >> MILLIS_MASK
    counter = uid >> COUNTER_MASK & ((1 << 0b1101) - 1)
    shard = uid >> SHARD_MASK & 0xFF
    return (millis, counter, shard)
