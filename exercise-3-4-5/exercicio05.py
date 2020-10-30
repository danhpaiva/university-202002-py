import os
import sqlite3

os.system('cls')

option = ''
continue_ = ''
exit_ = '1'

# Conectando no banco
conn = sqlite3.connect('C:/py/bdpessoas.db')

# Criação do cursor para manipular dados sql
cursor = conn.cursor()

while exit_ == '1':
    os.system('cls')

    option = input(
        '\n\tMENU\nDigite:\n[1]Cadastrar pessoa | [2]Ver cadastro | [3]Atualizar cadastro | [4]Deletar cadastro | [5]Sair do programa:')

    if option == '1':
        os.system('cls')

        print('\tCadastrar Pessoas\n')

        person_code = input('Informe o código da pessoa: ')
        name = input('Informe o nome da pessoa: ')
        age = input('Informe a idade da pessoa: ')

        cursor.execute(
            "INSERT INTO pessoas (codpessoa, nome, idade) VALUES(" + person_code + ", '" + name + "', " + age + ")")
        conn.commit()

        continue_ = input(
            '\nDeseja cadastrar mais uma pessoa? [1]sim | [2]não :')

        while continue_ == '1':
            person_code = input('Informe o código da pessoa: ')
            name = input('Informe o nome da pessoa: ')
            age = input('Informe a idade da pessoa: ')

            cursor.execute(
                "INSERT INTO pessoas (codpessoa, nome, idade) VALUES(" + person_code + ", '" + name + "', " + age + ")")
            conn.commit()

            for linha in cursor.fetchall():
                print(linha)

            continue_ = input(
                '\nDeseja cadastrar mais uma pessoa? [1]sim | [2]não :')

    elif option == '2':
        os.system('cls')
        cursor.execute('SELECT * FROM pessoas')

        print('Registro de pessoas cadastradas:\n')

        for linha in cursor.fetchall():
            print(linha)
        input('Pressione ENTER...')

    elif option == '3':
        os.system('cls')
        print('Atualizar Cadastro')

        person_code = input('Digite o código da pessoa a ser atualizada: ')
        name = input('Informe o novo nome: ')
        age = input('Informe a nova idade: ')

        cursor.execute(
            "UPDATE pessoas SET nome='" + name + "', idade= " + age + " WHERE codpessoa= " + person_code)
        conn.commit()

    elif option == '4':
        print('Deletar Cadastro')

        person_code = input('Digite o código da pessoa a ser deletada: ')
        cursor.execute(
            "DELETE FROM pessoas WHERE codpessoa =" + person_code)
        conn.commit()

    elif option == '5':
        exit_ = '0'

    else:
        print('Opção inválida!')

print('\nObrigado por usar nosso programa!')

conn.close()
