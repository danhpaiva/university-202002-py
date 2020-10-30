from datetime import datetime
import os
import random
import requests
import sqlite3
import time


def alimentarBancoDados():

    indice = verificarIndiceBanco()

    conn = conectarBanco()

    for i in range(10):

        temperature = random.randrange(0, 45)
        humidity = random.randrange(0, 100)

        # comando original do sqlite3 para pegar a data e hora atual no nosso fuso
        date = "datetime('now','localtime')"

        # Criação do cursor para manipular dados sql
        cursor = conn.cursor()

        # Incrementando o índice para não dar erro no banco de dados
        indice += 1
        cursor.execute(
            f"insert into Sensores (id, temperature, humidity, date) values({str(indice)}, {str(temperature)},{str(humidity)},{str(date)})")
        conn.commit()

    cursor.execute('select * from Sensores')

    for linha in cursor.fetchall():
        print(linha)

    fecharBanco(conn)


def realizarRequisicao(url, temperatura, umidade, data):

    backupThingSpeak = verificarQuantidadeBackupThingSpeak()

    if backupThingSpeak == None:
        backupThingSpeak = 0

    # Pegar primeiro índice válido do banco
    backupThingSpeak += 1

    databaseSQLiteLenght = verificarIndiceBanco()

    conn = conectarBanco()

    while backupThingSpeak <= databaseSQLiteLenght:
        valor = ''
        valor2 = ''
        valor3 = ''
        cursor = conn.cursor()

        cursor.execute(
            f'select * from Sensores where id={str(backupThingSpeak)}')

        for linha in cursor.fetchall():
            valor = linha[1]
            valor2 = linha[2]
            valor3 = linha[3]

        r = requests.get(url + temperatura + str(valor) +
                         umidade + str(valor2) + data + str(valor3))

        if (r.status_code == 200):
            print(
                f'\nBackup {str(backupThingSpeak)}º\nTemperatura: {str(valor)}\nUmidade:{str(valor2)}\nData:{str(valor3)}')
        else:
            print(
                f'\nBackup {str(backupThingSpeak)}º não houve sucesso na requisição.')

        time.sleep(20)
        backupThingSpeak += 1
    fecharBanco(conn)


def conectarBanco():
    # Conectando no banco
    conn = sqlite3.connect('C:/ex/db-sensores.db')
    return conn


def fecharBanco(conn):
    conn.close()


def verificarIndiceBanco():
    conn = conectarBanco()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) from Sensores')
    indice = 0
    for linha in cursor.fetchall():
        indice = linha[0]
    fecharBanco(conn)
    return indice


def verificarQuantidadeBackupThingSpeak():
    url = 'https://api.thingspeak.com/channels/1211372/feeds.json?api_key=8ZPLECEO2HMX8JFV&results=1'
    r = requests.get(url)
    data = r.json()
    channel_lenght = data['channel']['last_entry_id']
    return channel_lenght


print('\tExercício 13')

os.system('cls')

url = 'https://api.thingspeak.com/update?api_key=Z4CXNR24JO3PNN4L&'
temperatura = 'field1='
umidade = '&field2='
data = '&field3='

alimentarBancoDados()

print("\nInício do processo de backup no ThingSpeak...")
realizarRequisicao(url, temperatura, umidade, data)
print()
