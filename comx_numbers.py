class comx:
    def __init__(self, x, y):
        self.real = x
        self.imag = y

    def __add__(self, b):
        return comx(self.real + b.real, self.imag + b.imag)

    def __sub__(self, b):
        return comx(self.real - b.real, self.imag - b.imag)

    def __mul__(self, b):
        return comx(self.real * b.real - self.imag * b.imag, self.real * b.imag + self.imag * b.real)

    def __truediv__(self, b):
        divisor = b.real ** 2 + b.imag ** 2
        real_part = (self.real * b.real + self.imag * b.imag) / divisor
        imag_part = (self.imag * b.real - self.real * b.imag) / divisor
        return comx(real_part, imag_part)

a = comx(1, 2)
b = comx(2, 3)

C = a + b
print("a + b =", C.real, "+", C.imag, "i")

d = a - b
print("a - b =", d.real, "+", d.imag, "i")

e = a * b
print("a * b =", e.real, "+", e.imag, "i")

f = a / b
print("a / b =", f.real, "+", f.imag, "i")
