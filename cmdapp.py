#########################################################
#              -- Rep Rap Calibrator --                 #
#               Author: Matthew Gravis                  #
#                   Date: 2/20/19                       #
#                      Ver: 0.2                         #
#########################################################

# -*- coding: utf-8 -*-

# - Libraries -
from __future__ import print_function, unicode_literals
import time

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError

# - Styles -
style = style_from_dict({
    Token.Separator: '#f0ff00',
    Token.QuestionMark: '#0092ff bold',
    Token.Selected: '#00ff11 bold',
    Token.Pointer: '#ff0000 bold',  
    Token.Instruction: '',  # default
    Token.Answer: '#00ff04 bold',
    Token.Question: '',
})

# - Prompts-

# Select an action to run
actions = [
    {
        'type': 'checkbox',
        'name': 'script',
        'message': '',
        'choices': [
            Separator('\n   = Select One=\n'),
            {
                'name': 'Calibrate All' # Run all calibrations
            },
            {
                'name': 'PID Tune' # Walk-through for PID tuning extruder and bed
            },
            {
                'name': 'Extruder' # Walk-through for calibrating E-steps
            },
            {
                'name': 'Linear Advance' # Walk-through for calibrating K-value and enabling Linear Pressure Control
            },
            {
                'name': 'EEPROM Values' # Display modified EEPROM values for Maker Select V2.1
            },
        ],
    }
]

# - Functions - 
def main(firstRun): # Main program function
    # Check if to display intro
    if firstRun:
        intro()
    else:
        print('\n\n')

    # Run actionSelection prompt to select function
    actionSelection = prompt(actions, style=style)

    # Check for input
    if actionSelection['script'] == '':
        print('You must choose an action.\n')
        time.sleep(2)
        main(False)
    else:
        if actionSelection['script'][0] == 'Calibrate All':
            calibrateAll()
        elif actionSelection['script'][0] == 'PID Tune':
            pidTune(True)
        elif actionSelection['script'][0] == 'Extruder':
            calibrateExtruder(True)
        elif actionSelection['script'][0] == 'Linear Advance':
            calibrateLinearAdvance()
        elif actionSelection['script'][0] == 'EEPROM Values':
            displayEEPROM()

def intro(): # Program intro display
    print('\n----------\n\nRepRap Calibrator\n\n----------')
    time.sleep(5)
    print('\n\n')

def calibrateAll(): # Run all calibrations
    print('\n\n\n\n\n\n\n\nCalibrate All...\n\n')

    pidTune(False) # Run PID tuning without Single Run

def pidTune(singleRun): # PID tune extruder and bed
    print('\n\n\n\n\n\n\n\nPID Tuning Starting...\n\n----------\n')

    time.sleep(1)

    print('Step 1:\n\n-Launch octoprint or pronterface and start a usb session with the printer\n-Send the following command to the printer: (PLA) M303 E0 S210 C5 (ABS) M303 E0 S245 C5\n\n')
    
    time.sleep(2)
    temp_continue = input('Press enter to continue...')
    time.sleep(1)

    eP = input('Enter Kp Value: ')
    eI = input('Enter Ki Value: ')
    eD = input('Enter Kd Value: ')

    time.sleep(1)

    print('\nEnter the following command:\n\n- M301 P{} I{} D{}\n\n- M500\n\n'.format(eP, eI, eD))

    time.sleep(2)
    temp_continue = input('Press enter to continue...')
    time.sleep(1)

    print('\n-Send the following command to the printer: (PLA) M303 E-1 S60 C5 (ABS) M303 E-1 S70 C5\n\n')
   
   
    # !! STOP POINT !! -- You were continuing the script to PID tune a second time with higher values and lower height/high fan --
   
   
    time.sleep(1)

    bP = input('Enter Kp Value: ')
    bI = input('Enter Ki Value: ')
    bD = input('Enter Kd Value: ')

    print('\nEnter the following command:\n\n- M304 P{} I{} D{}\n\n- M500\n\n'.format(bP, bI, bD))
    
    if singleRun:
        main(False)
    else:
        calibrateExtruder(False)

def calibrateExtruder(singleRun): # Calibrate Extruder E-Steps
    print('\n\n\n\n\n\n\n\nExtruder Calibration Starting...\n\n----------\n')
    
    time.sleep(1)

    print('Tools Needed:\n\n-Ruler or Calipers\n-Marker\n')
    print('Preparation:\n\n-Heat Extruder (PLA: 210C / ABS: 240C)\n-Load a light colored filament (Or dark if you have a light marker ;))\n\n')
    
    time.sleep(2)
    temp_continue = input('Press enter to continue...')
    time.sleep(1)

    print('\n\nStep 1:\n\n-Measure 20mm from the top of the extruder and mark the filament.\n-Measure 100mm from the first mark and mark the filament.\n\n')
    
    time.sleep(2)
    temp_continue = input('Press enter to continue...')
    time.sleep(1)

    print('\n\nStep 2:\n\n-Select Move E-Axis on printer control box (1 mm)\n-IMPORTANT: Go Slowly.\n-Move the extruder 100mm one mm at a time\n\n')

    time.sleep(2)
    temp_continue = input('Press enter to continue...')
    time.sleep(1)

    print('\n\nStep 3:\n\n-Measure from the top of the extruder to the remaining mark.\n\n')
    
    time.sleep(2)
    actualMovement = input('Enter the measurement in mm: ')
    time.sleep(1)

    print('\n\nStep 4:\n\n-Launch octoprint or pronterface and start a usb session with the printer\n-Open the Terminal\n-Send Command M503 to the printer\n-Find the line starting with M92\n\n')

    time.sleep(2)
    setMovement = input('Enter the current value of E on line M92: ')
    time.sleep(1)

    newE = 95

    print('\nStep 5:\n\n-Send the printer the following command: M92 E{}\n-Send M503 again and ensure the value has changed for M92 E\n-Send command M500 to save the values\n\n'.format(newE))
    
    time.sleep(2)
    temp_continue = input('Press enter to continue...')
    time.sleep(1)

    print('\n\nExtruder Calibration Complete!')
    
    time.sleep(2)

    if singleRun:
        main(False)
    else:
        calibrateLinearAdvance()

def calibrateLinearAdvance(): # Calibrate K-Value and enable Linear Advance
    print('\n\n\n\n\n\n\n\nLinear Advance Calibration Starting...\n\n')

    # Placeholder :)

    main(False)

def displayEEPROM(): # Show EEPORM Values
    print('\n\n\n\n\n\n\n\nEEPROM Values Starting...\n\n')

    # Placeholder :)

    main(False)

# - Main Program Call -
main(True)
    