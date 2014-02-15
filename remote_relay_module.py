"""
An interface for controlling a NiTwo 16-relay Wi-Fi module.

>>> module = RemoteRelayModule()

>>> module.turn_off(1)
>>> module.is_turned_on(1)
False

>>> module.turn_on(1)
>>> module.is_turned_on(1)
True

>>> module.turn_off(1)
>>> module.is_turned_on(1)
False

>>> module.is_turned_on(16)
False

>>> module.turn_on(16)
>>> module.is_turned_on(16)
True

>>> module.turn_off(16)
>>> module.is_turned_on(16)
False

>>> import time
>>> for index in range(module.NUMBER_OF_RELAYS):
...     relay_number = index + 1
...     module.turn_on(relay_number)
...     time.sleep(0.1)
...     module.turn_off(relay_number)
...     time.sleep(0.1)
"""

import protocol
import socket


class RemoteRelayModule:
    MODULE_NUMBER = 1
    NUMBER_OF_RELAYS = 16
    host = "192.168.1.240"
    port = 8080
    timeout_in_seconds = 1

    relay_states = []

    def __init__(self):
        self.refresh()
    
    def refresh(self):
        response = self.send_message(protocol.pack_get_status_request(), True)
        self.relay_states = protocol.unpack_get_status_response(response)

    def turn_on(self, relay_number):
        self.send_message(protocol.pack_turn_on_request(relay_number))
        self.refresh()

    def turn_off(self, relay_number):
        self.send_message(protocol.pack_turn_off_request(relay_number))
        self.refresh()

    def is_turned_on(self, relay_number):
        return self.relay_states[relay_number - 1]
        
    def send_message(self, buffer, wait_for_response=False):
        def attempt_to_send_message():            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout_in_seconds)
                s.connect((self.host, self.port))
                s.send(buffer)
                if (wait_for_response):
                    return s.recv(len(buffer))
        def retry_on_exception(function, exceptions, attempts):
            for attempt in range(attempts):
                try:
                    return function()
                except exceptions:
                    pass
                else:
                    break
        return retry_on_exception(
            attempt_to_send_message,
            (socket.timeout, protocol.InvalidChecksumException),
            attempts=2
        )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
