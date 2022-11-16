
import csv
import time
from config.config import jobs_file

import json

from job_queue.performance.main import tally_total_submitted_jobs


async def save_job(data, jobs_lock):
    print('Saving job', data['job_name'])
    #  saving job {'job_name': '2', 'exec_time': 2, 'priority': 2}
    job_name, exec_time,  priority = data['job_name'], data[
        'exec_time'], data['priority']
    # print('saving job', job_name, exec_time, priority)
    exec_time = str(exec_time)
    priority = str(priority)

    try:
        with jobs_lock:
            with open(jobs_file, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                submitted_time = time.time()
                writer.writerow(
                    [job_name, exec_time, priority, submitted_time])

                csvfile.close()
                print('Job saved!!')
                expected_wait_time = 0
                with open(jobs_file, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        expected_wait_time += int(row[1])
                    csvfile.close()
                tally_total_submitted_jobs()
                return {'msg': 'job submitted', 'job_name': job_name, 'exec_time': exec_time, 'priority': priority, 'submitted_time': submitted_time, 'expected_wait_time': expected_wait_time}

    except Exception as e:
        print('error saving job', e)
        return {'msg': 'error saving job'}
