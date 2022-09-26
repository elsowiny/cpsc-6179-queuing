import csv
import time
from config import file_name, purple_text, red_text
# jobname,execution_time,priorty
# the file is jobs.csv
def save_job(job_name, exec_time, priority='',):
  exec_time = str(exec_time)
  priority = str(priority)
  try:
    with open(file_name, 'a', newline='') as csvfile:
      writer = csv.writer(csvfile)
      submitted_time = time.time()
      writer.writerow([job_name, exec_time, priority, submitted_time])
      # print in bold and blue
      print(purple_text(job_name + ' was submitted.'))
  except:
    print(red_text('There was an error saving the job.'))
    print()