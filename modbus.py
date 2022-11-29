#! /usr/bin/python3
import minimalmodbus
import serial
import time
import os
import random

from paho.mqtt import client as mqtt_client
def portSetup():
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
    instrument.serial.port = '/dev/ttyUSB0'                    # this is the serial port name
    instrument.serial.baudrate = 115200         # Baud
    instrument.serial.bytesize = 8
    instrument.serial.parity   = serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout  = 0.5        # seconds

    instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
    instrument.clear_buffers_before_each_transaction = True
    print(instrument)
    return instrument

def read( pribor ):
    ## Read temperature (PV = ProcessValue) ##
    temperature = pribor.read_register(30019, 0, 4)  # Registernumber, number of decimals
    print(temperature/10)
    return temperature/10

result = os.system('echo baziliy | sudo -S chmod 666 /dev/ttyUSB0')


# echo
#     password | sudo - S
#     команда

broker = '144.21.37.118'
port = 1883
topic = "temp"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'ubuntu'
password = 'baziliy'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, t):
        msg = t
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]


def run():

    client = connect_mqtt()
    client.loop_start()
    pribor = portSetup()
    while True:
#
        temp = read(pribor)
        publish(client, temp)
        time.sleep(1)
## Change temperature setpoint (SP) ##
# NEW_TEMPERATURE = 95
# instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage
