import csv
import pathlib
import sys
import threading
import time
from fastapi import FastAPI
from config.config import SUBMIT_JOB, jobs_file, event_queue_file
from pathlib import Path
from job_queue.check.main import start_job_queue
from server.controllers.change_policy.main import change_policy_handler
from server.controllers.get_jobs.main import get_jobs
from server.controllers.stats.index import get_stats
from server.controllers.submit_job.index import save_job
import uvicorn

app = FastAPI()

# spin up our thread and lock

jobs_lock = threading.Lock()
policy_lock = threading.Lock()

# start the job queue
start_job_queue(jobs_lock=jobs_lock, policy_lock=policy_lock)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/submit_job")
async def submit_job(body: dict):
    return await save_job(body, jobs_lock)


@app.post("/change_policy")
async def change_policy(body: dict):
    return await change_policy_handler(body, policy_lock, jobs_lock)


@app.get("/jobs_lock")
async def jobs_lock_func():
    return jobs_lock


@app.get("/jobs")
async def jobs():
    return await get_jobs(jobs_lock)


@app.get("/stats")
async def stats():
    return get_stats()


# @app.get("/stats/list")
# async def stats_list():
#     stats = get_stats()
#     jobs = get_jobs()


@app.get("/health")
async def health():
    return {"message": "OK"}
