import csv
from config import file_name, normal_text, purple_text, red_text,green_text
# This function will be called when the user
# selects the list option.
def list_jobs(policy):
  # jobname,execution_time,priority, submitted_time
  queue = []
  try:
    with open(file_name, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        queue.append(row)
    print('You selected the list option.')
    print('Total number of jobs in the queue: ' + str(len(queue)))
    print('Scheduling policy: ' + policy)
    print('Job name, Execution time, Priority, Submitted time')
    for job in queue:
      print(job[0] + ', ' + job[1] + ', ' + job[2] + ', ' + job[3])

  except:
    print(red_text('There are no jobs in the queue.'))
    print(normal_text(''))

