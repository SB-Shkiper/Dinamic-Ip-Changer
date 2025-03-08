# Dinamic-Ip-Changer
This is a project for educational practice that has simple functionality for dynamically changing IP using Tor.

There is a more advanced analogue ([TorNet](https://github.com/ByteBreach/tornet)).
# How the script works
After launch, the script takes the necessary values ​​from the config.txt file and immediately starts working.
# Config file values
Count=0 - Number of IP changes (if the value is 0, the change will be infinite until the script is disabled)

Interval=5 - Time between IP changes

ControllerPort=9050 - Tor controller port (Can be taken from the torrc config file of your Tor, under the value "ControlPort")

P.S. If there is no "ControlPort" in torrc, you must add it manually, for example "ControlPort 9050"
# How to connect to the script
To connect to a browser example, you need to select the Socks5 proxy in the connection settings, enter the value localhost (127.0.0.1) in the address field and the value coming after “SocksPort” in torrc in the port field.

P.S. If "SocksPort" is not there, you also need to add it manually, for example "SocksPort 5091".
