#!/bin/python3

"""This is a script meant to restart the relay
container with newly found microcontrollers

It uses udev to find new devices

Depends on libudev"""


import pyudev
import docker
from time import sleep

ctx = pyudev.Context()

monitor = pyudev.Monitor.from_netlink(ctx)

monitor.filter_by("tty")


devices = []  # will be in mode /dev/ttyACM0:/dev/ttyACM0 for each device
volumes = ["/dev/bus/usb:/dev/bus/usb",
           "/dev/serial:/dev/serial"]

dclient = docker.from_env()
cont = dclient.containers.get('tinyml-mcu-bridge-1')

failed_serial = None

for device in iter(monitor.poll, None):
    # if wanted device, add/remove from devices list
    if device.get('ID_VENDOR') != 'Arduino':
        continue
    if device.get('ACTION') == 'add':
        serial = device.get('ID_USB_SERIAL_SHORT')

        if serial[0] == '0':
            failed_serial = serial
            continue
        port = device.get('DEVNAME') + ':' + device.get('DEVNAME')
        devices.append(port)

        cont.commit("relay-new", "latest")
        cont.stop()
        cont.remove()
        cont = dclient.containers.run("relay-new",
                                      devices=devices,
                                      ports={'8080/tcp': 5000},
                                      runtime='sysbox-runc',
                                      volumes=volumes,
                                      detach=True,
                                      name='tinyml-mcu-bridge-1')
        print("Container successfully restarted with new device")

    elif device.get('ACTION') == 'remove':
        if failed_serial is not None:
            if device.get('ID_USB_SERIAL_SHORT') in failed_serial:
                failed_serial = None
                continue
        port = device.get('DEVNAME') + ':' + device.get('DEVNAME')
        try:
            devices.remove(port)
        except ValueError:
            pass

        cont.commit("relay-new", "latest")
        cont.stop()
        cont.remove()
        cont = dclient.containers.run("relay-new",
                                      devices=devices,
                                      ports={'8080/tcp': 5000},
                                      runtime='sysbox-runc',
                                      volumes=volumes,
                                      detach=True,
                                      name='tinyml-mcu-bridge-1')
        print("Device has been successfully removed from container")
