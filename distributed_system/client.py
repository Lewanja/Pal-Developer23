import logging
import os
import random
import socket
import threading
import time
import traceback

import requests
from flask import Flask, request

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.logger.setLevel(logging.INFO)

SERVER_URL = os.environ.get("SERVER_URL")
RUNNING_PORT = os.environ.get("RUNNING_PORT")
RUNNING_HOST = '0.0.0.0'
COMMANDS = [
    "START_TRANSMIT",
    "STOP_TRANSMIT",
    "PAUSE_TRANSMIT",
    "RESTART_TRANSMIT"
]
MIN_SEND_COMMAND_INTERVAL = 10
MAX_SEND_COMMAND_INTERVAL = 60


def send_command(command):
    """
    Make http call to server with command
    :return:
    """
    url = f"{SERVER_URL}/send-command"
    ip_port = get_self_ip_address_and_port()
    payload = dict(command=command, ip_port=ip_port)
    try:
        response = requests.post(url, json=payload, )
        app.logger.debug(f"send_command response status : {response.status_code}, payload {response.text}")
        return True
    except Exception as e:
        app.logger.error(f"Failed to send command to server {e}")
        traceback.print_exc()
        return False


def register_with_server():
    url = f"{SERVER_URL}/assign-rank"
    try:
        ip_port = get_self_ip_address_and_port()
        payload = dict(ip_port=ip_port)
        response = requests.post(url, json=payload)
        app.logger.debug(f"Register with server response : {response.status_code} - {response.text}")
    except Exception as e:
        app.logger.error(f"Failed to register with server : {e}")
        traceback.print_exc()


def send_exit_call():
    url = f"{SERVER_URL}//unassign-rank"
    try:
        ip_port = get_self_ip_address_and_port()
        payload = dict(ip_port=ip_port)
        response = requests.delete(url, json=payload)
        app.logger.debug(f"Exit response : {response.status_code} - {response.text}")
    except Exception as e:
        app.logger.error(f"Failed to make exit call : {e}")
        traceback.print_exc()


def execute_command(command, sender):
    app.logger.info(f"Received command : {command} from {sender}")


def get_self_ip_address_and_port():
    hostname = socket.gethostname()
    app.logger.debug(f"Host name is {hostname}")
    ipaddress = socket.gethostbyname(hostname)
    port = RUNNING_PORT
    return f"http://{ipaddress}:{port}"


def send_command_in_background():
    time_to_sleep = random.randint(MIN_SEND_COMMAND_INTERVAL, MAX_SEND_COMMAND_INTERVAL)
    time.sleep(time_to_sleep)
    command = random.choice(COMMANDS)
    send_command(command)
    send_command_in_background()


def start_background_send_command():
    """
    Start a new thread in the background to make a send_command call at random intervals
    :return: None
    """
    thread = threading.Thread(target=send_command_in_background)
    thread.start()


@app.route("/receive-command", methods=['POST', ])
def receive_command():
    payload = request.get_json()
    command = payload.get('command')
    sender = payload.get('sender')
    execute_command(command, sender)
    return {}


if __name__ == "__main__":
    register_with_server()
    start_background_send_command()
    app.run(host=RUNNING_HOST, port=RUNNING_PORT)
    send_exit_call()
