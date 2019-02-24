from adrini import Adrini 


url = 'https://iot.penapalu.club'
apikey = "fa4821fc-91dc-43dd-8e73-a578da2f7cc7428414508716425217"
id_channels = "428414886846103553"

# GET DATA BY CHANNELS
iot = Adrini(url, id_channels, apikey)
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
    "sensor3": "1",
    "sensor4": "1",
    "lampu1": "100",
    "lampu2": "200",
    "lampu3": "300",
    "lampu4": "400"
}
response_send = iot.send_channels(param_channels_send)
print("############################################")
print("SEND DATA TO CHANNELS")
print("############################################")
print(response_send)
print("############################################")

# GET DATA CHANNEL BY ID
param_channels_by_sensor = {
    "field1": "sensor1",
    "field2": "sensor2",
    "field3": "sensor3",
    "field4": "sensor4",
    "field5": "lampu1",
    "field6": "lampu2",
    "field7": "lampu3",
    "field8": "lampu4",
}
data_channels_id = iot.get_channels_id(param_channels_by_sensor)
print("############################################")
print("DATA CHANNELS BY ID")
print("############################################")
print(data_channels_id)
print("############################################")



