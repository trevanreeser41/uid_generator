# Assignment: UID

As the team lead for a new corporate system, you've decided the standard UUID (universally unique id) format creates numbers too large (256 bit). Instead, you want to follow the Instagram UID model and create 63-bit numbers -- the signed BIGINT size in many relational databases. Using 63 bits, the maximum integer is 2^63: 9,223,372,036,854,775,807. The benefit and drawback of these IDs is they encode when and where they were created.

As a unique ID, the UID must be unique in both space and time to allow any computer to create unique IDs in soluation -- without having to verify uniqueness with any other ocmputer. To this purpose, you'll assign the 63 bits as follows:

|                | Time Component                 | Counter Component                         | Space Component                                                            |
|----------------|--------------------------------|-------------------------------------------|----------------------------------------------------------------------------|
| Number of Bits | 42 bits                        | 13 bits                                   | 8 bits                                                                     |
| Description    | Milliseconds since Jan, 1970   | Counter (allows more than one UID per ms) | Shard ID (assigned explicitly to a server, process, or database)           |
| Maximum Value  | 4,398,046,511,104 (May, 2109)  | 8,192 per ms                              | 256 unique locations                                                       |

* *millis*: 42 bits gives us 4,398,046,511,104 milliseconds, or 139 years after the Unix epoch time of January 1, 1970: `(2^42) - 1 + 1970 == 4,398,046,511,104 ms + 1970 == May, 2109`. Milliseconds is the first component so these ids automatically sort by time.
* counter: 13 bits gives us 8,192 possible ids per millisecond per shard.
* shard id: 8 bits gives us 256 possible shards, which represent unique database instances, web server instances, etc.

To save space in writing these IDs, your program should convert them to different bases. The following bases need to be supported: 2, 10, 16, 58, and 64.

| Base | Max Value                                                       | Num of Characters | Alphabet                                                                    |
|------|-----------------------------------------------------------------|-------------------|-----------------------------------------------------------------------------|
| 2    | 111111111111111111111111111111111111111111111111111111111111111 | 63                | 01                                                                          |
| 10   | 9223372036854775807                                             | 19                | 0123456789                                                                  |
| 16   | 7fffffffffffffff                                                | 16                | 0123456789ABCDEF                                                            |
| 58   | NQm6nKp8qFC                                                     | 11                | 123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz (not used: 0OIl) |
| 64   |                                                                 |                   | 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_            |

    Note that the Base 64 conversion is NOT Base64 encoding. Our algorithm needs to do a math-related number base conversion using the given alphabet.


## Package Directory Structure

Create the following project structure with the names given.  Function names are given within each file:
```
project/
    uid/
        __init__.py
            # import package-level items (optional)

        uid.py
            SHARD_ID = 1                # range is 0-255
            def generate(base=10):
                '''Generates a uid with the given base'''
                # create variables: millis and counter
                # verify that we don't use up all the counters within the same millisecond
                uid = pack(millis, counter, SHARD_ID)
                # convert uid to the right base
                return uid

            def pack(millis, counter, shard):
                '''Combines the three items into a single uid number'''
                # bit shift to combine the three
                # think in binary here!
                return uid

            def unpack(uid)
                '''Separates the uid into its three parts'''
                # bit shift to separate the three parts
                # think in binary here!
                return (millis, counter, shard)

        base2.py
            def convert(val):
                '''Converts the given base-10 integer to a string of base-2 chars'''
                # base10 -> base2
                return b2val

            def invert(b2val):
                '''Converts the given string of base-2 chars to a base-10 integer'''
                # base2 -> base10
                return val

        base16.py
            def convert(val):
                '''Converts the given base-10 integer to a string of base-16 chars'''
                # base10 -> base16
                return b16val

            def invert(b16val):
                '''Converts the given string of base-2 chars to a base-10 integer'''
                # base16 -> base10
                return val

        base58.py
            def convert(val):
                '''Converts the given base-10 integer to a string of base-58 chars'''
                # base10 -> base58
                return b58val

            def invert(b58val):
                '''Converts the given string of base-58 chars to a base-10 integer'''
                # base58 -> base10
                return val

        base64.py
            def convert(val):
                '''Converts the given base-10 integer to a string of base-64 chars'''
                # base10 -> base64
                return b64val

            def invert(b64val):
                '''Converts the given string of base-64 chars to a base-10 integer'''
                # base64 -> base10
                return val

        profileit.py
            # create many thousands of UIDs in various bases and print profile stats


    tests/
        # one or more python unittest files

        test_baseX.py
            # should contain a unittest.TestCase class

```



## Submitting the Assignment

Submit via the Grading Engine. You can submit up to three times; your highest grade will be entered into the gradebook on Learning Suite.

The grading engine will create at least two processes, so be sure to try with different SHARD_ID values.
