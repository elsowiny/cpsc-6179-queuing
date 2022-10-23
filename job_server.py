# script for bus server located in events/bus.py
import threading
import uvicorn


def start():
    # start_event_queue_processor()  # start the event queue processor
    # run the python script that starts the bus server
    server_location = 'server.main:app'
    uvicorn.run(server_location,
                host="0.0.0.0", port=8000, reload=True)


if __name__ == '__main__':
    start()
