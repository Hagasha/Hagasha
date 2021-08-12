import mysql.connector
from mysql.connector import Error, connect, cursor

global meuCursor
#Criando conexão com o banco de dados
conexao = mysql.connector.connect(host = "127.0.0.1", user = "root")

#Criando cursor
meucursor = conexao.cursor()

#Comando para conectar com o mysql
def conecta():
    try:
        connection = mysql.connector.connect(user = "root", host = "127.0.0.1")
        return connection
    except:
        print("Não foi possível conectar ao SGBD. \nVerifique o XAMPP/WAMP ou os dados de conexão.")
        return 1

#Comando para criar o banco de dados
def criaBanco():
    try:
        meucursor.execute('CREATE DATABASE bd_urna;')
        meucursor.execute('USE bd_urna;')
        print('conexão estabelecida \nbd_urna ok')
    except:
        meucursor.execute('USE bd_urna;')
        print('conexão estabelecida \nbd_urna ok')

#Comando para criar a tabela da urna
def tabelaUrna():
    try:
        meucursor.execute('''CREATE TABLE tabela_urna(
                            candidatos VARCHAR(100) PRIMARY KEY NOT NULL, 
                            numeros VARCHAR(2) NOT NULL,
                            votos INT NOT NULL,
                            foto VARCHAR(50));''')
    except Error as err:
        print("A tabela está ok!:", err)

def tabela_voto():
    try:
        meucursor.execute('''CREATE TABLE tabela_voto(
                            voto_direto INT NOT NULL, 
                            voto_branco INT NOT NULL,
                            voto_nulo INT NOT NULL);''')
    except Error as err:
        print("A tabela está ok!:", err)

def addVoto(id):
    try:
        if len(id) == 2 or id == 'VOTO NULO':
            try:
                print(len(id))
                meucursor.execute("SELECT votos FROM tabela_urna WHERE numeros = '{}'".format(id))

                for i in meucursor:
                    lista = []
                    for x in i:
                        lista.append(x)

                v = lista[0]
                v += 1
                print(v)
                meucursor.execute(f"UPDATE tabela_urna SET votos = '{v}' WHERE numeros = '{id}';")
                print('voto adicionado')

                meucursor.execute("SELECT voto_direto FROM tabela_voto")

                for i in meucursor:
                    lista = []
                    for x in i:
                        lista.append(x)
                    
                v = lista[0]
                v += 1
                print(v)
                meucursor.execute(f"UPDATE tabela_voto SET voto_direto = '{v}';")
                print('voto direto adicionado')
                conexao.commit()
            except UnboundLocalError:
                meucursor.execute("SELECT voto_nulo FROM tabela_voto")

                for i in meucursor:
                    lista = []
                    for x in i:
                        lista.append(x)
                    
                v = lista[0]
                v += 1
                print(v)
                meucursor.execute(f"UPDATE tabela_voto SET voto_nulo = '{v}';")
                print('voto adicionado')
                conexao.commit()
            
        elif id == 'VOTO BRANCO':
            meucursor.execute('USE bd_urna;')
            meucursor.execute("SELECT voto_branco FROM tabela_voto")

            for i in meucursor:
                lista = []
                for x in i:
                    lista.append(x)

            v = lista[0]
            v += 1
            print(v)
            meucursor.execute(f"UPDATE tabela_voto SET voto_branco = '{v}';")
            print('voto adicionado')
            conexao.commit()    

        else:
            pass
    except Error as err:
        print("Erro!:", err)

def locCandi(id):
    try:
        meucursor.execute('USE bd_urna;')
        meucursor.execute("SELECT candidatos FROM tabela_urna WHERE numeros = '{}';".format(id))

        for i in meucursor:
            l = []
            for x in i:
                l.append(x)
        return l[0]

    except:
        return 0

def selecFoto(id):
    try:
        meucursor.execute('USE bd_urna;')
        meucursor.execute("SELECT foto FROM tabela_urna WHERE numeros = '{}';".format(id))

        for i in meucursor:
            f = []
            for x in i:
                f.append(x)
        return f[0]

    except Error as err:
        print("Erro!:", err)
        
if __name__ == '__main__':
    conexao = conecta()
    if conexao != 1:
        meucursor = conexao.cursor()
        criaBanco()
        tabelaUrna()
        tabela_voto()

        conexao.close()
