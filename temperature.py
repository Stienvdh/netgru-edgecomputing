import time
import smbus

def read_i2c_temperature():
    address = 0x38 # Put your device's address here

    i2cbus = smbus.SMBus(1)
    time.sleep(0.5)

    data = i2cbus.read_i2c_block_data(address,0x71,1)
    if (data[0] | 0x08) == 0:
        print('Initialization error')

    i2cbus.write_i2c_block_data(address,0xac,[0x33,0x00])
    time.sleep(0.1)

    data = i2cbus.read_i2c_block_data(address,0x71,7)

    Traw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
    temperature = 200*float(Traw)/2**20 - 50

    return temperature