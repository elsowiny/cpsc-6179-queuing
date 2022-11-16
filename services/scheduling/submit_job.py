import requests
from config.config import SUBMIT_JOB_API, blue_text, green_text, red_text

from config.config import red_text, purple_text


def submit_job():
    print(green_text('You selected option: Submit Job.'))
    print(blue_text('Please enter the job name: '), end='')
    job_name = input()
    exec_time = handle_sanitized_input(exec_input=True)
    priority = handle_sanitized_input()

    #  post to event bus
    #  event bus will save job to queue
    try:
        body = {
            'job_name': job_name,
            'exec_time': exec_time,
            'priority': priority,

        }
        # requests.post(SUBMIT_JOB_API, json=body)
        response = requests.post(SUBMIT_JOB_API, json=body)
        print(response.text)
    except:
        print(red_text('There was an error submitting the job.'))
        print()


def handle_sanitized_input(exec_input=False):
    if(exec_input):
        print(purple_text('Please enter the execution time: '), end='')
    else:
        print(blue_text('Please enter the priority: '), end='')
    try:
        user_input = input()
        if(user_input == '' and type != EXEC):
            print('no priority')
            return ''
        converted = int(user_input)
        return converted
    except:
        print(red_text('Please enter a number'))
        return handle_sanitized_input(type)
