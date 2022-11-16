

# test <benchmark> <policy> <num_of_jobs> <priority_levels>
#      <min_CPU_time> <max_CPU_time>

import csv
import random
import time

from config.config import FCFS, PRI, SJF, tester_file
from job_queue.processor import clean_job_queue
from utils.reorder import fcfs, pri, sjf


total_submitted_jobs_t = 0

total_turnaround_time_t = 0
total_cpu_time_t = 0
total_waiting_time_t = 0
total_processing_time_t = 0
start_time_t = time.time()


average_turnaround_time_t = 0
average_cpu_time_t = 0
average_waiting_time_t = 0

# test_name fcfs 6 1 1 10


def tester(benchmark, policy, num_of_jobs, priority_levels, min_CPU_time, max_CPU_time):
    policy = policy.upper()
    if policy.upper() not in [FCFS, SJF, PRI]:
        print('Invalid policy')
        return

    global start_time_t
    start_time_t = time.time()

    #  clear the job queue
    with open(tester_file, 'w') as jobs_csv:
        writer = csv.writer(jobs_csv, lineterminator='\n')
        writer.writerows([])
        jobs_csv.close()

    for i in range(num_of_jobs):
        # generate a job
        # save it to tester_queue.csv
        # Job name, Execution time, Priority, Submitted time
        exec_time = random.randint(min_CPU_time, max_CPU_time)
        job_to_save = [str(i) + benchmark, exec_time,
                       priority_levels, time.time()]

        with open(tester_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(job_to_save)
            csvfile.close()

    # sort based on policy
    tester_re_organize(policy)
    global total_submitted_jobs_t
    total_submitted_jobs_t = num_of_jobs

    # run each job and log the performance
    for i in range(num_of_jobs):
        job = fetch_single_job()
        process_job(job)

    print_performance()


def tester_re_organize(policy):
    if(policy == FCFS):
        return fcfs(tester_file)
    elif(policy == SJF):
        return sjf(tester_file)
    elif(policy == PRI):
        return pri(tester_file)


def fetch_single_job():
    # read only one job read it as an array
    with open(tester_file, 'r') as jobs_csv:
        job_queue = list(csv.reader(jobs_csv))
        jobs_csv.close()
    job_queue = clean_job_queue(job_queue)

    if(len(job_queue) > 0):
        job = job_queue[0]
        job_queue = job_queue[1:]
        # write the new job queue
        with open(tester_file, 'w') as jobs_csv:
            #  no empty lines
            writer = csv.writer(jobs_csv, lineterminator='\n')
            writer.writerows(job_queue)
            jobs_csv.close()
    return job


def process_job(job):
    exec_time = job[1]
    job_name = job[0]
    time_submitted = job[3]
    for i in range(int(exec_time), 0, -1):
        str1 = 'Running job ' + job_name
        str2 = 'Time left: ' + str(i+1) + '/' + str(exec_time)
        # print(str1 + ' -- ' + str2)
        time.sleep(1)

    log_performance(time_submitted, exec_time)


def log_performance(time_submitted, exec_time):
    global total_submitted_jobs_t

    global average_turnaround_time_t
    global average_cpu_time_t
    global average_waiting_time_t

    global total_turnaround_time_t
    global total_cpu_time_t
    global total_waiting_time_t

    # calculate turnaround time
    turnaround_time = time.time() - float(time_submitted)
    total_turnaround_time_t += turnaround_time
    average_turnaround_time_t = total_turnaround_time_t / total_submitted_jobs_t

    # calculate cpu time
    cpu_time = int(exec_time)
    total_cpu_time_t += cpu_time
    average_cpu_time_t = total_cpu_time_t / total_submitted_jobs_t

    # calculate waiting time
    waiting_time = turnaround_time - cpu_time
    total_waiting_time_t += waiting_time
    average_waiting_time_t = total_waiting_time_t / total_submitted_jobs_t


def print_performance():
    global total_submitted_jobs_t

    global average_turnaround_time_t
    global average_cpu_time_t
    global average_waiting_time_t

    global total_turnaround_time_t
    global total_cpu_time_t
    global total_waiting_time_t

    print('Total number of jobs submitted: ' + str(total_submitted_jobs_t))
    print('Average turnaround time: ' + str(average_turnaround_time_t))
    print('Average CPU time: ' + str(average_cpu_time_t))
    print('Average waiting time: ' + str(average_waiting_time_t))
    print('Throughput: ' + str(total_submitted_jobs_t / (time.time() - start_time_t)))
