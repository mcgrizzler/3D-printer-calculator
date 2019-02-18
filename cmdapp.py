#########################################################
#              -- Rep Rap Calibrator --                 #
#               Author: Matthew Gravis                  #
#                   Date: 2/18/19                       #
#                      Ver: 0.1                         #
#########################################################

# -*- coding: utf-8 -*-

# - Libraries -
from __future__ import print_function, unicode_literals
import time

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError

# - Variables -

# Booleans
firstRun = True # True = Show Intro || False == Two Return-lines

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
        'validate': lambda answer: 'You must choose at least one action.' \
            if len(answer) == 0 else True
    }
]

# - Functions - 
def main(): # Main program function
    # Check if to display intro
    if firstRun:
        intro()
        firstRun = False
    else:
        print('\n\n')

    # Run actionSelection prompt to select function
    actionSelection = prompt(actions, style=style)

    # --Debug-- Print
    pprint(actionSelection)


def intro(): # Program intro display
    print('\n----------\n\nRepRap Calibrator\n\n----------')
    time.sleep(5)
    print('\n\n')

def calibrateAll(): # Run all calibrations
    print('\n\n\n\n\n\n\n\nCalibrate All...\n\n')

    pidTune(False) # Run PID tuning without Single Run

def pidTune(singleRun): # PID tune extruder and bed
    print('\n\n\n\n\n\n\n\nPID Tuning Starting...\n\n')
    
    # Placeholder :)

    if singleRun:
        main():
    else:
        calibrateExtruder():

def calibrateExtruder(singleRun): # Calibrate Extruder E-Steps
    print('\n\n\n\n\n\n\n\nExtruder Calibration Starting...\n\n')
    
    # Placeholder :)

    if singleRun:
        main():
    else:
        calibrateLinearAdvance():

def calibrateLinearAdvance(): # Calibrate K-Value and enable Linear Advance
    print('\n\n\n\n\n\n\n\nLinear Advance Calibration Starting...\n\n')

    # Placeholder :)

    main():

def displayEEPROM(): # Show EEPORM Values
    print('\n\n\n\n\n\n\n\nEEPROM Values Starting...\n\n')

    # Placeholder :)

    main():

# - Main Program Call -
main()
    