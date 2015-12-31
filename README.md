# Combining ZeroMQ and Socket.IO

This example runs a Node.js server, a/several client(s) ask the server to perform a certain task. For maintainability and speed concerns the worker process is written in Python (we could easily replace it with C++)

Socket.IO is used to achieve client-server communication and ZeroMQ for "server - worker process" communication.

    - A client requests the server to perform a certain task (Socket.IO)
    - The server sends a request to the worker process (ZMQ)
    - The worker process completes the task and sends the output to the server (ZMQ)
    - The server dispatches the output to the right client (Socket.IO)

## How to

    - python worker.py
    - cd server
    - npm start
