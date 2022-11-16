import uvicorn


def start():
    server_location = 'server.main:app'  # server/main.py:app
    uvicorn.run(server_location,
                host="0.0.0.0", port=8000, reload=True)


if __name__ == '__main__':
    start()
