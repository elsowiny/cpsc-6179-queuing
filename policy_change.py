import csv
from config import file_name

def change():
  print('You selected the change option.')
  print('Please enter the new scheduling policy: ', end='')
  new_policy = input()
  new_policy = new_policy.upper()
  # needs to be a valid policy
  if new_policy == 'FCFS' or new_policy == 'SJF' or new_policy == 'PRI':
    global policy
    policy = new_policy
    handle_policy_change(policy)
  elif new_policy == '':
    print('Policy is ',  policy)
    return
  else:
    print('Invalid scheduling policy. Please try again.')
    change()


def handle_policy_change(policy):
  print('The new scheduling policy is: ' + policy)
  print()
  if(policy == 'FCFS'):
    fcfs()
  elif(policy == 'SJF'):
    sjf()
  elif(policy == 'PRI'):
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
  with open(file_name, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      queue.append(row)
  # sort the queue based on the submitted time
  queue.sort(key=lambda x: x[3])
  # print the queue
  print(queue)
  print()
  # save the queue back to the csv file
  with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in queue:
      writer.writerow(row)
  print('The queue has been processed.')
  print()
  
def sjf():
  print('You selected the SJF policy.')
  print('The queue is being processed.')
  print()

def pri():
  print('You selected the PRI policy.')
  print('The queue is being processed.')
  print()
