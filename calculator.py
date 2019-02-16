# 3D Printer Calculator
# Calculates values to calibrate 3D Printers
# Author: Matt G
# Date: 2/15/19
# Ver: 0.1

#Libraries

import time

#Variables

running = True

#Functions

def main():
    if running:
        intro()

def intro():
    print(drawLine(10))
    print('3D Printer Calculator')
    print('By Mcgrizzler')
    print('Ver: 0.1')
    print(drawLine(10))
    time.sleep(5)
    returnLines(5)
    e_calibrate()

def drawLine(lineLength):
    return ('-' * lineLength)

def returnLines(numLines):
    print('\n' * numLines)
    return

def waitForUser():
    waitForKey = input('Press any key to continue...')
    print('\n')
    return

def e_calibrate():
    eSteps = 0.0
    actualMovement = 0.0
    offset = 0.0

    returnLines(2)
    drawLine(10)
    print('E Axis Calibration')
    drawLine(10)
    returnLines(2)

    time.sleep(2)
    print('Please load at least 150mm of a light filament [or dark if you have a light marker ;)]')
    waitForUser()

    print('Please take a ruler and make a mark 20mm up the filament, and another 100mm above that.')
    waitForUser()

    print('Important: Extrude the filament 1mm at a time via the printer controller.\nExtrude 100mm of filament.')
    waitForUser()

    print('Please measure the distance from the extruder to the mark on the filament.')
    waitForUser()

    userInput = input('How many mm to the mark?: ')

    try:
        userInput = int(userInput)
    except:
        print('Sorry, I do not recognize that input. Please try again.')
   
    eSteps = 80 + userInput
    offset = 100 - eSteps


    print('Extruder Input: 100mm\nExtruder Actual: {}mm\nOffset: {}mm'.format(eSteps, offset))
    time.sleep(5)
    returnLines(2)

    print('Please send the following command to your printer.')
    print('M92 E{}'.format(eSteps))
    waitForUser()

    print('To verify the setting has been stored, type the following command')
    print('M503')
    print('Look for the line that says M92 and verify the E value is the one set in the previous command.')
    waitForUser()

    print('To save the value to EEPROM permanently, send the following command.')
    print('M500')
    waitForUser()

    print('Congratulations! Your extruder is now calibrated. :)')
    time.sleep(5)
    print('The script will now restart...')
    main()
    

#Main program call
main()