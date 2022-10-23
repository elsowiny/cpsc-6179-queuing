from cmath import inf
import csv

import requests
from config.config import CHANGE_POLICY_API, jobs_file, normal_text, red_text, policy_file_name, FCFS, PRI, SJF


def change_policy():
    print('You selected the change option.')
    print('Please enter the new scheduling policy: ', end='')
    new_policy = input()
    new_policy = new_policy.upper()  # needs to be a valid policy
    if new_policy == FCFS or new_policy == SJF or new_policy == PRI:
        submit_new_policy(new_policy)
    elif new_policy == '5':
        print('You selected the exit option.')
        print('Exiting the scheduling module.')
        exit()
    elif new_policy == '':
        return
    else:
        print('Invalid scheduling policy. Please try again.')
        change_policy()


def submit_new_policy(policy):
    # send to the server
    # response = requests.post('http://localhost:5000/submit_event', json={'policy': policy})
    # print(response.text)
    try:
        response = requests.post(CHANGE_POLICY_API, json={'policy': policy})
        print(response.text)
    except:
        print('The server is not running. Please start the server and try again.')
