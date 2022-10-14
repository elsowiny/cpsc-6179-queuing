from cmath import inf
import csv
from config import file_name, normal_text, red_text, policy_file_name, FCFS, PRI, SJF

def change():
  print('You selected the change option.')
  print('Please enter the new scheduling policy: ', end='')
  new_policy = input()
  new_policy = new_policy.upper() # needs to be a valid policy
  if new_policy == FCFS or new_policy == SJF or new_policy == PRI:
    handle_policy_change(new_policy)
  elif new_policy == '5':
    print('You selected the exit option.')
    print('Exiting the scheduling module.')
    exit()
  elif new_policy == '':
     with open(policy_file_name, 'r') as file:
      curr_policy = file.read()
      print('Policy is ', curr_policy)  
      return
  else:
    print('Invalid scheduling policy. Please try again.')
    change()


def handle_policy_change(policy):
  print('The new scheduling policy is: ' + policy)
  print()
  with open(policy_file_name, 'w') as file:
    file.write(policy)
  if(policy == FCFS):
    fcfs()
  elif(policy == SJF):
    sjf()
  elif(policy == PRI):
    pri()

def fcfs():
  print('You selected the FCFS policy.')
  print('The queue is being processed.')
  print()
  # we will reorder the queue based on the time the job was submitted
  # we will use the submitted time to sort the queue
  # which will be the 4th element in the list
  # need to read it in from the csv file
  queue = []
  try:
    with open(file_name, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        queue.append(row)
    # sort the queue based on the submitted time
    queue.sort(key=lambda x: x[3])
    # print the queue
    print('Job name, Execution time, Priority, Submitted time')
    for job in queue:
      print(job[0] + ', ' + job[1] + ', ' + job[2] + ', ' + job[3])
    # save the queue back to the csv file
    with open(file_name, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      for row in queue:
        writer.writerow(row)
    print('The queue has been reordered based on the submitted time.')
  except:
    print(red_text('There are no jobs in the queue.'))
    print(normal_text(''))
  
def sjf():
  print('You selected the SJF policy.')
  print('The queue is being processed.')
  print()
  # we will reorder the queue based on the execution time
  # we will use the execution time to sort the queue
  # which will be the 2nd element in the list
  # need to read it in from the csv file
  queue = []
  try:
    with open(file_name, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        queue.append(row)

    # sort the queue based on the execution time
    # we need to convert the execution time to an integer
    # so we can sort it
    queue.sort(key=lambda x: int(x[1]))
    
    

    # print the queue
    print('Job name, Execution time, Priority, Submitted time')
    for job in queue:
      print(job[0] + ', ' + job[1] + ', ' + job[2] + ', ' + job[3])
    # save the queue back to the csv file
    with open(file_name, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      for row in queue:
        writer.writerow(row)
    print('The queue has been reordered based on the execution time. SJF')
  except:
    print(red_text('There are no jobs in the queue.'))
    print(normal_text(''))


def pri():
  print('You selected the PRI policy.')
  print('The queue is being processed.')
  print()
  # we will reorder the queue based on the priority
  # we will use the priority to sort the queue
  # which will be the 3rd element in the list
  #if it is empty, we will use the submitted time
  # need to read it in from the csv file
  queue = []
  try:
    with open(file_name, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        queue.append(row)
    # sort the queue based on the priority
    # if it is an empty string it goes to the end
    # we need to convert the priority to an integer
    # so we can sort it

    queue = sorted(queue, key=lambda x: int(x[2]) if x[2] != '' else inf)

    # queue = sorted(queue, key=lambda x: (x[2] == '', x[2]))
    # print the queue
    print('Job name, Execution time, Priority, Submitted time')
    for job in queue:
      print(job[0] + ', ' + job[1] + ', ' + job[2] + ', ' + job[3])
    # save the queue back to the csv file
    with open(file_name, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      for row in queue:
        writer.writerow(row)
    print('The queue has been reordered based on the priority.')
  except:
    print(red_text('There are no jobs in the queue.'))
    print(normal_text(''))