import requests

dados = {'id': '2345678', 'name': 'Elson de Abreu'}

r = requests.get("http://httpbin.org/get", params=dados)

print('Codigo de status: ', r.status_code)

if (r.status_code == 200):
    print('Resposta Json:')
    print(r.json())

    print('URL da resposta:')
    print(r.url)