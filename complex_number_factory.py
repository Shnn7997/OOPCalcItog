from complex_number import ComplexNumber

class ComplexNumberFactory:
    @staticmethod
    def create_complex_number(string):
        parts = string.split("+")
        if len(parts) == 2:
            real = float(parts[0].strip())
            imaginary = float(parts[1].strip()[:-1])
            return ComplexNumber(real, imaginary)
        elif string.endswith("i"):
            return ComplexNumber(0, float(string[:-1]))
        else:
            return ComplexNumber(float(string))