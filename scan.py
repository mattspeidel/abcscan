import requests

# response = requests.get('http://durhamabc.tagretail.com/transack/live_qoh/locations.json?plu=27001')

# json_response = response.json()

# store_quantities = json_response['store_quantities']

sku_list = [27169, 20590, 20595, 20594, 27090, 27118, 25568, 20592, 20570, 20752, 20715, '00013', 27001, 20020]

for sku in sku_list:
    response = requests.get(f'http://durhamabc.tagretail.com/transack/live_qoh/locations.json?plu={sku}')
    print(response.json()['plu']['description'])
    if response.json()['store_quantities'] == []:
        print('NO STOCK')
    else:
        for store in response.json()['store_quantities']:
            print(store['address'])
            print(store['qoh'])