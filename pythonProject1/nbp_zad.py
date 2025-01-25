import json

import requests
waluta = 'eur'
kurs = 1.24
# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
print(f" {waluta}, {kurs}")
# dane = {"table":"C","currency":"dolar amerykański","code":"USD","rates":[{"no":"064/C/NBP/2016","effectiveDate":"2016-04-04","bid":3.6929,"ask":3.7675}]}
code = 'usd'
x='2023-01-05'
dane = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{x}/')
ile = dane.json()
print(ile)
x='2023-01-06'
dane2 = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/2023-12-01/2024-01-01')
ile = dane2.json()
print(ile)
for subitem in ile["rates"]:
    print(subitem["effectiveDate"],subitem["mid"])







