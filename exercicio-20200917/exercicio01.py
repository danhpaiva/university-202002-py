import requests

url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'

r = requests.get(url + cep + formato)

if (r.status_code == 200):
    print()
    print('XML : \n', r.text)
    print()
else:
    print('Não houve sucesso na requisição.')
