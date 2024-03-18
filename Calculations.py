class BinaryCalculator:

""" 
Calculations to be called from the main script handling program loop.
"""
    
    def bin_add(self):
        print('\nBinary Addition\n')
        bin1 = [0] * 8
        bin2 = [0] * 8
        answer_bin = [0] * 8
        print('First Number')
        bin1 = BinaryCalculator.get_user_bin(self)
        print(bin1)
        print('\nSecond Number')
        bin2 = BinaryCalculator.get_user_bin(self)
        print(bin2)
        input('\nPress any key to continue')

        iterator = 0
        carry_over = False
        answer_bin = BinaryCalculator.bin_simple_add(self, bin1, bin2)

        print(' ', bin1, '\n+', bin2, '\n=', answer_bin)
        input('\nPress any key to continue')

    def bin_sub(self):
        print('\nBinary Subtraction\n')
        bin1 = [0] * 8
        bin2 = [0] * 8
        answer_bin = [0] * 8
        print('First Number')
        bin1 = BinaryCalculator.get_user_bin(self)
        print(bin1)
        print('\nSecond Number')
        bin2 = BinaryCalculator.get_user_bin(self)
        print(bin2)
        input('\nPress any key to continue')
        print(' ', bin1, ' - ', bin2)
        bin2 = BinaryCalculator.bin_simple_neg(self, bin2)
        print('=', bin1, ' + ', bin2)
        input('\nPress any key to continue')
        answer_bin = BinaryCalculator.bin_simple_add(self, bin1, bin2)
        print('\n ', bin1, '\n+', bin2, '\n=', answer_bin)
        input('\nPress any key to continue')

    # Binary negation that shows working to the user
    def bin_neg(self):
        print('\nBinary Negation\n')
        bin1 = [0] * 8
        answer_bin = [0] * 8
        bin_value1 = [0, 0, 0, 0, 0, 0, 0, 1]
        print('Number for Operation')
        bin1 = BinaryCalculator.get_user_bin(self)
        print(bin1)
        input('\nPress any key to continue')
        print(' ', bin1)
        # flip 1s complement
        iterator = 0
        for bit in bin1:
            if bit == 0:
                bin1[iterator] = 1
            else:
                bin1[iterator] = 0
            iterator += 1
        print(' ', bin1, '(Flip')
        # add 1 for 2s complement
        answer_bin = BinaryCalculator.bin_simple_add(self, bin1, bin_value1)
        print('+', bin_value1, '(Add 1)', '\n=', answer_bin)
        input('\nPress any key to continue')

    # negate function used by other calculation functions
    # not used by the main negation function 'bin_neg' as it does not show working to the user
    def bin_simple_neg(self, negation_bin):
        bin_value1 = [0, 0, 0, 0, 0, 0, 0, 1]
        iterator = 0
        # flip for 1s complement
        for bit in negation_bin:
            if bit == 0:
                negation_bin[iterator] = 1
            else:
                negation_bin[iterator] = 0
            iterator += 1
        # add 1 for 2s complement
        negation_bin = BinaryCalculator.bin_simple_add(self, negation_bin, bin_value1)
        return negation_bin

    # add function used by other calculation functions
    def bin_simple_add(self, firstNum, secondNum):
        answer_bin = [0] * 8
        iterator = 0
        carry_over = False
        while iterator <= 7:
            current_bit = 7 - iterator
            answer_bit = firstNum[current_bit] + secondNum[current_bit]
            if carry_over:
                carry_over = False
                answer_bit = answer_bit + 1

            if answer_bit == 2:
                carry_over = True
                answer_bit = 0
            elif answer_bit == 3:
                carry_over = True
                answer_bit = 1

            answer_bin[current_bit] = answer_bit
            iterator += 1
        return answer_bin

    # multiple functions need to get a 8bit binary number from the user
    def get_user_bin(self):
        gettingInput = True
        while gettingInput:
            user_bin = input('Input: ')
            if len(user_bin) == 8 and BinaryCalculator.is_bin(self, user_bin):
                return BinaryCalculator.convert_input(self, user_bin)
            else:
                print('Invalid\n')
                continue

    # check user input is a binary number
    def is_bin(self, bin_input):
        bin_input.lower()
        for bit in bin_input:
            if bit == '1' or bit == '0':
                continue
            else:
                return False
        return True

    def convert_input(self, bin_input):
        input_num = [0] * 8
        iterator = 0
        for bit in bin_input:
            input_num[iterator] = int(bit)
            iterator += 1
        return input_num

