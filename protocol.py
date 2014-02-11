from io import BytesIO



class BinaryMessageExamples:

    class GetStateWhenAllRelaysAreOff:
        request  = bytes.fromhex("55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 00 00 33")

    class GetStateWhenEightOfSixteenRelaysAreOn:
        request  = bytes.fromhex("55 01 10 00 00 00 00 66")
        request  = bytes.fromhex("22 01 10 00 00 AA AA 87")

    class GetStateWhenAllRelaysAreOn:
        request  = bytes.fromhex("55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 FF FF 31")
        
    class TurnOnRelay1:
        request  = bytes.fromhex("55 01 12 00 00 00 01 69  55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 00 01 34")

    class TurnOffRelay1:
        request  = bytes.fromhex("55 01 11 00 00 00 01 68  55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 00 00 33")

    class TurnOffRelay2:
        request  = bytes.fromhex("55 01 12 00 00 00 02 6A  55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 00 02 35")

    class TurnOffRelay2:
        request  = bytes.fromhex("55 01 11 00 00 00 02 69  55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 00 00 33")

    class TurnOnRelay3:
        request  = bytes.fromhex("55 01 12 00 00 00 03 6B  55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 00 04 37") 

    class TurnOffRelay3:
        request  = bytes.fromhex("55 01 11 00 00 00 03 6A  55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 00 00 33")

    class TurnOnRelay16:
        request  = bytes.fromhex("55 01 12 00 00 00 10 78  55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 80 00 B3")

    class TurnOffRelay16:
        request  = bytes.fromhex("55 01 11 00 00 00 10 77  55 01 10 00 00 00 00 66")
        response = bytes.fromhex("22 01 10 00 00 00 00 33")


