from config import blue_text, green_text, red_text
from save_to_queue import save_job
from config import red_text, purple_text
global EXEC
EXEC = 'exec'
# This function will be called when the user
# selects the run option.
# takes in a job name, execution time, and priority
# and adds it to the job queue
# and returns total number of jobs in the queue
# expected waiting time
# and scheduling policy
def run(policy):
  print(green_text('You selected the run option.'))
  print(blue_text('Please enter the job name: '), end='')
  job_name = input()
  exec_time = handle_sanitized_input(EXEC)
  priority = handle_sanitized_input()
  save_job(job_name, exec_time,policy, priority)


def handle_sanitized_input(type=''):
  if(type == EXEC):
    print(purple_text('Please enter the execution time: '), end='')
  else:
    print(blue_text('Please enter the priority: '), end='')
  try:
    user_input = input()
    if(user_input == '' and type != EXEC):
      print('no priority')
      return ''
    converted = int(user_input)
    return converted
  except:
    print(red_text('Please enter a number'))
    return handle_sanitized_input(type)

  