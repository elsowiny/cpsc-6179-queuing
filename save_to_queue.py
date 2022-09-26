import csv
import time
from config import file_name, green_text, purple_text, red_text
# jobname,execution_time,priorty
# the file is jobs.csv
def save_job(job_name, exec_time,policy, priority=''):
  exec_time = str(exec_time)
  priority = str(priority)
  try:
    with open(file_name, 'a', newline='') as csvfile:
      writer = csv.writer(csvfile)
      submitted_time = time.time()
      writer.writerow([job_name, exec_time, priority, submitted_time])
      print(green_text(job_name + ' was submitted.'))

      # now get all the jobs in the queue
      # and sum up the execution times
      # and print the expected waiting time
      queue = []
      with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
          queue.append(row)
      total_exec_time = 0
      for job in queue:
        total_exec_time += int(job[1])
      print(purple_text('Expected waiting time: ' + str(total_exec_time)))
      print(purple_text('Scheduling policy: ' + policy))
  except FileNotFoundError:
    print(red_text('There are no jobs in the queue.'))
    print()


  except:
    print(red_text('There was an error saving the job.'))
    print()