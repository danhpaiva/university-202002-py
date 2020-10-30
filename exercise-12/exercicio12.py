import random
import requests
import time


def realizarRequisicao(url, medida):
    i = 1
    while i <= 15:
        valor = random.randrange(0, 45)
        r = requests.get(url + medida + str(valor))

        if (r.status_code == 200):
            print()
            print('Teste número ' + str(i) +
                  ' de requisição com o valor: ', str(valor))
        else:
            print('Teste número:' + str(i) +
                  ' não houve sucesso na requisição.')

        time.sleep(15)
        i += 1


url = 'https://api.thingspeak.com/update?api_key=XXXXXXXXXX&field' # Substituir os XXXX pela sua chave da API
temperatura = '1='
umidade = '2='

# Fazer requisição da temperatura
print("Temperatura: Início do processo...")
realizarRequisicao(url, temperatura)
print()

# Fazer requisição da umidade
print("Umidade: Início do processo...")
realizarRequisicao(url, umidade)
print()
