import threading
from config.config import policy_file_name
from utils.reorder import re_organize


async def change_policy_handler(body: dict, policy_lock: threading.Lock, jobs_lock: threading.Lock):
    print('changing policy')
    new_policy = body['policy']
    with policy_lock:
        # get old policy
        with open(policy_file_name, 'r') as f:
            old_policy = f.read()
            f.close()
        with open(policy_file_name, 'w') as policy_file:
            policy_file.write(new_policy)
            policy_file.close()
    if(old_policy == new_policy):
        print('policy is the same')
        return {'msg': 'policy not changed'}

    return re_organize(new_policy, jobs_lock)   # re_organize the jobs
    