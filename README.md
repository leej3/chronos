# Chronos #
## README ##

### What is this repository for? ###

Chronos is a boiling/cooling water system working on Raspberry Pi. Chronos has a web interface to control the system and tracking for the state.

![Alt text](http://i.imgur.com/8II1ydG.png "A screenshot of the Chronos web interface")
### Summary of set up ###
#### Installation ####
To install the latest version Chronos from Bitbucket repo enter the following command:

`# sudo pip install git+https://bitbucket.org/quarck/chronos.git`

To install a certain version from a tag, commit or branch enter this:

`# sudo pip install git+https://bitbucket.org/quarck/chronos.git@commit|tag|branch`

#### Python packages dependencies ####

* Flask
* pyserial
* apscheduler
* pymodbus
* sqlalchemy
* python-socketio
* socketIO_client
* uwsgi

#### System dependencies ####

* nginx

#### Hardware dependencies ####

* Raspberry Pi
* USB to RS4485 adapter such as the GearMo Mini USB to RS485 / RS422 Converter FTDI CHIP
* Relay array such as the Numato 16 Channel USB Relay Module https://numato.com/product/16-channel-usb-relay-module
* Two DS18B20 temperature sensors connected to GPIO 

#### Database configuration ####

TODO
#### Deployment instructions ####

To work with shared log and access to the db file www-data and pi users have to be added in one group.
Installation script does all required actions.

#### Files locations ####

chronos log directory: `/var/log/chronos`

chronos database directory: `/home/pi/chronos_db`

chronos config path: `/etc/chronos_config.json`
#### Managing ####
Chronos has a daemon which controlled by the following command:

`# service chronos start|stop|restart`

Web UI managed by uwsgi app server:

`# service uwsgi start|stop|restart|reload chronos`

SocketIO server managing:

`# service uwsgi start|stop|restart|reload socketio_server`