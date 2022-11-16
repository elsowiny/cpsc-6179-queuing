# global
# performance variables

import time


total_submitted_jobs = 0

total_turnaround_time = 0
total_cpu_time = 0
total_waiting_time = 0
total_processing_time = 0
start_time = time.time()


average_turnaround_time = 0
average_cpu_time = 0
average_waiting_time = 0


def log_performance(time_submitted, exec_time):
    global total_submitted_jobs

    global average_turnaround_time
    global average_cpu_time
    global average_waiting_time

    global total_turnaround_time
    global total_cpu_time
    global total_waiting_time

    # calculate turnaround time
    turnaround_time = time.time() - float(time_submitted)
    total_turnaround_time += turnaround_time
    average_turnaround_time = total_turnaround_time / total_submitted_jobs

    # calculate cpu time
    cpu_time = int(exec_time)
    total_cpu_time += cpu_time
    average_cpu_time = total_cpu_time / total_submitted_jobs

    # calculate waiting time
    waiting_time = turnaround_time - cpu_time
    total_waiting_time += waiting_time
    average_waiting_time = total_waiting_time / total_submitted_jobs

    # calculate throughput ?


def tally_total_submitted_jobs():
    global total_submitted_jobs
    total_submitted_jobs += 1
    print('Job tally: ' + str(total_submitted_jobs))


def get_performance():
    global average_turnaround_time
    global average_cpu_time
    global average_waiting_time
    global total_submitted_jobs

    # print('Total number of jobs submitted: ' + str(total_submitted_jobs))
    # print('Average turnaround time: ' + str(average_turnaround_time))
    # print('Average CPU time: ' + str(average_cpu_time))
    # print('Average waiting time: ' + str(average_waiting_time))
    # print('Throughput: ' + str(total_submitted_jobs / (time.time() - start_time)))
    return {'total_submitted_jobs': total_submitted_jobs, 'average_turnaround_time': average_turnaround_time, 'average_cpu_time': average_cpu_time, 'average_waiting_time': average_waiting_time, 'throughput': total_submitted_jobs / (time.time() - start_time)}


def start_performance():
    global start_time
    start_time = time.time()
