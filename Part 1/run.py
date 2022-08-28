import time
import requests

website = 'https://webscraper.io/test-sites'

interval = 5

while True:
    try:
        info = requests.get(website)
        print(info)
    except:
        print(f'can not connect to server')
        print({
            'code':404,
            'status':'Fail'
        })
    
    print(f'will do it again in {interval} seconds')
    time.sleep(interval)