from config import purple_text
def help():
  print(purple_text('You selected the help option.'))
  print(purple_text('This module is designed to explain '))
  print(purple_text('each menu option in CSU Batch Scheduling.'))
  print()
  print(purple_text('Run: Run a job the is list in the Job Queue\n'))
  print(purple_text('List: List all jobs in the Job Queue that are scheduled to run\n' ))
  print(purple_text('Change: Change the scheduling policy of a submitted job'))
  print(purple_text('Exit: Quit the Program'))
  print()
