import sys
from list_jobs import list_jobs

from policy_change import change
from run_job import run
from config import normal_text, blue_text, white_text, red_text,purple_text, policy_file_name
from help import help



# This is the main function that will be called
# when the program is run.
def main():
  global policy
  # we are now reading policy in from policy.txt
  with open(policy_file_name, 'r') as f:
    policy = f.read()
 
  while True:
    print()
    print(purple_text('Welcome to the scheduling module.'))
    print(purple_text('Please select an option from the menu below.' ))
    print(blue_text('1. Help'))
    print(white_text('2. Run'))
    print(blue_text('3. List'))
    print(white_text('4. Change'))
    print(blue_text('5. Exit'))
    print()
    print(purple_text('Please enter your choice: '), end='')
    print(normal_text(''))

    choice = input()
    if choice == '1':
      help()
    elif choice == '2':
      run(policy)
    elif choice == '3':
      list_jobs(policy)
    elif choice == '4':
      change()
    elif choice == '5':
      exit()
    else:
      print(red_text('Invalid choice. Please try again.'))
      print()


def exit():
  print(red_text('You selected the exit option.'))
  print(red_text('Exiting the scheduling module.'))
  # return console to normal
  print(normal_text(''))
  sys.exit()

if __name__ == '__main__':
  main()
