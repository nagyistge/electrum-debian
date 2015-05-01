import requests



url = 'https://www.coinbase.com'
response = requests.request('get', url, verify='packages/requests/cacert.pem.old')
print response
print dir(response)

