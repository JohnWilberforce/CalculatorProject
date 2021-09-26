class Calculator:
    def __init__(self):
        pass

    def get_input_operators(self, key1, key2, operator):
        if operator == '*':
            print(key1 * key2)
        elif operator == '-':
            print(key1 - key2)
        elif operator == '+':
            print(key1 + key2)
        elif operator == '/':
            print(key1 / key2)
        elif operator == '%':
            print(key1 % key2)
        else:
            print('Enter the right operator')

    def run(self):
        x = 0
        while x < 4:
            key1 = float(input('Enter your first number: '))
            key2 = float(input('Enter your second number: '))
            operator = input('Enter operator: ')
            self.get_input_operators(key1, key2, operator)

            if x == 3:
                print(' Wait for 5 min and try again')

                break
            x += 1


calc = Calculator()
calc.run()
