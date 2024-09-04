from i2cdevice import MockSMBus

I2C_SMBUS = 0x0720
I2C_SMBUS_BYTE_DATA = 2
I2C_SMBUS_WRITE = 0
I2C_SLAVE = 0x0703  # Use this slave address
I2C_SLAVE_FORCE = 0x0706  # Use this slave address, even if it is already in use by a driver!


class SMBusFakeDevice(MockSMBus):
    def __init__(self, i2c_bus):
        MockSMBus.__init__(self, i2c_bus)
        self.regs[0x0F] = 0x6A         # Fake part ID

    def write_byte_data(self, i2c_addr, register, value):
        self.regs[register] = value
