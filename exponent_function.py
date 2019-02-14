#-----------------------------------------
# Python Learning -- Exponent Functions
#-----------------------------------------

#-----------------------------------------
# Using a For Loop


class ExponentFunction:
    def __init__(self, base_num, pow_num):
        self.base_num = base_num
        self.pow_num = pow_num

    def raise_to_power(self, base_num, pow_num):
        result = 1
        for index in range(self.pow_num):
            result = result * self.base_num
        return result

if __name__ == '__main__':
    base_num = int(input("What number is your base number to be powered by? "))
    pow_num = int(input("...and what do you want to power it by? "))
    obj = ExponentFunction(base_num, pow_num)
    print(obj.raise_to_power(base_num, pow_num))


