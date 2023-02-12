
class Complex(object):
    def __init__(self, real_part, imaginary_part):   # this called a constructor in Java
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, second_num):   # __ is a special method (Magic/Dunder)
        return Complex(self.real_part + second_num.real_part, self.imaginary_part + second_num.imaginary_part)

    def __sub__(self, second_num):
        return Complex(self.real_part - second_num.real_part, self.imaginary_part - second_num.imaginary_part)

    def __mul__(self, second_num):
        return Complex(self.real_part * second_num.real_part - self.imaginary_part * second_num.imaginary_part,
                       self.real_part * second_num.imaginary_part + second_num.real_part * self.imaginary_part)

    def __truediv__(self, second_num):
        denominator = second_num.real_part ** 2 + second_num.imaginary_part ** 2
        if denominator==0:
            return "Denominator cannot be zero "
        else:
            return Complex((self.real_part * second_num.real_part + self.imaginary_part * second_num.imaginary_part) / denominator,
                       (self.imaginary_part * second_num.real_part - self.real_part * second_num.imaginary_part) / denominator)

    def __str__(self):
        if self.imaginary_part == 0:
            result = "%.2f+0.00i" % (self.real_part)
        elif self.real_part == 0:
            if self.imaginary_part >= 0:
                result = "0.00+%.2fi" % (self.imaginary_part)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary_part))
        elif self.imaginary_part > 0:
            result = "%.2f+%.2fi" % (self.real_part, self.imaginary_part)
        else:
            result = "%.2f-%.2fi" % (self.real_part, abs(self.imaginary_part))
        return result

if __name__ == '__main__':
    x=Complex(2,4)
    y=Complex(3,5)
    print(*map(str, [x+y, x-y, x*y, x/y]), sep='\n')


