import requests
import json

base = 'USD'
qoute = 'RUB'
amount = 1

headers = {"apikey": "wSAiPyUjIkMtozybPJmVHKv1v4GgqPyd"}


def convert(base, qoute, amount):
    response = requests.get(f"https://api.apilayer.com/fixer/convert?" 
                            f"from={base}&to={qoute}&amount={amount}",
                            headers=headers)
    r = json.loads(response.text)['result']
    return r


def symbols():
    response = requests.get('https://api.apilayer.com/fixer/symbols',
                            headers=headers)
    r = json.loads(response.text)['symbols']
    for i in r:
        print(f'{i}: {r[i]}')
    return r


f = symbols()

# for i in f:
#print(f)

#print(convert('USD', 'RUB', 1))

