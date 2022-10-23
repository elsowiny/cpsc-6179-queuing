baseApi = 'http://localhost:8000'

jobs_file = './shared/jobs.csv'
policy_file_name = './shared/policy.txt'
event_queue_file = './shared/event_queue.csv'
CURR_JOB_CSV = './shared/current_job.csv'
FCFS = 'FCFS'
PRI = 'PRI'
SJF = "SJF"
SUBMIT_JOB = 'submit_job'
CHANGE_POLICY = 'change_policy'

#  apis
SUBMIT_JOB_API = baseApi + '/submit_job'
SUBMIT_EVENT_API = baseApi + '/submit_event'
CHANGE_POLICY_API = baseApi + '/change_policy'
GET_JOBS_API = baseApi + '/jobs'


yellow = '\033[1;33m'
blue = '\033[94m'
white = '\033[97m'
red = '\033[1;31m'
purple = '\033[95m'
green = '\033[92m'
normal = '\033[0m'


def yellow_text(text):
    return yellow + text + yellow


def blue_text(text):
    return blue + text + blue


def white_text(text):
    return white + text + white


def red_text(text):
    return red + text + red


def purple_text(text):
    return purple + text + purple


def green_text(text):
    return green + text + green


def normal_text(text):
    return normal + text + normal
