import csv
from config import file_name, red_text,green_text
# This function will be called when the user
# selects the list option.
def list_jobs():
  # jobname,execution_time,priority, submitted_time
  queue = []
  try:
    with open(file_name, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        queue.append(row)
    print(green_text('You selected the list option.'))
    print(queue)
  except FileNotFoundError:
    print('There are no jobs in the queue.')
    print()

