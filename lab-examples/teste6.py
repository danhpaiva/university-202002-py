import requests

cabecalho = {'Content-type': 'application/json', 'Accept': 'text/plain'}

registro = {'id': 2345678, 'name': 'Elson de Abreu'}

response = requests.post('https://httpbin.org/post',
                         data=registro,
                         headers=cabecalho)

print('Codigo de status: ', response.status_code)

if (response.status_code == 200):
    rJson = response.json()

    print("Dados enviados por post:")
    print(rJson['data'])

    print("Content-Type = ", rJson['headers']['Content-Type'])
else:
    print('Ocorreu algo inesperado!')