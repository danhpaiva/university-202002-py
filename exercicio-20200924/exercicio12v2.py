import random
import requests
import time


def realizarRequisicao(url, temperatura, umidade):
    i = 1
    while i <= 15:
        valor = random.randrange(0, 45)
        valor2 = random.randrange(0, 45)
        r = requests.get(url + temperatura + str(valor) +
                         '&' + umidade + str(valor2))

        if (r.status_code == 200):
            print()
            print('Temperatura: Teste número ' + str(i) +
                  ' de requisição com o valor: ', str(valor))
        else:
            print('Teste número:' + str(i) +
                  ' não houve sucesso na requisição.')

        time.sleep(20)
        i += 1


# Substituir os XXXX pela sua chave da API
url = 'https://api.thingspeak.com/update?api_key=XXXXX&field'
temperatura = '1='
umidade = '2='

# Fazer requisição da temperatura e umidade ao mesmo tempo
print("Temperatura: Início do processo...")
realizarRequisicao(url, temperatura, umidade)
print()
