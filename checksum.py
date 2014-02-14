"""
A set of tools for working with simple one-byte (modulo-256) checksums.
"""

def calculate(buffer):
    """Calculate modulo-256 sum of all bytes in a buffer (a byte string or array).
    Works with any kind of lists (produces a modulo-256 sum of all elements).

    >>> calculate(b"\x01\x02\x03\x04\x05")
    15

    >>> calculate(bytearray.fromhex("22 01 10 00 00 AA AA"))
    135

    >>> calculate([256, 512, 1024, 1])
    1

    >>> calculate(b"")
    0
    """
    return sum(buffer) & 0xFF


def is_valid(buffer):
    """Return true if checksum at the end of a buffer is valid
    (i.e. matches to the sum of all bytes in the buffer except the last one).

    >>> is_valid(bytearray.fromhex("55 02 12 00 00 00 01 6A"))
    True

    >>> is_valid(bytearray.fromhex("55 02 12 00 00 00 01 69"))
    False

    >>> is_valid(bytes.fromhex("00"))
    True

    >>> is_valid(b"")
    True

    >>> is_valid([512, 32768, 0])
    True
    """
    return (len(buffer) == 0) or (buffer[-1] == calculate(buffer[0:-1]))
    

def append_to(buffer):
    """Calculate modulo-256 sum of all bytes in a given byte array
    and append the checksum to the end of the array.

    >>> buffer =  bytearray.fromhex("55 01 12 00 00 00 10")
    >>> append_to(buffer)
    >>> buffer == bytearray.fromhex("55 01 12 00 00 00 10 78")
    True

    >>> buffer = bytearray()
    >>> append_to(buffer)
    >>> buffer == bytearray.fromhex('00')
    True
    """
    buffer.append(calculate(buffer))



if __name__ == "__main__":
    import doctest
    doctest.testmod()
