import sys
import threading

from config.config import normal_text, blue_text, white_text, red_text, purple_text, policy_file_name
from services.scheduling.submit_job import submit_job
from services.scheduling.list_jobs import list_jobs
from services.scheduling.policy_change import change_policy

# Job name, Execution time, Priority, Submitted time

# This is the main function that will be called
# when the program is run.


def ui():
    while True:
        intro_text()
        choice = input()
        if choice == '1':
            help()
        elif choice == '2':
            submit_job()
        elif choice == '3':
            list_jobs()
        elif choice == '4':
            change_policy()
        elif choice == '5':
            exit()
        else:
            print(red_text('Invalid choice. Please try again.'))
            print()


def exit():
    print(red_text('You selected the exit option.'))
    print(red_text('Exiting the scheduling module.'))
    print(normal_text(''))

    sys.exit()


def intro_text():
    print()
    print(purple_text('Welcome to the scheduling module.'))
    print(purple_text('Please select an option from the menu below.'))
    print(blue_text('1. Help'))
    print(white_text('2. Submit job'))
    print(blue_text('3. List jobs'))
    print(white_text('4. Change policy'))
    print(blue_text('5. Exit'))
    print()
    print(purple_text('Please enter your choice: '), end='')
    print(normal_text(''))


def help():
    print(purple_text('You selected the help option.'))
    print(purple_text('This module is designed to explain '))
    print(purple_text('each menu option in CSU Batch Scheduling.'))
    print()
    print(purple_text('Run: Add jobs to the scheduling queue\n'))
    print(purple_text('List: List all jobs in the Job Queue that are scheduled to run\n'))
    print(purple_text('Change: Reorder all objects in the Queue'))
    print(purple_text('Exit: Quit the Program'))
    print()
