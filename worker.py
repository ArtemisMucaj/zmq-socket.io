import json
import zmq


def worker(socketID, content):
    # Send output
    json_string = '{"socketID":"'+socketID+'", "output" :"'+str("hello world "+str(content))+'"}'
    socket.send_string(json_string)
    pass


def waitForWorker():
    while True:
        message = sub.recv()
        if message:
            obj = json.loads(str(message))
            worker(obj["socketID"], obj["content"])
    pass

if __name__ == '__main__':
    # insantiate a subscriber
    context = zmq.Context()
    sub = context.socket(zmq.SUB)
    sub.setsockopt(zmq.SUBSCRIBE, b'')
    sub.connect("tcp://127.0.0.1:5555")
    # instantiate a publisher (send to nodejs server)
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:5556")

    print("Waiting for work")

    waitForWorker()
