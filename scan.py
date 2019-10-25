import requests
import os
from twilio.rest import Client
import schedule
import time

account_sid = os.getenv('TWILSID')
auth_token = os.getenv('TWILTOKEN')
client = Client(account_sid, auth_token)


def scanner():
    newstock = []
    output = ''
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
            newstock.append(response.json()['plu']['description'])
            output += response.json()['plu']['description'] + " "

    with open('instock.txt') as oldstock:
        comparestock = oldstock.read().splitlines()

    if sorted(newstock) == sorted(comparestock):
        print('---NO CHANGES---')
    else:
        with open('instock.txt', 'w') as instock:
            for item in newstock:
                instock.write('%s\n' % item)
        print('---CHANGES WERE MADE---')
        message = client.messages \
                    .create(
                        body=output + 'are in stock now',
                        from_=os.getenv('MYTWILNUMBER'),
                        to=os.getenv('MYPHONENUMBER')
                    )

        print(message.sid)

def status_update():
    message = client.messages \
                .create(
                    body='ABCScan is running',
                    from_=os.getenv('MYTWILNUMBER'),
                    to=os.getenv('MYPHONENUMBER')
                )
    print(message.sid)


scanner()
schedule.every().day.at("00:00").do(status_update)
schedule.every().day.at("08:00").do(scanner)
schedule.every().day.at("12:00").do(scanner)
schedule.every().day.at("16:00").do(scanner)


while True:
    schedule.run_pending()
    time.sleep(60)