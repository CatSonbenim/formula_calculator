class Counter:

    def __init__(self, x):

        self.y = 0
        if x <= -5.643 or x >= 409.254:
            self.x = x
        else:
            raise ValueError('Number you entered is not in range. Please reenter number.')

    def count_f1(self):
        self.y = (self.x ** 4 * 2.986) + (self.x ** 3 * 3.021) - (self.x ** 2 * 4.179) + (self.x * 1.179)

    def count_f2(self):
        self.y = (self.x ** 3 * 4.246) - (self.x ** 2 * 2.396) + (self.x * 2.96)

    def count_f3(self):
        self.y = (self.x ** 2 * 2.29) + (self.x * 3.877)

    def count_f4(self):
        self.y = self.x * 2.473

    def answer(self, formula):
        select = {1: self.count_f1, 2: self.count_f2, 3: self.count_f3, 4: self.count_f4}
        select[formula]()
        return self.y


def main():

    while True:
        try:
            x = float(input('Enter x in range x <= -5.643 or x >= 409.254:  '))
            obj = Counter(x)
            break
        except ValueError:
            print('\nNumber you entered is not in range. Please reenter number.\n\n')

    while True:
        try:
            formula = int(input('\nEnter number of formula that you want to count in range from 1 to 4:'))
            if 1 <= formula <= 4:
                answer = obj.answer(formula)
                print(answer)
                break
            else:
                raise ValueError
        except ValueError:
            print('\nNumber you entered is not in range. Please reenter number.\n\n')

    choosing()


def choosing():
    while True:
        try:
            choice = input('Do you want to count again? y/n   ')
            if choice == 'y':
                main()
            elif choice == 'n':
                break
            else:
                raise ValueError
        except ValueError:
            print('Please enter y or n!\n')


if __name__ == '__main__':
    main()
