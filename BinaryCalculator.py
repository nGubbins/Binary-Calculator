"""SUMMARY
# A simple 8bit binary calculator created to show binary calculations through code.
# Some implementation may be extended to show logic."""

import Calculations
Calc = Calculations.BinaryCalculator()

# The main menu string showing options to the user
startingString = ('\nOptions:\nAddition (a) || Subtraction (s) || Negation (n)' 
                  # '\nBinary to Decimal (b2d) || Decimal to Binary (d2b)' 
                  '\nExit (e)\n')

# handle multiple user inputs for single option
optionE = ['exit', 'e']
optionA = ['addition', 'add', 'a']
optionS = ['subtraction', 'subtract', 's']
optionN = ['negation', 'negate', 'n']
optionB2D = ['binary to decimal', 'bin to dec', 'bin2dec', 'binary2decimal', 'b2d', 'btd', 'binary 2 decimal']
optionD2B = ['decimal to binary', 'dec to bin', 'dec2bin', 'decimal2binary', 'dtb', 'd2b', 'decimal 2 binary']

# Run (Main Loop) #
print('\n8bit BINARY CALCULATOR')
running = True

while running:
    # Give user menu
    print(startingString)

    # Get user input
    userInput = input('Choose Option: ').lower()

    # Select option
    if userInput in optionE:
        break
    elif userInput in optionA:
        # do addition
        Calc.bin_add()
        continue
    elif userInput in optionS:
        # do subtraction
        Calc.bin_sub()
        continue
    elif userInput in optionN:
        # do negation
        Calc.bin_neg()
        continue
    elif userInput in optionB2D:
        # do binary to decimal
        print('binary to decimal: non-functional')
        continue
    elif userInput in optionD2B:
        # do decimal to binary
        print('decimal to binary: non-functional')
        continue
    else:
        # handle all other input
        print('\nINVALID INPUT')

exit()
