import json
import logging
import os
import traceback
from typing import List

import requests
from flask import Flask, request
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)

CLIENT_LIST_CACHE_KEY = "CLIENT_LIST"
RUNNING_PORT = os.environ.get('RUNNING_PORT')
RUNNING_HOST = '0.0.0.0'


def get_client_list() -> List:
    cache_str = cache.get(CLIENT_LIST_CACHE_KEY)
    if cache_str:
        return json.loads(cache_str)
    else:
        return []


def assign_client_rank(client_ip_port):
    """
    Check if client ip is in cache, if not add
    :param client_ip_port:
    :return: Index of client in list
    """
    clients: List = get_client_list()
    if client_ip_port not in clients:
        clients.append(client_ip_port)
        cache.set(CLIENT_LIST_CACHE_KEY, json.dumps(clients))
        app.logger.info(pretty_print_ranks(clients))
    return clients.index(client_ip_port)


def unassign_client_rank(client_ip):
    """
    Remove client from cache and update
    :param client_ip: string
    :return: None
    """
    clients: List = get_client_list()
    clients.remove(client_ip)
    cache.set(CLIENT_LIST_CACHE_KEY, json.dumps(clients))
    app.logger.info("Clients list is + \n" +pretty_print_ranks(clients))


def pretty_print_ranks(clients):
    output = ""
    for index, client in enumerate(clients):
        output += f"{index} - {client} \n"
    return output


def send_command_to_client(sender_rank, command, client_address):
    payload = dict(sender=sender_rank, command=command)
    try:
        url = f"{client_address}/receive-command"
        response = requests.post(url, json=payload)
        return dict(success=response.ok)
    except Exception as e:
        app.logger.error(f"Failed to send request : {e}")
        traceback.print_exc()
        return dict(success=False)


@app.route("/assign-rank", methods=['POST', ])
def assign_rank():
    client_ip = request.json.get('ip_port')
    rank = assign_client_rank(client_ip)
    app.logger.info(f"IP {client_ip} registered with rank {rank}")
    return dict(rank=rank)


@app.route("/unassign-rank", methods=['DELETE', ])
def unassign_rank():
    client_ip = request.json.get('ip_port')
    app.logger.info(f"Received unassign rank request from {client_ip}")
    unassign_client_rank(client_ip)
    return dict(success=True)


@app.route("/send-command", methods=['POST'])
def send_command():
    client_data = request.get_json()
    command = client_data.get('command')
    client_ip_port = client_data.get('ip_port')
    sender_rank = assign_client_rank(client_ip_port)
    all_clients: List = get_client_list()
    clients_who_can_execute = all_clients[sender_rank+1:]
    app.logger.info(f"Received command from rank {sender_rank}. "
                    f"Sending to {len(clients_who_can_execute)}/{len(all_clients)}")
    response = {}
    for client_address in clients_who_can_execute:
        response_data = send_command_to_client(sender_rank, command, client_address)
        response[client_address] = response_data
    return response


if __name__ == "__main__":
    app.run(host=RUNNING_HOST, port=RUNNING_PORT)
