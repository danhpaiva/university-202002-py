import requests

r = requests.get('https://github.com/timeline.json')

print('Codigo de Retorno HTTP : ', r.status_code)

if (r.status_code == 200):
    print()
    print('JSON : ', r.json())
    print()
else:
    print('Nao houve sucesso na requisicao.')
