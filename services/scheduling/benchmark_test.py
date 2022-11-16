
# test <benchmark> <policy> <num_of_jobs> <priority_levels>
#  <min_CPU_time> <max_CPU_time>

from config.config import FCFS, PRI, SJF
from tester.main import tester


def testing_prompt():
    # > mybenchmark fcfs 5 3 10 20
    print('You selected the benchmark test option.')
    print('Please enter the name of the benchmark test, followed by the policy, number of jobs, priority levels, minimum CPU time, and maximum CPU time.')
    print('Example: mybenchmark fcfs 5 3 10 20')
    print('Please enter your choice: ', end='')
    choice = input()
    choice = choice.split(' ')
    if len(choice) != 6:
        print('Invalid choice. Please try again.')
        testing_prompt()
    else:
        # are the values valid?
        benchmark = choice[0]
        policy = choice[1]
        num_of_jobs = choice[2]
        priority_levels = choice[3]
        min_CPU_time = choice[4]
        max_CPU_time = choice[5]
        try:
            policy = policy.upper()
            if policy not in [FCFS, SJF, PRI]:
                print('Invalid choice. Please try again.')
                testing_prompt()
        except:
            print('Invalid choice. Please try again.')
            testing_prompt()
        try:
            num_of_jobs = int(num_of_jobs)
            priority_levels = int(priority_levels)
            min_CPU_time = int(min_CPU_time)
            max_CPU_time = int(max_CPU_time)
        except:
            print('Invalid choice. Please try again.')
            testing_prompt()
        # run the benchmark test
        tester(benchmark, policy, num_of_jobs,
               priority_levels, min_CPU_time, max_CPU_time)
