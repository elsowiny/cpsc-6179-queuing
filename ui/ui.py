import sys
import threading

from config.config import normal_text, blue_text, white_text, red_text, purple_text, policy_file_name
from job_queue.performance.main import get_performance as get_performance_from_queue
from services.scheduling.benchmark_test import testing_prompt
from services.scheduling.get_performance import get_performance

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
        elif choice == '6':
            get_performance()
        elif choice == '7':
            testing_prompt()
        elif choice == '8':
            sys.exit()
        else:
            print(red_text('Invalid choice. Please try again.'))
            print()


def exit():
    print(red_text('You selected the exit option.'))
    print(red_text('Exiting the scheduling module.'))
    print(normal_text(''))
    get_performance()

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
    print(white_text('6. Get performance'))
    print(blue_text('7. Run benchmark test'))
    print()
    print(purple_text('Please enter your choice: '), end='')
    print(normal_text(''))


def help():
    print(purple_text('You selected the help option.'))
    print(purple_text('This module is designed to explain '))
    print(purple_text('each menu option in CSU Batch Scheduling.'))
    print()
    print(purple_text('Submit: Add jobs to the scheduling queue\n'))
    print(purple_text('List: List all jobs in the Job Queue that are scheduled to run\n'))
    print(purple_text('Change: Change Policy all objects in the Queue'))
    print()
    print(purple_text('fcfs: change the scheduling policy to FCFS\n'))
    print(purple_text('sjf: change the scheduling policy to SJF\n'))
    print(purple_text('pri: change the scheduling policy to priority\n'))
    print()
    print(purple_text('Exit: Quit the Program'))
    print()
