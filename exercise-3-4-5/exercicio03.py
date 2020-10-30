import os
import sqlite3

os.system('cls')

print('Exercício 3\n')

# Conectando no banco
conn = sqlite3.connect('C:/py/bdpessoas.db')

person_code = input('Informe o código da pessoa: ')
name = input('Informe o nome da pessoa: ')
age = input('Informe a idade da pessoa: ')

# Criação do cursor para manipular dados sql
cursor = conn.cursor()
cursor.execute(
    "insert into pessoas (codpessoa, nome, idade) values(" + person_code + ", '" + name + "', " + age + ")")
conn.commit()

cursor.execute('select * from pessoas')

for linha in cursor.fetchall():
    print(linha)

conn.close()
