import requests
from config.config import PERFORMANCE_API


def get_performance():
    try:
        response = requests.get(PERFORMANCE_API).json()
        print("🚀 ~ file: get_performance.py ~ line 7 ~ response", response)
        print('Total number of jobs submitted: ' +
              str(response['total_submitted_jobs']))
        print('Average turnaround time: ' +
              str(response['average_turnaround_time']))
        print('Average CPU time: ' + str(response['average_cpu_time']))
        print('Average waiting time: ' + str(response['average_waiting_time']))
        print('Throughput: ' + str(response['throughput']))
    except Exception as e:
        print('error getting performance', e)
