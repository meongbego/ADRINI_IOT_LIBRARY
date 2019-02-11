from adrini.tools import utils

def get_channels_data(url, id_channels, count, headers=None):
    url_fix= url+"/api/get/channels/"+id_channels
    json_data = {
        'count': str(count)
    }
    try:
        data = utils.get_http(url_fix, param=json_data,header=headers)
    except Exception as e:
        utils.log_err(e)
    else:
        return data

def get_channels_by_id(url, id_channels, params=None, headers=None, limit=None):
    url_fix= url+"/api/get/"+id_channels+"/limit/"+str(limit)
    try:
        data = utils.get_http(url_fix, param=params,header=headers)
    except Exception as e:
        utils.log_err(e)
    else:
        return data

def send_data_to_channels(url, id_channels, params=None, headers=None):
    url_fix= url+"/api/send/"+id_channels
    try:
        data = utils.get_http(url_fix, param=params,header=headers)
    except Exception as e:
        utils.log_err(e)
    else:
        return data
