import csv
import threading
import time
from config.config import CURR_JOB_CSV, jobs_file
from job_queue.performance.main import log_performance, start_performance
from job_queue.processor import clean_job_queue,  retrieve_single_job


def start_job_queue(jobs_lock, policy_lock):
    thread = threading.Thread(target=check_job_queue,
                              args=(jobs_lock, policy_lock), daemon=True)
    start_performance()
    thread.start()


def check_job_queue(jobs_lock, policy_lock):

    for i in range(10):
        print()
    print("<....starting job queue.....>")
    while True:
        jobs_lock.acquire()
        print('job queue has acquired lock')
        job_queue = get_jobs()
        jobs_lock.release()
        job_queue = clean_job_queue(job_queue)
        if(has_jobs()):
            job_to_process = retrieve_single_job(policy_lock)
            print('Preparing to process job: ' + job_to_process[0])
            process_job(job_to_process, get_queue_length())
        else:
            print('job queue is empty')

        # sleep for 15 seconds before checking again
            for i in range(15, 0, -1):
                print('sleeping ' + ('*') * (15-i+1),
                      "checking back in ", str(i * 1), "seconds")
                time.sleep(1)
            print('done sleeping restarting and resuming job queue checking')


def get_jobs():
    with open(jobs_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        job_queue = []
        for row in reader:
            job_queue.append(row)
        csvfile.close()
    return job_queue


def has_jobs():
    return get_queue_length() > 0


def get_queue_length():
    with open(jobs_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        job_queue = []
        for row in reader:
            job_queue.append(row)
        csvfile.close()
    return len(job_queue)


def process_job(job, queue_length):
    exec_time = job[1]
    job_name = job[0]
    time_submitted = job[3]
    # delete and write to current_job.csv
    with open(CURR_JOB_CSV, 'w') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow(job)
        csvfile.close()

    for i in range(int(exec_time), 0, -1):
        str1 = 'Running job ' + job_name
        str2 = 'Time left: ' + str(i+1) + '/' + str(exec_time)
        str3 = 'Jobs left: ' + str(queue_length)
        print(str1 + ' -- ' + str2 + ' --- ' + str3)
        time.sleep(1)

    log_performance(time_submitted, exec_time)
