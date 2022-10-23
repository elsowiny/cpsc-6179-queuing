from cmath import inf
import csv
from config.config import jobs_file, normal_text, red_text, policy_file_name, FCFS, PRI, SJF


def re_organize(policy, jobs_lock):
    with jobs_lock:
        print('re-organizing the jobs, acquired lock')
        if(policy == FCFS):
            return fcfs()
        elif(policy == SJF):
            return sjf()
        elif(policy == PRI):
            return pri()


def fcfs():
    queue = []
    try:
        with open(jobs_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                queue.append(row)
        # sort the queue based on the submitted time
        queue.sort(key=lambda x: x[3])
        with open(jobs_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in queue:
                writer.writerow(row)
        return {'result': 'success', 'policy': FCFS, 'msg': 'The queue has been reordered based on the submitted time.'}
    except:
        return {'result': 'error', 'policy': FCFS, 'msg': 'There are no jobs in the queue.'}


def sjf():
    queue = []
    try:
        with open(jobs_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                queue.append(row)

        # sort the queue based on the execution time
        # we need to convert the execution time to an integer
        # so we can sort it
        queue.sort(key=lambda x: int(x[1]))

        with open(jobs_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in queue:
                writer.writerow(row)
        return {'result': 'success', 'policy': SJF, 'msg': 'The queue has been reordered based on the execution time.'}

    except:
        return {'result': 'error', 'policy': SJF, 'msg': 'There are no jobs in the queue.'}


def pri():

    queue = []
    try:
        with open(jobs_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                queue.append(row)

        queue = sorted(queue, key=lambda x: int(x[2]) if x[2] != '' else inf)

        with open(jobs_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in queue:
                writer.writerow(row)
        return {'result': 'success', 'policy': PRI, 'msg': 'The queue has been reordered based on the priority.'}
    except:
        return {'result': 'error', 'policy': PRI, 'msg': 'There are no jobs in the queue.'}
