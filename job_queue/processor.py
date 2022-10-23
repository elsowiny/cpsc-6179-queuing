

import csv
import threading
import time
from config.config import CHANGE_POLICY, SUBMIT_JOB, jobs_file, policy_file_name


from server.controllers.submit_job.index import save_job


def clean_job_queue(job_queue):
    new_job_queue = []
    if(len(job_queue) == 0):
        return new_job_queue
    for job in job_queue:
        if(len(job) > 0):
            new_job_queue.append(job)
    return new_job_queue


def retrieve_single_job(job_lock):
    with job_lock:
        # read only one job read it as an array
        with open(jobs_file, 'r') as jobs_csv:
            job_queue = list(csv.reader(jobs_csv))
            jobs_csv.close()
        job_queue = clean_job_queue(job_queue)

        if(len(job_queue) > 0):
            job = job_queue[0]
            job_queue = job_queue[1:]
            # write the new job queue
            with open(jobs_file, 'w') as jobs_csv:
                #  no empty lines
                writer = csv.writer(jobs_csv, lineterminator='\n')
                writer.writerows(job_queue)
                jobs_csv.close()
    return job
