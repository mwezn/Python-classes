import math

class Complex(object):
    def __init__(self, real, imaginary):
       
        global x
        global y
        self.real=real
        self.imaginary=imaginary
        
        
    def __add__(self, no):
        z=Complex(self.real,self.imaginary)
        z.real=x.real+y.real
        z.imaginary=x.imaginary+y.imaginary
        return z
    def __sub__(self, no):
        z=Complex(self.real,self.imaginary)
        z.real=x.real-y.real
        z.imaginary=x.imaginary-y.imaginary
        return z
    def __mul__(self, no):
        z=Complex(self.real,self.imaginary)
        z.real=(x.real*y.real-x.imaginary*y.imaginary)
        z.imaginary=(x.real*y.imaginary)+(x.imaginary*y.real)
        return z
        
    def __div__(self,no):
        z=Complex(self.real,self.imaginary)
        z.real=(x.real*y.real+x.imaginary*y.imaginary)/(y.real*y.real+y.imaginary*y.imaginary)
        z.imaginary=(x.imaginary*y.real-x.real*y.imaginary)/(y.real*y.real+y.imaginary*y.imaginary)
        return z

    def mod(self):
        z=self.real**2+self.imaginary**2
        return "%.2f +0.00i"%math.sqrt(z)
        

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())
    x = Complex(*c)
    y = Complex(*d)
    print '\n'.join(map(str, [x+y,x-y,x*y,x/y,x.mod(),y.mod()]))