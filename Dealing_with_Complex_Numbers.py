import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __div__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
            
        elif self.real == 0 and self.imaginary >= 0:
            result = "0.00+%.2fi" % (self.imaginary)
        elif self.real == 0 and self.imaginary < 0:
            result = "0.00%.2fi" % (self.imaginary)   
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
            
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


C = map(float, raw_input().split())
D = map(float, raw_input().split())
x = Complex(C[0],C[1])
y = Complex(D[0],D[1])

print str(x+y)
print str(x-y)
print str(x*y)
print str(x/y)
print str(x.mod())
print str(y.mod())
