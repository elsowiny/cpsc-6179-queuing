from server.controllers.stats.index import get_stats
import csv
from server.controllers.stats.index import get_stats
from config.config import SUBMIT_JOB, jobs_file, event_queue_file


async def get_jobs(jobs_lock):
    try:
        jobs = []
        with jobs_lock:
            with open(jobs_file, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    jobs.append(row)
                csvfile.close()

            stats = get_stats()
            stats['jobs'] = jobs
            return stats
    except Exception as e:
        print('error getting jobs', e)
        return {'msg': 'error getting jobs'}
        