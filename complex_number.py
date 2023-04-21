import math

class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return "{} + {}i".format(self.real, self.imaginary)

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def multiply(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)

    def divide(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / denominator,
                             (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def is_zero(self):
        return self.real == 0 and self.imaginary == 0

    def square_root(self):
        r = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        phi = math.atan2(self.imaginary, self.real)
        return ComplexNumber(round(r * math.cos(phi / 2), 2), round(r * math.sin(phi / 2), 2))