import os
import sqlite3

os.system('cls')

print('Exercício 4\n')

# Conectando no banco
conn = sqlite3.connect('C:/py/bdpessoas.db')

# Criação do cursor para manipular dados sql
cursor = conn.cursor()

cursor.execute('select * from pessoas')

print("Registro de pessoas cadastradas: \n")
for linha in cursor.fetchall():
    print(linha)

continue_ = '1'
continue_ = input('\nDeseja inserir mais um registro? [1]sim | [2]não :')

while continue_ == '1':
    person_code = input('Informe o código da pessoa: ')
    name = input('Informe o nome da pessoa: ')
    age = input('Informe a idade da pessoa: ')

    cursor.execute(
        "insert into pessoas (codpessoa, nome, idade) values(" + person_code + ", '" + name + "', " + age + ")")
    conn.commit()

    for linha in cursor.fetchall():
        print(linha)

    continue_ = input('\nDeseja inserir mais um registro? [1]sim | [2]não')

print('\nObrigado por usar nosso programa!')

conn.close()
