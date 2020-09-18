import requests

url = 'https://viacep.com.br/ws/'
cep = ['31990510','31990511','31990512', '31990513', '31990514', '31990515']
formato = '/xml/'

for listaCep in cep:
    r = requests.get(url + listaCep + formato)

    if (r.status_code == 200):
        print()
        print('XML : \n', r.text)
        print()
    else:
        print('Nao houve sucesso na requisicao.')
