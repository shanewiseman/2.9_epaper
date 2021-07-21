import logging
import time

class hardware:

    RST_PIN = 17
    DC_PIN = 25
    CS_PIN = 8
    BUSY_PIN = 24

    def __init__(self):
        import spidev
        import RPi.GPIO

        self.GPIO = RPi.GPIO
        self.SPI = spidev.SpiDev()

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
        self.GPIO.setup(self.RST_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.DC_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.CS_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.BUSY_PIN, self.GPIO.IN)

        # SPI device, bus = 0, device = 0
        self.SPI.open(0, 0)
        self.SPI.max_speed_hz = 4000000
        return 0

    def __del__(self):
        logging.debug("Closing SPI")

        self.SPI.close()

        self.GPIO.output(self.RST_PIN, 0)
        self.GPIO.output(self.DC_PIN, 0)
        self.GPIO.cleanup()

    def gpio_write(self, pin, value):
        self.GPIO.output(pin, value)

    def gpio_read(self, pin):
        return self.GPIO.input(pin)
    
    def delay_ms(self, delaytime):
        time.sleep(delaytime / 1000.0)

    def spi_write(self, data):
        self.SPI.writebytes(data)

    def spi_write_list(self, data: list):
        self.SPI.writebytes2(data)








