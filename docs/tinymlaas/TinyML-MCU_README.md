# TinyML-MCU

Code for [TinyMLaaS](https://github.com/JeHugawa/TinyMLaaS-main) MCU devices.

# Bridge

## Dependencies

The bridge has a dependency on `usbutils`. On Debian-based systems, it can be installed with

```bash
apt install usbutils
```

## Running

### Locally

Install the python dependecies

```bash
pip install -r requirements.txt
```

There are two different ways to run the bridge locally.

First, to run a development server, run

```bash
flask --app main.py --debug run
```

For production, this is not ideal. To use waitress as production server

```bash
waitress-serve main:app
```

### Docker

The docker version of the bridge requires [nestybox/sysbox](https://github.com/nestybox/sysbox).

The provided docker-compose file looks like this

```yaml
version: '3'

services:
  bridge:
    build:
      context: .
    # If you have devices connected to the relay, add them here
    # devices:
      # - "/dev/ttyACM0:/dev/ttyACM0"
    volumes:
      - "/dev/bus/usb:/dev/bus/usb"
      - "/dev/serial:/dev/serial"
    runtime: sysbox-runc
    ports:
      - 5000:8080
```

Any microcontrollers you want to control with the bridge need to be added to the devices at this point. They also need to be connected to the computer.

If you want to add more microcontrollers to the bridge later, you can add them manually by adding them to the *docker-compose* file and restarting the container.

There is also a provided script to check for added Arduinos. The script [docker-container-restarted](./docker-container-restarter.py) automatically detects, when new arduinos are added and restart the container with the new devices. It can be run by making it executable and running it

```bash
chmod u+x docker-container-restarter.py
./docker-container-restarter.py
```

There might be problems with serial port permissions. As a solution, give permissions to the port for all users with

```bash
chmod 777 /path/to/port
```

Note that this will most likely require root priviledges.

## Serving the application to internet

### Webserver

If you already have a webserver setup, such as [Apache2](https://httpd.apache.org/) or [Nginx](https://www.nginx.com/), with which you can serve the application to the internet, add a new proxy for the bridge according to the style of the webserver.

### Port forwarding

Another way is to add a new port forwarding setting to the host machine to port 5000 in the router.

### Ngrok

However, these might not be usable by everyone. With [Ngrok](https://ngrok.com/), you can serve the bridge to the internet without having access to the local router. 

1. [Install ngrok](https://ngrok.com/download)
2. Serve the application with
```bash
ngrok http 5000
```

## Microcontrollers

There are seperate instructions for microcontrollers.

[Arduino](./arduino/README.md)
