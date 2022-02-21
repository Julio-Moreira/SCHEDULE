# ;)
# ! {<J>}
# ! autor: Julio C. Moreira 
# ! feito entre 20/02/2022 ate 20/02/2022

# * BIBLIOTECAS {
from time import sleep
import sqlite3
conn = sqlite3.connect('/home/julio/med {<J>}/1 prog/PYTHON/projetos/agenda/agenda.db') # conecta com o banco
cursor = conn.cursor()
# cursor.execute('CREATE TABLE agenda (nome text,email text,telefone text,endereco text)') cria a tabela
# * }

# * MENU PRINCIPAL {
print('\033[32;1m-_-'*10,'\n\033[31;1m     SCHEDULE\n','\033[32;1m-_-\033[m'*10) 
sleep(0.2)
print('\n\033[31m[\033[36mc\033[31m]\033[36mregister \033[31m[\033[35ml\033[31m]\033[35mlist')
sleep(0.3)
esc = str(input('\n\033[31m[\033[36mr\033[31m/\033[35ml\033[31m]\n\033[32m: ')).strip().lower()[0]
# * }

# * CADASTRAR {
if esc == 'r':
    sleep(0.5)
    esc_cas = str(input('\n\033[36mput or to throw? ')).strip().lower()[0]
    if esc_cas == 'p':
        sleep(0.6)
        # * COLOCAR {
        nom = str(input('\n\033[31;1menter the name: ')).strip()
        ema = str(input('enter the email: ')).strip()
        tel = str(input('enter the telephone: ')).strip()
        end = str(input('enter the address: ')).strip()
        cursor.execute("INSERT INTO agenda VALUES ('"+nom+"','"+ema+"','"+tel+"','"+end+"')") # coloca os valores no banco
        conn.commit() # commita tudo
        print('\n\033[36mOK\nvalores cadastrados com sucesso!')
        # * }
    if esc_cas == 't':
        sleep(0.5)
        # * TIRAR {
        delet = str(input('\n\033[36mwhat do you want to erase? '))
        cursor.execute("DELETE FROM agenda WHERE nome LIKE "+delet+" ") # deleta de agenda onde nome for delet
        conn.commit()
        print('\n\033[35mOK\nvalores deletados com sucesso!')
        # * }
# * }
if esc == 'l':
    sleep(0.5)
    # * LISTAR {
    listar = cursor.execute("SELECT * FROM agenda")
    fet = str(listar.fetchall()) # transforma em str para deixar a saida mais bonita
    print('\n\033[31;1mname:   email:  telephone:   address:   ',fet.replace('[','').replace(']','').replace('(','\n').replace(')','').replace("'",'')) 
    # * }

conn.close() # desconecta do banco