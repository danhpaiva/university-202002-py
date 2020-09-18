import requests

r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})

logRequisicao = open('logRequisicao.html', 'w')

if (r.status_code == 200):
    logRequisicao.write(r.text)
    print()
    print('A requisição foi atendida. Verifique na pasta um arquivo .html gerado pelo programa.\nCódigo : ', r.status_code)
    print()
else:
    logRequisicao.write("Código do Erro: " + str(r.status_code))
    print('Não houve sucesso na requisição. Verifique na pasta um arquivo .html com o código do erro.')

logRequisicao.close()