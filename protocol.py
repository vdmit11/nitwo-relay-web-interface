import struct
from nitwo_relay_python_client import checksum

class InvalidChecksumException(Exception):
    pass


class type:
    REQUEST = 0x55
    RESPONSE = 0x22


class action:
    TURN_ON = 0x12
    TURN_OFF = 0x11
    GET_STATUS = 0x10



def pack_message(type_code, module_number, action_code, data):
    """Pack a binary message for a NiTwo relay module.
    
    >>> message = pack_message(type.REQUEST, 1, action.TURN_ON, 16)
    >>> message == bytes.fromhex("55 01 12 00 00 00 10 78")
    True

    >>> message = pack_message(type.RESPONSE, 7, action.GET_STATUS, 0xFFFF)
    >>> message == bytes.fromhex("22 07 10 00 00 FF FF 37")
    True
    """
    message = struct.pack(">BBBI", type_code, module_number, action_code, data)
    message = bytearray(message)
    checksum.append_to(message)
    return message


def unpack_message(buffer):
    """Unpack a binary message received from a NiTwo relay module.
    
    Returns a tuple of unpacked data in the following format:
      (type_code, module_number, action_code, data).
    
    Also validates the message and raises an InvalidChecksumException if the checksum is wrong.

    >>> fields = unpack_message(bytes.fromhex("22 01 10 00 00 00 00 33"))
    >>> fields == (type.RESPONSE, 1, action.GET_STATUS, 0x0)
    True
    
    >>> fields = unpack_message(bytes.fromhex("55 03 11 00 00 00 10 79"))
    >>> fields == (type.REQUEST, 3, action.TURN_OFF, 16)
    True

    >>> unpack_message(bytes.fromhex("55 03 11 00 00 00 10 78"))
    Traceback (most recent call last):
    InvalidChecksumException: Invalid checksum of the messate: '55 03 11 00 00 00 10 78'
    """

    if (not checksum.is_valid(buffer)):
        formatted_buffer = " ".join(format(byte, "02x") for byte in buffer)
        error_message = "Invalid checksum of the messate: '" + formatted_buffer + "'"
        raise InvalidChecksumException(error_message)
    
    return struct.unpack(">BBBIB", buffer)[0:-1]
    
   
    


def pack_turn_on_request(relay_number, module_number=1):
    """Pack a 'Turn On a relay' binary message.

    >>> message = pack_turn_on_request(1)
    >>> message == bytes.fromhex("55 01 12 00 00 00 01 69")
    True

    >>> message = pack_turn_on_request(1, module_number=2)
    >>> message == bytes.fromhex("55 02 12 00 00 00 01 6A")
    True

    >>> message = pack_turn_on_request(16)
    >>> message == bytes.fromhex("55 01 12 00 00 00 10 78")
    True
    """
    return pack_message(type.REQUEST, module_number, action.TURN_ON, relay_number);



def pack_turn_off_request(relay_number, module_number=1):
    """Pack a 'Turn Off a relay' binary message.

    >>> message = pack_turn_off_request(1)
    >>> message == bytes.fromhex("55 01 11 00 00 00 01 68")
    True

    >>> message = pack_turn_off_request(1, module_number=2)
    >>> message == bytes.fromhex("55 02 11 00 00 00 01 69")
    True

    >>> message = pack_turn_off_request(16)
    >>> message ==  bytes.fromhex("55 01 11 00 00 00 10 77")
    True
    """
    return pack_message(type.REQUEST, module_number, action.TURN_OFF, relay_number);


def pack_get_status_request(module_number=1):
    """Pack a 'Get status of all relays' binary message.

    >>> message = pack_get_status_request()
    >>> message == bytes.fromhex("55 01 10 00 00 00 00 66")
    True

    >>> message = pack_get_status_request(4)
    >>> message == bytes.fromhex("55 04 10 00 00 00 00 69")
    True
    """
    return pack_message(type.REQUEST, module_number, action.GET_STATUS, 0)


def unpack_get_status_response(buffer, number_of_relays=16):
    """Unpack a 'Get status of all relays' binary message.
    Returns a list of booleans representing state of each relay in the module (True is ON, False is OFF).

    >>> unpack_get_status_response(bytes.fromhex("22 01 10 00 00 00 00 33"))
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    >>> status = unpack_get_status_response(bytes.fromhex("22 01 10 00 00 00 02 35"))
    >>> status[0]
    False
    >>> status[1]
    True

    >>> status = unpack_get_status_response(bytes.fromhex("22 01 10 00 00 FF FE 30"))
    >>> status[0]
    False
    >>> status[1]
    True
    >>> status[15]
    True
    """
    result = []
    (type, module, action, data) = unpack_message(buffer)
    for relay_index in range(0, number_of_relays):
        relay_state = bool((data >> relay_index) & 0x1)
        result.append(relay_state)
    return result
        


    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
