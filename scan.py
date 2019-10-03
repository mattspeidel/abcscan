import requests

with open('skulist.txt') as file:
    sku_list = file.read().splitlines()

for sku in sku_list:
    response = requests.get(f'http://durhamabc.tagretail.com/transack/live_qoh/locations.json?plu={sku}')
    print(response.json()['plu']['description'])
    if response.json()['store_quantities'] == []:
        print('NO STOCK')
    else:
        for store in response.json()['store_quantities']:
            print(store['address'])
            print(store['qoh'])