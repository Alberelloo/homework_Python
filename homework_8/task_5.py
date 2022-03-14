# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения
# и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.

# (Complex_number(real_part,imag_part))
class Complex_number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return f'{real_part}+{imag_part}i'

    def __mul__(self, other):
        real_part = self.real * other.real - (self.imag * other.imag)
        imag_part = self.real * other.imag + other.real * self.imag
        return f'{real_part}+{imag_part}i'

num_1 = Complex_number(7, -2)
num_2 = Complex_number(2, 3)

print(num_1 + num_2)
print(num_1 * num_2)