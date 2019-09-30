import requests

response = requests.get('http://durhamabc.tagretail.com/transack/live_qoh/locations.json?plu=27001')

json_response = response.json()

store_quantities = json_response['store_quantities']