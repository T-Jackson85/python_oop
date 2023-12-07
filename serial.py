"""Python serial number generator."""
from random import randint

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start =100):
        """ Creates starting point for generator"""
        self.start = self.next = start
    
    def generate(self):
        """genrate the next number"""
        self.next += 1
        return self.next -1
    
    def reset(self):
        """Start the counter from the beginning"""
        self.next = self.start




