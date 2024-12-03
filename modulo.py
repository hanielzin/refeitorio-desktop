#IMPORTANDO AS CONSTANTES
import consts as c
import mysql.connector

#FUNÇÃO BANCO PARA CONEXÃO E CONSULTA 
def banco(consulta):
    #TENTA FAZER CONEXÃO COM BANCO DE DADOS
    try: 
        #CRIA A CONEXÃO
        conexao = mysql.connector.connect(
            host = c.server,
            user = c.usuario,
            password = c.senha,
            database = c.bd
        )

        #CRIA UM CURSOR
        cursor = conexao.cursor()
        #EXECUTA A CONSULTA
        cursor.execute(consulta)

        #VERIFICA SE A CONSULTA É UM SELECT
        if consulta.split()[0].upper() == 'SELECT':
            #LÊ TODOS OS ELEMENTOS 
            resultado = cursor.fetchall()
            return resultado
        else:
            #EDITA NO BANCO DE DADOS O COMANDO EXECUTADO
            conexao.commit()
            resultado = cursor
            return resultado 
        
    #VERITICA SE HÁ ALGUM ERRO DE CONSULTA OU CONEXÃO
    except mysql.connector.Error as e:
        print(f'Erro ao executar consulta ou conectar ao banco de dados {e}')
        exit()

    #FECHA O CURSOR E A CONEXÃO COM BANCO INDEPENDENTE DE OCORRER UM ERRO
    finally:
        if cursor:
            cursor.close()
        if conexao.is_connected():
            conexao.close()