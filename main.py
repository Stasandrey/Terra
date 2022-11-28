import minimalmodbus
import serial
import time
import os
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

result = os.system('echo baziliy | sudo -S chmod 666 /dev/ttyUSB0')


# echo
#     password | sudo - S
#     команда
pribor = portSetup()
while True:
#
    read(pribor)
    time.sleep(1)
## Change temperature setpoint (SP) ##
# NEW_TEMPERATURE = 95
# instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage

