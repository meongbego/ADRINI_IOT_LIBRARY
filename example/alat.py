from adrini import Adrini 


url = 'iot.penapalu.id'
port = '6969'
url_yes = url+":"+port
apikey = "2ffaf8a9-d6d2-4ec9-8da7-90bf9783e3ae410349097441296385"
id_channels = "410349196528746497"

# GET DATA BY CHANNELS
iot = Adrini(url_yes, id_channels, apikey)
data_channels = iot.get_channels(4)
print("############################################")
print("DATA CHANNELS")
print("############################################")
print(data_channels)
print("############################################")

# SEND DATA TO CHANNEL BY ID
param_channels_send = {
    "sensor1": "0",
    "sensor2": "1",
    "sensor3": "1"
}
response_send = iot.send_channels(param_channels_send)
print("############################################")
print("SEND DATA TO CHANNELS")
print("############################################")
print(response_send)
print("############################################")

# GET DATA CHANNEL BY ID
param_channels_by_sensor = {
    "sensor": "sensor1",
    "sensor1": "sensor2"
}
data_channels_id = iot.get_channels_id(param_channels_by_sensor)
print("############################################")
print("DATA CHANNELS BY ID")
print("############################################")
print(data_channels_id)
print("############################################")



