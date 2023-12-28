import re
import requests

# parse out lines with "SSID: "
# f = open('networks.txt', 'r')
# target = 'the target'


# arr = []
# searchText = 'S'
# for idx in f:
#     if re.search(searchText, idx):
#         #  write to file
#         # iterate string until after :
#         # then take str[counter:]
#         vals = idx.split(' ')
#         # won't work for SSID with spaces in name
#         ssid = vals[3].rsplit('\n')[0]
#         arr.append(ssid)


# print(arr)
# print('There are '+str(len(arr)-1)+ ' SSIDs availabe nearby '+ target)


# submit to wigle.com
lat = '32.93577327944811'
long = '-96.85119342925033'
# zoom, the higher the value, the more zoom, 2 - 22
zoom = '15'
url = f'https://wigle.net/mapsearch?maplat={lat}&maplon={long}&mapzoom={zoom}'
print(url)
ssid_supplied = input('enter ssid to search for: ')
data = {'ssid':ssid_supplied}

# pull cordinates on map and address information
x = requests.post(url, json=data)
print(x.text)
