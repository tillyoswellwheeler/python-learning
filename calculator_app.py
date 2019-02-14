#-----------------------------------------
# Python Learning -- Creating a calculator
#-----------------------------------------

#-----------------------------------------
#


class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def choice_op():
        choice = 1

        while choice != 0:
            print("Choose your operation by number:\n"
                  "1) +\n"
                  "2) -\n"
                  "3) /\n"
                  "4) *\n")
            choice = int(input("Enter chosen operator: "))
            if choice == 1:
                result = obj.sum_op()
                print("Result: ", obj.sum_op())
                return result
            elif choice == 2:
                result = obj.minus_op()
                print("Result: ", result)
                return result
            elif choice == 3:
                result = round(obj.divide_op(), 2)
                print("Result: ", result)
                return result
            elif choice == 4:
                result = obj.multiply_op()
                print("Result: ", result)
                return result
            elif choice == 0:
                print("Exiting")
            else:
                print("Invalid input")
                return False

#---- Sub-Functions
    def sum_op(self):
        result = self.num1 + self.num2
        return result

    def minus_op(self):
        result = self.num1 - self.num2
        return result

    def divide_op(self):
        result = self.num1 / self.num2
        return result

    def multiply_op(self):
        result = self.num1 * self.num2
        return result



if __name__ == '__main__':
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))
    obj = Calculator(num1, num2)
    Calculator.choice_op()

