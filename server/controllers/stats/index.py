
import csv
import time
from config.config import jobs_file


def get_stats():
    queue = []
    with open(jobs_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            queue.append(row)
    csvfile.close()
    with open('./shared/policy.txt', 'r') as policyfile:
        policy = policyfile.read()
    policyfile.close()
    total_exec_time = 0
    for job in queue:
        total_exec_time += int(job[1])
    # read in policy

    return {
        'expected_waiting_time': total_exec_time,
        'policy': policy}
