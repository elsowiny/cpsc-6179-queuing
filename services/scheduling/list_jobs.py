import csv

import requests
from config.config import jobs_file, normal_text, red_text, GET_JOBS_API
# This function will be called when the user
# selects the list option.


def list_jobs():
    # jobname,execution_time,priority, submitted_time
    try:
        print('You selected the list option.')
        stats = requests.get(GET_JOBS_API).json()
        jobs = stats['jobs']
        policy = stats['policy']
        expected_waiting_time = stats['expected_waiting_time']
        jobs_len = len(jobs)
        list_print(jobs_len, policy, expected_waiting_time)
    except:
        print('error listing jobs')


def list_print(jobs_len, policy, expected_waiting_time):
    print('Total number of jobs in the queue: ' + str(jobs_len))
    print('Scheduling policy: ' + policy)
    print('Expected waiting time: ' + str(expected_waiting_time))
    print('Job name, Execution time, Priority, Submitted time')
