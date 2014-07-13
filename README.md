nitwo-relay-python-client
=========================

A Python client interface for NiTwo WiFi relay board.

One day I purchased a 16-channel relay board made by NiTwo.
I wanted to use it in automation, so I reverse-engineered the software
and wrote a primitive Python class which is used in my applications to
communicate with the board.
I'm leaving it here (under a Public Domain license) with hope it will be useful for you.


How to use it
=============

```
# clone this repo
$ git clone https://github.com/vdmit11/nitwo_relay_python_client.git

# run a Python3 interpreter (only Python3, no compatibility with Python2, sorry for that)
$ python3

# import the RemoteRelayModule class and instanciate it
>>> from nitwo_relay_python_client.remote_relay_module import RemoteRelayModule
>>> m = RemoteRelayModule()

# set address and port of the board
>>> m.host = "192.168.1.2"
>>> m.port = 8080

# ok, now we can try to turn the relays on and off and get their state
# if an operation was unsuccessfull, you will get an exception

# turn on and off the 1st relay:
>>> m.turn_on(1)
>>> m.turn_off(1)



# Check whether a relay is turned on with a .is_turned_on() method: 

>>> m.is_turned_on(16)
False

>>> m.turn_on(16)
>>> m.is_turned_on(16)
True

>>> m.turn_off(16)
>>> m.is_turned_on(16)
False



# You can poll the board via the .refresh() methot to obtain a fresh information
# about the relay states. That is necessary when multiple clients are working with
# a board simultaneously.
>>> m.refresh()
>>> m.is_turned_on(16)
True
```
