import json
import requests
import coloredlogs
import logging

def question(word):
    answer = False
    while answer not in ["y", "n"]:
        answer = input("{} [y/n]? ".format(word)).lower().strip()

    if answer == "y":
        answer = True
    else:
        answer = False
    return answer

def log_rep(stdin):
    coloredlogs.install()
    logging.info(stdin)

def log_warn(stdin):
    coloredlogs.install()
    logging.warn(stdin)

def log_err(stdin):
    coloredlogs.install()
    logging.error(stdin)

def send_http(url, data, headers=None):
    json_data = json.dumps(data)
    send = requests.post(url, data=json_data, headers=headers)
    respons = send.json()
    data = json.loads(respons['data'])
    respons['data'] = data
    return respons

def get_http(url, param=None, header=None):
    json_data = None
    if param:
        json_data = param
    get_func = requests.get(url, params=json_data, headers=header)
    data = get_func.json()
    return data
